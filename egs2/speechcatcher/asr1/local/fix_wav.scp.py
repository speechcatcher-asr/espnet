# Open the segments file and create a set of recordids
segments_file = open("data/train/segments", "r")
segments_recordids = set()
for line in segments_file:
    segments_recordids.add(line.split()[1])
segments_file.close()

# Open the wav.scp file and create a new wav.scp file without the recordids that are not in the segments file
wav_file = open("data/train/wav.scp", "r")
new_wav_file = open("data/train/new_wav.scp", "w")
for line in wav_file:
    recordid = line.split()[0]
    if recordid in segments_recordids:
        new_wav_file.write(line)
wav_file.close()
new_wav_file.close()
