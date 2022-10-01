# audioWhisper
Listen to any audio stream on your machine and print out the transcribed or translated audio. Based on OpenAI's [Whisper](https://github.com/openai/whisper) project. 

## Prerequisites

1. [**Turn on stereo mix settings on windows first before running the script**](https://www.howtogeek.com/howto/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/)
2. [**Install and add ffmpeg to your PATH**](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10#:~:text=Click%20New%20and%20type%20the,Click%20OK%20to%20apply%20changes.)
3. [**Install CUDA to your system**](https://developer.nvidia.com/cuda-downloads) 
## Setup

1. choose envs of your choices.
2. clone this repo into your local storage.
3. run ```pip install -r requirements.txt```
4. run ```python audioWhisper.py --devices true``` to get `device_index` and `channel`
5. run ```python audioWhisper.py ```. Make sure to define the index of `Stereo Mix` output device if it is not `2`.

<img src="https://raw.githubusercontent.com/Awexander/audioWhisper/main/screenshots/--deviceslist.png">

## Command-line flags
|      --flags          |  Default Value  |      Description                                                                                       |
|:---------------------:|:---------------:|:------------------------------------------------------------------------------------------------------:|
|`--devices`            | false           | To print all available devices                                                                         |
|`--model`              | small           | Select model list. refer [here](https://github.com/openai/whisper#available-models-and-languages)      |
|`--task`               | transcribe      | Choose between to transcribe  or to translate the audio to English                                     |
|`--device_index`       | 2               | Choose the output device to listen to and transcribe the audio from this device                        |
|`--channel`            | 2               | Number of channels of the output device                                                                |
|`--rate`               | 44100           | Sampling rate of the output device                                                                     |
|`--audioseconds`       | 5               | Length of audio files to record                                                                        |
|`--audiocounts`        | 5               | Number of audio files to save into path                                                                |
|`--output_dir`         | "audio"         | Output directory to save audio files recorded by audioWhisper.py                                       |

## Disclaimer
The performance of the transcribing and translating the audio are depending on your machine's performance. 

## Performance Test on Ryzen 5 5600G with NVIDIA RTX3060
The translated audio is not perfect but it can still translate the point of the talk from audio. Video demo for this app is on [youtube](https://youtu.be/8n_KKEST1gg).


## License
The code and the model weights of Whisper are released under the MIT License. See their [repo](https://github.com/openai/whisper#license) for more information.
The code of this repo is under MIT License. See [LICENSE](LICENSE) for further details.


