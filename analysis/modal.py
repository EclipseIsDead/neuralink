import os
import wave
import struct
import numpy as np
import diptest

def read_wav_data(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        sample_width = wav_file.getsampwidth()
        raw_data = wav_file.readframes(wav_file.getnframes())
        data = np.array([struct.unpack('<h', raw_data[i:i+sample_width])[0] for i in range(0, len(raw_data), sample_width)])
    return data

data_folder = 'data'
wav_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.wav')]

all_data = []
for wav_file in wav_files:
    data = read_wav_data(wav_file)
    all_data.extend(data)

all_data = np.array(all_data)

dip_statistic, dip_p_value = diptest.diptest(all_data)
print(f"\nDip Test Statistic: {dip_statistic:.4f}")
print(f"p-value: {dip_p_value:.4e}")
if dip_p_value > 0.05:
    print("The data is unimodal at the 5% significance level.")
else:
    print("The data is not unimodal (possibly bimodal or multimodal) at the 5% significance level.")
