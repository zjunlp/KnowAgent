"""
 Copyright (c) 2023, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: Apache License 2.0
 For full license text, see the LICENSE file in the repo root or https://www.apache.org/licenses/LICENSE-2.0
"""

KNOWAGENT_EXAMPLE = """Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
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
"""




