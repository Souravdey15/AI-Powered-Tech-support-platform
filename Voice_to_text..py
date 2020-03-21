import pyaudio
import wave
import sphinxbase
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path
import os

def recognize(wav_file):
    #BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    #HMDIR = os.path.join(BASE_PATH, "hmm")
    #LMDIR = os.path.join(BASE_PATH, "lm/en-us.lm.bin")
    #DICTD = os.path.join(BASE_PATH, "dict/en_in.dic")
    sound="try1.wav"

    model_path = get_model_path()
    data_path = get_data_path()
    config = DefaultConfig()
    config.set_string('-hmm', "hmm/")
    config.set_string('-lm', 'lm\en-us.lm.bin')
    config.set_string('-dict',  'dict\en_in.dic')
    #decoder = Decoder(config)

    """
    Run speech recognition on a given file.
    """
    speech_rec =  Decoder(config)
    print("Decoder Initialized")
    wav_file = wave.open(wav_file, 'rb')
    print("AudioFile Loaded")
    speech_rec.decode_raw(wav_file)
    print("Audio file decoded")
    result = speech_rec.get_hyp()
    print("Result Ready\n")
    return result

# Run the thing!
if __name__ == '__main__':
    #save_audio(WAVE_OUTPUT_FILENAME)
    result = recognize("audios/try1.wav")
    print("You just said: {0}".format(result[0]))

