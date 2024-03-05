import json
import argparse
from alfworld_prompts.taskprompt import alf_put_prompt,alf_clean_prompt,alf_cool_prompt,alf_examine_prompt,alf_heat_prompt,alf_puttwo_prompt

import json

task_to_prompt = {
    'pick_and_place': alf_put_prompt,
    'pick_clean_then_place': alf_clean_prompt,
    'pick_heat_then_place': alf_heat_prompt,
    'pick_cool_then_place': alf_cool_prompt,
    'look_at_obj': alf_examine_prompt,
    'pick_two_obj': alf_puttwo_prompt
}

parser = argparse.ArgumentParser(description='Parsing the file_path to reformat and to save the data.')
parser.add_argument("--input_path", type=str, help="input data path")
parser.add_argument("--output_path", type=str, help="output data path")
args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
if output_path[-1]!='/':
    output_path+='/'
output_path = f"{output_path}ALFWorld_data_knowagent.json" 

processed_data = []

with open(input_path, 'r') as input_file:
    for line in input_file:
        data = json.loads(line.strip())
        if data.get('result') == True:
            task_name = data.get('name', '')
            task_type = None
            for key in task_to_prompt.keys():
                if key in task_name:
                    task_type = key
                    break
            
            if task_type is None:
                continue
  
            prompt = task_to_prompt.get(task_type)
            
            traj = data.get('traj')
            
            act_0_index = traj.find('> ') 
            if act_0_index == -1:
                continue
            
            input_part = traj[:act_0_index].rstrip(' ')  
            output_part = traj[act_0_index:]  
            
            new_data = {
                'input': prompt + " " + input_part,
                'output': output_part
            }
            
            processed_data.append(new_data)

with open(output_path, 'w') as output_file:
    json.dump(processed_data, output_file, indent=4)
print(f"The length of the file is: {len(processed_data)}")
print(f"Processed data has been saved to {output_path}")