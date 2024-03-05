# train
python run_hotpotqa.py \
    --llm_name llama-2-13b \
    --max_context_len 4000 \
    --mode train \
    --output_path ../Self-Learning/trajs/


# test
python run_hotpotqa.py \
    --llm_name llama-2-13b \
    --max_context_len 4000 \
    --mode test \
    --output_path output/