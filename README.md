# neuralink
Overview of the Neuralink Data Compression challenge.

## Commands

To curl install the zip file, run the following commands:
```
chmod +x data.sh
./data.sh
```

It is expected the user unzip the file however they see fit, into a folder at root called "data". This should yield something similar to the following relative path:
```
data/0ab237b7-fb12-4687-afed-8d1e2070d621.wav
```

## Data

Upon running `python3 analysis/sample.py`, we see that `_wave_params(nchannels=1, sampwidth=2, framerate=19531, nframes=98991, comptype='NONE', compname='not compressed')`.

1.  nframes is not consistent, and sometimes when divided by framerate is 5.07 seconds so not exactly 5 seconds. Sample rate is 19531, not 20000 as the challenge mentioned. This is a common theme in this dataset!
2. The challenge states 1024 electrodes @ 20kHz, 10b resolution but we are given 732 files of 1 channel @ ~19.5kHz, 16b resolution?
3. Followup from the previous but it's not lower bound -512, but instead -32768 so scaled from 10b to 16b by steps of 64.

### Noise analysis

We have established this data is sketchy at best. Let's move on to visualizing the data and observe what we can.

1. From `python3 analysis/modal.py` we can diptest to see the data is not at all unimodal (possibly bimodal or multimodal). This might indicate an external noise source consistently present at recording time?

## Approach
Lets rip out the last 6 bits of each sample for an easy 1.6x compression base.
