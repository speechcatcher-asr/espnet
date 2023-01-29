import kaldiio
import numpy as np
from io import BytesIO
import soundfile

import os 
import ffmpeg

def soundfile_write_workaround(owavpath, wave, samplerate):
    basepath, audio_format = os.path.splitext(owavpath)
    if audio_format == 'flac':
        #workaround for buggy soundfile flac output

        wav_filename = basepath + ".wav"
        flac_filename = basepath + ".flac"

        soundfile.write(wav_filename, wave, samplerate=rate)
        ffmpeg.input(wav_filename).output(flac_filename, acodec='flac').run(overwrite_output=True)
        os.remove(wav_filename)
    else:
        soundfile.write(owavpath, wave, samplerate=rate)

audio_format = 'flac'
line = '17141c1dbff79d6cefde_199d94e1149dd49cb852 ffmpeg -i "https://speechcatcher.net/cache/podcasts/de/1668853163_77e8fb38.mp3" -acodec pcm_s16le -ar 16000 -ac 1 -f wav - |'

uttid, wavpath = line.strip().split(None, 1)

with kaldiio.open_like_kaldi(wavpath, "rb") as f:
    with BytesIO(f.read()) as g:
        wave, rate = soundfile.read(g, dtype=np.int16)

assert(wave.ndim == 1)

owavpath =  f"{uttid}.{audio_format}"

soundfile_write_workaround(owavpath, wave, samplerate=rate)
