import json
import re
import argparse


parser = argparse.ArgumentParser(description="The process of Knowledgeable Self_Learning.")
parser.add_argument("--task", type=str, required=True, choices=['HotpotQA', 'ALFWorld'], help="The name of the task to perform. Accepts 'HotpotQA' or 'ALFWorld'.")
parser.add_argument("--input_path1", type=str, required=True, help="File path to the first input JSONL file that needs to be processed.")
parser.add_argument("--input_path2", type=str, required=True, help="File path to the second input JSONL file that needs to be processed.")
parser.add_argument("--output_path", type=str, required=True, help="Output file path where the merged JSONL file will be saved.")
args = parser.parse_args()

input_path1 =  args.input_path1
input_path2 =  args.input_path2
output_path = args.output_path
if output_path[-1]!='/':
    output_path+='/'
output_path = output_path + f"{args.task}_processed_knowagent.jsonl"
def process_prompt_for_hotpotqa(prompt):
    lines = prompt.strip().split('\n')
    if len(lines) < 2:
        return ""
    second_to_last_line = lines[-4]
    path = second_to_last_line.split(': ')[-1] if ': ' in second_to_last_line else ""
    cleaned_prompt = re.sub(r'^Start->', '', path)
    cleaned_prompt = re.sub(r'->Finish.*', '', cleaned_prompt)
    cleaned_prompt = re.sub(r'\[.*?\]', '', cleaned_prompt)
    actions = cleaned_prompt.strip().split('->')
    actions = [action for action in actions if action]
    return actions

def process_prompt_for_alfworld(prompt):
    lines = prompt.strip().split('\n')
    count = 0  
    for line in lines:  
        if "> " in line:  
            count += 1 
    return count  

# Read and filter jsonl file, returning correct entries and a mapping of questions to answers
def read_jsonl_for_hotpotqa(file_path):
    correct_entries = []
    question_to_answer = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line.strip())
            if entry['correct'] == True and 'answer' in entry and 'Invalid Action' not in entry['prompt'] and 'Search error' not in entry['prompt']:
                correct_entries.append(entry)
                question_to_answer[entry['question']] = entry
    return correct_entries, question_to_answer

def read_jsonl_for_alfworld(file_path):
    correct_entries = []
    question_to_answer = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line.strip())
            if entry['result'] == True:
                correct_entries.append(entry)
                question_to_answer[entry['name']] = entry
    return correct_entries, question_to_answer

# Read the files
if args.task == "HotpotQA":
    correct_entries1, question_to_answer1 = read_jsonl_for_hotpotqa(input_path1)
    correct_entries2, question_to_answer2 = read_jsonl_for_hotpotqa(input_path2)
elif args.task == "ALFWorld":
    correct_entries1, question_to_answer1 = read_jsonl_for_alfworld(input_path1)
    correct_entries2, question_to_answer2 = read_jsonl_for_alfworld(input_path2)

# Count
number_of_correct_items_1 = len(correct_entries1)
number_of_correct_items_2 = len(correct_entries2)
number_of_replaced_items = 0
number_of_none_replaced_items = 0

# Merge the lists, keeping the entry with the shortest action path from the second to last line of the prompt

if args.task == "HotpotQA":
    merged_entries = {entry['question']: entry for entry in correct_entries1}
    for entry in correct_entries2:
        question = entry['question']
        if question in merged_entries:
            existing_entry = merged_entries[question]
            existing_actionpath = process_prompt_for_hotpotqa(existing_entry['prompt'])
            print(existing_actionpath)
            new_actionpath = process_prompt_for_hotpotqa(entry['prompt'])
            print(new_actionpath)

            if len(new_actionpath) <= len(existing_actionpath):
                merged_entries[question] = entry
                print(f"Replaced entry for question: {question}")
                number_of_replaced_items += 1
            else:
                print("Do not Replace")
                number_of_none_replaced_items += 1
        else:
            merged_entries[question] = entry
elif args.task == "ALFWorld":
    merged_entries = {entry['name']: entry for entry in correct_entries1}
    for entry in correct_entries2:
        question = entry['name']
        if question in merged_entries:
            existing_entry = merged_entries[question]
            existing_number = process_prompt_for_alfworld(existing_entry['traj'])
            new_number = process_prompt_for_alfworld(entry['traj'])
            if new_number <= existing_number:
                merged_entries[question] = entry
                number_of_replaced_items += 1
            else:
                number_of_none_replaced_items += 1
        else:
            merged_entries[question] = entry
            
# Count merged items
number_of_merged_items = len(merged_entries)

# Write results to new jsonl file
with open(output_path, 'w', encoding='utf-8') as output_file:
    for entry in merged_entries.values():
        output_file.write(json.dumps(entry) + '\n')

# Output statistics
print(f"Completed. The  dmerged and filtered data has been saved to {output_path}")
print(f"Number of correct items in the first file: {number_of_correct_items_1}")
print(f"Number of correct items in the second file: {number_of_correct_items_2}")
print(f"Number of replaced items due to shorter action paths: {number_of_replaced_items}")
print(f"Number of none replaced items due to shorter action paths: {number_of_none_replaced_items}")
print(f"Total number of items after merging: {number_of_merged_items}")
