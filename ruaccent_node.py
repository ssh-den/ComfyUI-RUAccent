from ruaccent import RUAccent
import ast

class RUAccentApply:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "model_size": (
                    ["tiny", "tiny2", "tiny2.1", "turbo", "turbo2", "turbo3", "turbo3.1", "big_poetry"],
                    {"default": "turbo3.1"}
                ),
                "use_dictionary": ("BOOLEAN", {"default": True}),
                "tiny_mode": ("BOOLEAN", {"default": False}),
                "device": (["CPU", "CUDA"], {"default": "CPU"}),
                "force_reload": ("BOOLEAN", {"default": False}),
                "custom_dict": ("STRING", {"multiline": True, "default": ""}),  # Expecting Python dict literal
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("accented_text",)
    FUNCTION = "run"
    CATEGORY = "Text/Processing"

    def __init__(self):
        self.accentizer = None
        self.loaded_config = None

    def run(self, text, model_size, use_dictionary, tiny_mode, device, force_reload, custom_dict):
        # Empty input check
        if not text.strip():
            return ("",)

        # Try to parse custom_dict safely
        parsed_custom_dict = {}
        if custom_dict.strip():
            try:
                parsed_custom_dict = ast.literal_eval(custom_dict)
                if not isinstance(parsed_custom_dict, dict):
                    parsed_custom_dict = {}
            except Exception:
                parsed_custom_dict = {}

        # Create config signature for caching
        config = (model_size, use_dictionary, tiny_mode, device, str(parsed_custom_dict))

        # Load or reload model if config changed or force_reload is True
        if self.accentizer is None or self.loaded_config != config or force_reload:
            self.accentizer = RUAccent()
            self.accentizer.load(
                omograph_model_size=model_size,
                use_dictionary=use_dictionary,
                tiny_mode=tiny_mode,
                device=device,
                custom_dict=parsed_custom_dict,
            )
            self.loaded_config = config

        result = self.accentizer.process_all(text)
        return (result,)

NODE_CLASS_MAPPINGS = {
    "RUAccentApply": RUAccentApply,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RUAccentApply": "RUAccent: Расстановка ударений",
}
