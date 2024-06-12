import wave
import random
import os
import struct
import math

random_file = "data/" + random.choice(os.listdir("data/"))

with wave.open(random_file, 'rb') as f:
    print(f.getparams())
    print(f.readframes(10))
    raw_data = f.readframes(f.getnframes())

# Iterate over the raw data and find the minimum and maximum values
min_value = float('inf')
max_value = -float('inf')

for i in range(0, len(raw_data), 2):
    frame = raw_data[i:i+2]
    value = struct.unpack('<h', frame)[0]
    min_value = min(min_value, value)
    max_value = max(max_value, value)

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
