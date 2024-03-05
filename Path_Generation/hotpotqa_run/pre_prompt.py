"""
 Copyright (c) 2023, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: Apache License 2.0
 For full license text, see the LICENSE file in the repo root or https://www.apache.org/licenses/LICENSE-2.0
"""

from langchain.prompts import PromptTemplate


KNOWAGENT_INSTRUCTION = """Your task is to answer a question using a specific graph-based method. You must navigate from the "Start" node to the "Finish" node by following the paths outlined in the graph. The correct path is a series of actions that will lead you to the answer.
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
{examples}
(END OF EXAMPLES)
Question: {question}{scratchpad}"""

knowagent_prompt = PromptTemplate(
                        input_variables=["examples","question", "scratchpad"],
                        template = KNOWAGENT_INSTRUCTION,
                        )




