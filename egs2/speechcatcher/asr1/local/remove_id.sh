#!/bin/bash

#1668949167_b86a1737.mp3
REMID="c502615d2bcea6efe696_7eedf56974d1a1e27586"

#1668982352_6bc0122c.mp3
REMID="97a99c77aa1d5970b8b3_f8350df2b854023057af"

for file in data/train/segments data/train/wav.scp data/train/text data/train/utt2spk; do
    sed -i "/$REMID/d" $file
done
