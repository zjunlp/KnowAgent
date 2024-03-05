
for iter in 2
do
let prev_iter=iter-1
echo "####################"
echo "Training iteration $iter"
echo "Training pre-iteration $prev_iter"
echo "####################"

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 deepspeed train/train_lora_iter.py \
    --model_name_or_path  llama-2-13b-chat \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --data_path train/trajs/train_answer_v3_500_D0_D1.json \
    --output_dir models/Hotpotqa/M$iter \
    --lora_weight_path models/Hotpotqa/M$prev_iter \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 10000 \
    --save_total_limit 1 \
    --learning_rate 1e-4 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fp16 True \
    --model_max_length 4096 \
    --gradient_checkpointing True \
    --q_lora False \
    --deepspeed /data/zyq/FastChat/playground/deepspeed_config_s3.json \
    --resume_from_checkpoint False 
if [ $? -ne 0 ]; then
    echo "Error occurred during training iteration $inter"
    break  
fi
done