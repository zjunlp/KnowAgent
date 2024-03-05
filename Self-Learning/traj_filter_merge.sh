python trajs/traj_merge_and_filter.py \
    --task HotpotQA \
    --input_path1  trajs/datas/KnowAgentHotpotQA_llama-2-13b_D0.jsonl \
    --input_path2  trajs/datas/KnowAgentHotpotQA_llama-2-13b_D1.jsonl \
    --output_path   trajs/datas/ 

python trajs/traj_merge_and_filter.py \
    --task ALFWorld \
    --input_path1  trajs/datas/KnowAgentALFWorld_llama-2-13b_D0.jsonl \
    --input_path2  trajs/datas/KnowAgentALFWorld_llama-2-13b_D1.jsonl \
    --output_path   trajs/datas/ 


