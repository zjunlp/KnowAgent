import os
import argparse 
import json
import numpy as np
import pandas as pd
import concurrent
import joblib
from hotpotqa_run.utils import summarize_trial_detailed, log_trial
import hotpotqa_run.utils as utils
from hotpotqa_run.agent_arch import get_agent
from hotpotqa_run.llms import get_llm_backend
import warnings
warnings.filterwarnings('ignore')


parser = argparse.ArgumentParser(description='Parsing the input of agents, llms and llm context length.')
parser.add_argument("--llm_name", type=str, help="Name of the llm", default="gpt-3.5-turbo")
parser.add_argument("--max_context_len", type=int, help="Maximum context length", default=1700)
parser.add_argument("--mode", type=str, required=True, help="train or test",default="test")
parser.add_argument("--output_path", type=str, required=True, help="output path")
args = parser.parse_args()

agent_name = "KnowAgentHotpotQA"
llm_name = args.llm_name
max_context_len = args.max_context_len
mode = args.mode
output_path=args.output_path
if output_path[-1]!='/':
    output_path+='/'
def process_agent_run_step(agent):
    agent.run()

def run_one_complex_level(level="easy"):
    if mode == "train":
        hotpot = json.load(open("hotpotqa_run/data/train/hotpot_train.json"))
        # hotpot=hotpot[:2]
        agent_save_file = f"{output_path}{agent_name}_{llm_name}.jsonl"
        task_instructions = [(row['question'], row['answer']) for row in hotpot]
    elif mode == "test":
        hotpot = joblib.load(f'hotpotqa_run/data/test/{level}.joblib').reset_index(drop = True)
        # hotpot=hotpot[:2]
        agent_save_file = f"{output_path}{level}_{agent_name}_{llm_name}.jsonl"
        task_instructions = [(row['question'], row['answer']) for _, row in hotpot.iterrows()]

    if os.path.exists(agent_save_file):
        sessions = utils.get_all_agent_sessions(agent_save_file)
        completed_tasks = utils.get_non_error_tasks(sessions)
        print(f"{level}:{len(completed_tasks)}")
        task_instructions = [task for task in task_instructions if task not in completed_tasks]
        utils.delete_error(agent_save_file)
    llm = get_llm_backend(llm_name).run
    agent_cls = get_agent(agent_name)
    agents = [agent_cls(ques, ans, llm, max_context_len) for ques, ans in task_instructions]
    for agent in agents:
        process_agent_run_step(agent)
        utils.log_agent(agent, agent_save_file)
    print(f'Finished Trial. Total: {len(agents)}')
    
def main():
    if mode == "train":
        run_one_complex_level()
    elif mode == "test":
        levels = ['easy','medium','hard']
        for level in levels:
            run_one_complex_level(level)
    else:
        print("Mode Error!")

if __name__ == '__main__':
    main()