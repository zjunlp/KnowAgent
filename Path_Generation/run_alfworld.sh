#train
python alfworld_run/run_alfworld.py \
    --llm_name llama-2-13b \
    --mode train \
    --output_path ../Self-Learning/trajs/


#test
python alfworld_run/run_alfworld.py \
    --llm_name llama-2-13b \
    --mode test \
    --output_path output/
