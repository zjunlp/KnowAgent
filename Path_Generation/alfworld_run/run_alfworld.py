import os
import json
import openai
import yaml
import alfworld
import alfworld.agents.environment
import sys
from langchain import PromptTemplate, OpenAI, LLMChain
import tiktoken
from prompts.taskprompt import alf_put_prompt,alf_clean_prompt,alf_cool_prompt,alf_examine_prompt,alf_heat_prompt,alf_puttwo_prompt
token_enc = tiktoken.get_encoding("cl100k_base")
import argparse
import warnings
warnings.filterwarnings('ignore')

OPENAI_API_KEY = "sk-xxxxxxx"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

parser = argparse.ArgumentParser(description='Run the ALFWORLD task with a specified LLM model.')
parser.add_argument('--llm_name', type=str, required=True, help='The name of the LLM model to use for the task.')
parser.add_argument("--mode",type=str, required=True, help="train or test",default="test")
parser.add_argument("--output_path",type=str, required=True, help="output path")
args = parser.parse_args()

model_name = args.llm_name
mode = args.mode
output_path = args.output_path
if output_path[-1]!='/':
    output_path+='/'
print(f"LLM's name: {model_name}\n")


class langchain_fastchat_llm:
    def __init__(self, llm_name):
        openai.api_key = "EMPTY"  # Not supported yet
        self.prompt_temp = PromptTemplate(
            input_variables=["prompt"], template="{prompt}"
        )
        self.llm_name = llm_name
        
    def run(self, prompt, temperature=0.9, stop=['\n'], max_tokens=128):
        openai.api_base = "http://localhost:8000/v1"
        # llm = OpenAI(model=self.llm_name, temperature=temperature, stop=stop, max_tokens=max_tokens)
        llm  = OpenAI(
            model=self.llm_name, 
            temperature=temperature, 
            top_p=0.75, 
            top_k=40, 
            num_beams=4, 
            stop=stop,
            max_tokens=max_tokens
        )
        chain = LLMChain(llm=llm, prompt=self.prompt_temp)
        return chain.run(prompt)

def llm(prompt: str, model: str):
    try:
        cur_try = 0
        while cur_try < 5:
            llm_instance = langchain_fastchat_llm(llm_name=model).run
            text = llm_instance(prompt=prompt)
            # dumb way to do this
            if len(text.strip()) >= 5:
                return text
            cur_try += 1
        return ""
    except Exception as e:
        print(e)

def alfworld_run(prompt, to_print=True, ob=''):
    init_prompt = prompt + ob + '\n>'
    prompt = ''
    traj = ""
    if to_print:
        print(ob)
        sys.stdout.flush()
    try:    
        action = llm(init_prompt + prompt,model_name)
        action = action.strip('\n').strip().replace('\n', '')
        observation, reward, done, info = env.step([action])
        observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]
        print(f'Act {0}: {action}')
        traj += f'> {action}\n'
        prompt += f' {action}\n>'

        for i in range(1, 50):
            if (len(token_enc.encode(init_prompt + prompt)) > 4000):
                return reward, traj
            action = llm(init_prompt + prompt,model_name)
            action = action.strip('\n').strip().replace('\n', '')
            observation, reward, done, info = env.step([action])
            observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]
            if action.startswith('ActionPath:'):
                observation = ''
                if to_print:
                    print(f'Act {i}: {action}')
                    traj += f'> {action}\n'
                    sys.stdout.flush()
                prompt += f' {action}\n>'
            elif action.startswith('Think:'):
                observation = ''
                if to_print:
                    print(f'Act {i}: {action}')
                    traj += f'> {action}\n'
                    sys.stdout.flush()
                prompt += f' {action}\n>'
            else:
                if to_print:
                    print(f'Act {i}: {action}\nObs {i}: {observation}')
                    traj += f'> {action}\n{observation}\n'
                    sys.stdout.flush()
                prompt += f' {action}\n{observation}\n>'
            if done:
                return reward, traj
        return 0, traj
    except Exception as e:
        print(f"Error: {e}")
        return 0, traj

with open('alfworld_run/base_config.yaml') as reader:
    config = yaml.safe_load(reader)

prefixes = {
    'pick_and_place': 'put',
    'pick_clean_then_place': 'clean',
    'pick_heat_then_place': 'heat',
    'pick_cool_then_place': 'cool',
    'look_at_obj': 'examine',
    'pick_two_obj': 'puttwo'
}


game_num = 0
split = ""
if mode == "train":
    game_num = 510
    split = "train"
elif mode == "test":
    game_num = 134
    split = "eval_out_of_distribution"
    

env = getattr(alfworld.agents.environment, config["env"]["type"])(config, train_eval=split)
env = env.init_env(batch_size=1)

def process_ob(ob):
    if ob.startswith('You arrive at loc '):
        ob = ob[ob.find('. ')+2:]
    return ob


prompts = {
    'put':alf_put_prompt,
    'clean':alf_clean_prompt,
    'heat':alf_heat_prompt,
    'cool':alf_cool_prompt,
    'examine':alf_examine_prompt,
    'puttwo': alf_puttwo_prompt
}

cnts = [0] * 6
rs = [0] * 6

results = []

for _ in range(game_num):
    ob, info = env.reset()
    ob = '\n'.join(ob[0].split('\n\n')[1:])
    name = '/'.join(info['extra.gamefile'][0].split('/')[-3:-1])
    print(name)
    for i, (k, v) in enumerate(prefixes.items()):
        if name.startswith(k):
            print(k, v)
            prompt = prompts[v]
            r, traj = alfworld_run(prompt, ob=ob)
            rs[i] += r
            cnts[i] += 1
            result_entry = {"name": name, "result": r, "traj": ob+'\n'+traj}
            results.append(result_entry)
            break
    print(_+1, 'r', r, 'rs', rs, 'cnts', cnts, 'sum(rs)/sum(cnts)', sum(rs) / sum(cnts))
    print('------------\n')

# Save results to a JSONL file
with open(f'{output_path}{model_name}_knowagent_results.jsonl', 'w') as jsonl_file:
    for result_entry in results:
        jsonl_file.write(json.dumps(result_entry) + '\n')
