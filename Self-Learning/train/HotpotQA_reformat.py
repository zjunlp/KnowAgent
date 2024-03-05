import json
import random
import copy
import argparse

parser = argparse.ArgumentParser(description='Parsing the file_path to reformat and to save the data.')
parser.add_argument("--input_path", type=str, help="input data path")
parser.add_argument("--output_path", type=str, help="output data path")
args = parser.parse_args()

systemprompt = """Your task is to answer a question using a specific graph-based method. You must navigate from the "Start" node to the "Finish" node by following the paths outlined in the graph. The correct path is a series of actions that will lead you to the answer.
The decision graph is constructed upon a set of principles known as "Action Knowledge", outlined as follows:
   Start:(Search, Retrieve)
   Retrieve:(Retrieve, Search, Lookup, Finish)
   Search:(Search, Retrieve, Lookup, Finish)
   Lookup:(Lookup, Search, Retrieve, Finish)
   Finish:()
Here's how to interpret the graph's Action Knowledge:
From "Start", you can initiate with either a "Search" or a "Retrieve" action.
At the "Retrieve" node, you have the options to persist with "Retrieve", shift to "Search", experiment with "Lookup", or advance to "Finish".
At the "Search" node, you can repeat "Search", switch to "Retrieve" or "Lookup", or proceed to "Finish".
At the "Lookup" node, you have the choice to keep using "Lookup", switch to "Search" or "Retrieve", or complete the task by going to "Finish".
The "Finish" node is the final action where you provide the answer and the task is completed.
Each node action is defined as follows:
(1) Retrieve[entity]: Retrieve the exact entity on Wikipedia and return the first paragraph if it exists. If not, return some similar entities for searching. 
(2) Search[topic]:  Use Bing Search to find relevant information on a specified topic, question, or term.
(3) Lookup[keyword]: Return the next sentence that contains the keyword in the last passage successfully found by Search or Retrieve.  
(4) Finish[answer]: Return the answer and conclude the task.  
As you solve the question using the above graph structure, interleave ActionPath, Thought, Action, and Observation steps. ActionPath documents the sequence of nodes you have traversed within the graph. Thought analyzes the current node to reveal potential next steps and reasons for the current situation. 
You may take as many steps as necessary.
Here are some examples:
Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
ActionPath 1: Start
Thought 1: From "Start", the adjacent nodes are "Search" and "Retrieve". The subsequent action should only be chosen from these options. The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to retrieve Milhouse and find who it is named after.
Action 1: Retrieve[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
ActionPath 2: Start->Retrieve[Milhouse]
Thought 2: After "Retrieve", the only possible actions are "Retrieve", "Search", "Lookup" or "Finish". The next step should only be selected from among these choices. The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2:  Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous.
ActionPath 3: Start->Retrieve[Milhouse]->Lookup[named after]
Thought 3: From "Lookup", the available actions are "Lookup", "Retrieve", "Search", or "Finish." Having found that Milhouse was named after U.S. president Richard Nixon, the answer to the question is now clear. No further actions are needed as the necessary information has been obtained.
Action 3: Finish[Richard Nixon]

Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?
ActionPath 1: Start
Thought 1: From "Start", the adjacent nodes are "Search" and "Retrieve". To determine if Pavel Urysohn and Leonid Levin were known for the same type of work, it's essential to understand their professional backgrounds and contributions. A "Search" action seems appropriate to gather this information about each individual.
Action 1: Search[Pavel Urysohn]
Observation 1: Pavel Samuilovich Urysohn (February 3, 1898 August 17, 1924) was a Soviet mathematician who is best known for his contributions in dimension theory.
ActionPath 2: Start->Search[Pavel Urysohn]
Thought 2: After "Search", the only possible actions are "Search", "Retrieve", "Lookup" or "Finish". Pavel Urysohn is a mathematician. I need to search Leonid Levin next and find his type of work. 
Action 2: Search[Leonid Levin]
Observation 2: Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist.
ActionPath 3: Start->Search[Pavel Urysohn]->Search[Leonid Levin]
Thought 3: After "Search", the only possible actions are "Search", "Retrieve", "Lookup" or "Finish". Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work. No further actions are needed as the necessary information has been obtained.
Action 3: Finish[yes]

(END OF EXAMPLES)"""

def prompt_retrieve(prompt: str) -> str:
    end_of_examples_index = prompt.find("(END OF EXAMPLES)")
    if end_of_examples_index != -1:
        prompt = prompt[end_of_examples_index + len("(END OF EXAMPLES)") + 1:]
    else:
        prompt = prompt

    prompt_index = prompt.find("Question: ")
    
    if prompt_index != -1:
        remaining_content = prompt[prompt_index:].split('\n', 1)[1]
    else:
        remaining_content = ""

    return remaining_content

output_path = args.output_path
if output_path[-1]!='/':
    output_path+='/'
save_path = f"{output_path}HotpotQA_data_knowagent.json" 

file_path = args.input_path
data_actionpath = []
all_lines = []   

with open(file_path, "r") as f:
    lines = f.readlines()
    all_lines.extend(lines)  

print("Total number of lines:", len(all_lines))

random.shuffle(all_lines)

for line in all_lines:
    item = json.loads(line)
    if not item['correct']:
        continue
    question = item['question']
    prompt = item["prompt"]
    if 'Invalid Action' in prompt:
        continue
    data = prompt_retrieve(prompt)

    d_actionpath = {"input": systemprompt + f"\nQuestion: {question}\n", "output": ""}
    d_actionpath["output"] = data
    data_actionpath.append(copy.copy(d_actionpath))
        
print("The length of the json",len(data_actionpath))

with open(save_path, "w") as f_actionpath:
    json.dump(data_actionpath, f_actionpath, indent=4)

