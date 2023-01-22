#!/bin/bash

#1668949167_b86a1737.mp3
REMID="c502615d2bcea6efe696_7eedf56974d1a1e27586"

for file in data/train/segments data/train/wav.scp data/train/text data/train/utt2spk; do
    sed -i "/$REMID/d" $file
done
