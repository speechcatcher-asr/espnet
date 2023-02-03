DIR="data/dev"
utils/utt2spk_to_spk2utt.pl $DIR/utt2spk > $DIR/spk2utt

mv $DIR/utt2dur $DIR/utt2dur.my

FILES=("text" "utt2spk" "spk2utt" "segments" "wav.scp")
for file in "${FILES[@]}"
do
  sort -k1 "$DIR/$file" > "$DIR/${file}.sorted"
  mv "$DIR/$file" "$DIR/${file}.unsorted"
  mv "$DIR/${file}.sorted" "$DIR/$file"
done

bash utils/validate_data_dir.sh --no-feats $DIR
