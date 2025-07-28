# RUAccent Node for ComfyUI

✨ A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that adds **automatic stress marking (accenting)** to Russian text using the [RUAccent](https://github.com/Den4ikAI/ruaccent) library.

## What It Does

This node uses advanced NLP models to place stress accents (`+`) in Russian words, which is useful for:

* Text-to-speech systems
* Audiobook preparation
* Linguistic analysis
* Rhythmic or poetic formatting

## Features

* 🧠 Supports multiple RUAccent models: `tiny`, `turbo`, `turbo3.1`, `big_poetry`, and more
* 🧹 Can use dictionary-based or purely neural accenting
* ↺ Optional manual model reload (`force_reload`)
* 🗾 Allows custom accent dictionaries
* ⚙️ Runs on CPU or GPU

## Installation

1. **Copy the node files**
   Place all project files into a subfolder (e.g. `ComfyUI-RUAccent/`) inside your `ComfyUI/custom_nodes/` directory.

2. **Install RUAccent**
   Make sure Python 3.9+ is installed in your environment, then run:

```bash
pip install -r requirements.txt
```

## Node Parameters

| Name             | Type      | Description                                                        |
| ---------------- | --------- | ------------------------------------------------------------------ |
| `text`           | `STRING`  | Russian text to process                                            |
| `model_size`     | `CHOICE`  | Model to use (`tiny`, `turbo`, etc.)                               |
| `use_dictionary` | `BOOLEAN` | Enable RUAccent built-in dictionary                                |
| `tiny_mode`      | `BOOLEAN` | Use reduced model pipeline                                         |
| `device`         | `CHOICE`  | `CPU` or `CUDA` (currently only CPU tested)                        |
| `force_reload`   | `BOOLEAN` | Forces reload of the model                                         |
| `custom_dict`    | `STRING`  | Python-style dictionary of manual accents (`{'слово': 'сл+ ово'}`) |

## Example Output

**Input:**

```
на двери висит замок
```

**Output:**

```
на двер+и вис+ит зам+ок
```

## Acknowledgements

* Thanks to Den4ikAI for [RUAccent](https://github.com/Den4ikAI/ruaccent)
* Built for use with [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

---

## License

This node is released under the MIT License.
RUAccent has its own license — please check their repo for details.
