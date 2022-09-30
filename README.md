# audioWhisper

## Setup
1. choose envs of your choices.
2. clone this repo into your local storage.
3. run `pip install -r requirements.txt`
4. run `python audioWhisper.py`

## Command-line flags
|      --flags          |      Parameters         |  Default Value  |      Description                                                                                       |
|:---------------------:|:-----------------------:|:---------------:|:------------------------------------------------------------------------------------------------------:|
|`--devices`            |  true, false            |  false          | To print all available devices                                                                         |
|`--model`              |  model name             |  small          | Select model list. refer [here](https://github.com/openai/whisper#available-models-and-languages)      |
|`--task`               |  transcribe, translate  |  transcribe     | Choose between transcribe the audio or to translate the audio to English                               |
|`--device_index`       | index of output device  |  2              | Choose the output device to listen to and transcribe the audio from this device                        |

