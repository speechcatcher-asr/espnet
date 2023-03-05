#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

train_set="train"
valid_set="dev"
test_sets="test"

asr_config=conf/train_asr_streaming_transformer_size_l.yaml
inference_config=conf/decode_asr_streaming.yaml
bpe_train_text=dump/raw/train/text #data/train/text.raw
lm_config=conf/train_lm.yaml
# was true
use_lm=false
use_wordlm=false

# speed perturbation related
# (train_set will be "${train_set}_sp" if speed_perturb_factors is specified)
speed_perturb_factors="" #"0.9 1.0 1.1"

./asr.sh                                               \
    --use_streaming true                                \
    --lang de                                          \
    --ngpu 4                                          \
    --nj 24                                            \
    --feats_type raw                                   \
    --audio_format flac                                 \
    --max_wav_duration 120                             \
    --token_type bpe                                  \
    --nbpe 1024                                        \
    --bpe_train_text ${bpe_train_text}        \
    --use_lm ${use_lm}                                 \
    --use_word_lm ${use_wordlm}                        \
    --lm_config "${lm_config}"                         \
    --asr_config "${asr_config}"                       \
    --inference_config "${inference_config}"           \
    --train_set "${train_set}"                         \
    --valid_set "${valid_set}"                         \
    --test_sets "${test_sets}"                         \
    --speed_perturb_factors "${speed_perturb_factors}" \
    --lm_train_text "data/${train_set}/text" "$@" \
    --hf_repo speechcatcher/speechcatcher_german_espnet_streaming_transformer_13k_train_size_l_raw_de_bpe1024 \
    --skip_upload_hf false \
    --stage 11
