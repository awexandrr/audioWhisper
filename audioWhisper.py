
import sounddevice as sd
import whisper
from scipy.io import wavfile
import numpy as np
from datetime import datetime as time
import argparse
import os

parser = argparse.ArgumentParser(description="parameters for audioWhisper.py")
parser.add_argument('--devices', default='False', type=str, help='print all available devices id')
parser.add_argument('--model', type=str, choices=['tiny','tiny.en', 'small', 'small.en', 'medium', 'medium.en', 'large'], default='small', help='model to be use for generating audio transcribe')
parser.add_argument('--task', type=str, choices=['transcribe', 'translate'], default='transcribe', help='task for the model whether to only transcribe the audio or translate the audio to english')
parser.add_argument('--device_index', default= 2, type=int, help='the id of the device ')
parser.add_argument('--channel', default= 2, type=int, help='number of channels for the device')
parser.add_argument('--rate', default= 44100, type=int, help="polling rate of the output device")
parser.add_argument('--audioseconds', default=5, type=int, help='the length of the audio for recording')
parser.add_argument('--audiocounts', default=5, type=int, help='counts to save audio files in audio folder')
parser.add_argument('--output_dir', default="audio", type=str, help='output directory for audio files recorded')
args = parser.parse_args()

def main():
    model: str=args.model
    task: str=args.task
    rate: int=args.rate
    channel: int=args.channel
    device_index: int=args.device_index
    seconds: int=args.audioseconds
    audio_counts: int=args.audiocounts
    output_dir: str=args.output_dir
    language: str=None

    os.makedirs(output_dir, exist_ok=True)
    if model.endswith('.en'):
        language = 'english'
        if model == 'large.en':
            raise ValueError("english model does not have large model, please choose from {tiny.en, small.en, medium.en}")

    audio_model = whisper.load_model(model)

    sd.default.device[0] = device_index
    sd.default.dtype[0] = np.float32

    index = 0

    while True:
        print("recording...")
        recording = sd.rec(frames=rate*seconds, samplerate = rate, channels=channel, dtype=np.float32)
        if index == 0:
            indexPath = audio_counts
        else:
            indexPath = index - 1

        try:
            print("transcribing...")
            prevTime = time.now()
            result = audio_model.transcribe(f"{output_dir}/audio{indexPath}.wav", 
                                            task=task, 
                                            no_speech_threshold=0.6, 
                                            compression_ratio_threshold=2.4,
                                            language=language)

            translatedText = result.get('text')
            print('\n', translatedText)
        except:
            print("no audio track recorded yet")
            
        print(f"time taken to transcribe: {time.now() - prevTime}")
        sd.wait()
        wavfile.write(f"{output_dir}/audio{index}.wav", rate=rate, data=recording)

        index += 1
        if index > audio_counts:
            index = 0

def str2bool(string):
    str2val = {"true": True, "false": False}
    if string.lower() in str2val:
        return str2val[string.lower()]
    else:
        raise ValueError(f"Expected one of {set(str2val.keys())}, got {string}")

if __name__ == '__main__':    
    if str2bool(args.devices) == True:
        print(sd.query_devices()) 
    else:
        main()