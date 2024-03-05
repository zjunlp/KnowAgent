
from alfworld_prompts.example import knowagent_put_0,knowagent_put_1,knowagent_examine_0,knowagent_examine_1,knowagent_clean_1,knowagent_clean_2
from alfworld_prompts.example import knowagent_heat_0,knowagent_heat_1,knowagent_cool_1,knowagent_puttwo_0,knowagent_puttwo_1,knowagent_cool_2


# List of imported variables
imported_strings = [
    knowagent_put_0, knowagent_put_1, knowagent_examine_0, knowagent_examine_1,
    knowagent_clean_2, knowagent_clean_1, knowagent_heat_0, knowagent_heat_1,
    knowagent_cool_2, knowagent_cool_1, knowagent_puttwo_0, knowagent_puttwo_1
]

# Process each string to replace consecutive \n\n with \n
processed_strings = [s.replace("\n\n", "\n") for s in imported_strings]
processed_strings = [s.replace("\n\n\n", "\n") for s in processed_strings]

knowagent_put_0, knowagent_put_1, knowagent_examine_0, knowagent_examine_1, knowagent_clean_2, knowagent_clean_1, knowagent_heat_0, knowagent_heat_1, knowagent_cool_2, knowagent_cool_1, knowagent_puttwo_0, knowagent_puttwo_1 = processed_strings


alf_put_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge".The guidelines are:
Goto(receptacle) -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
Take(object, from: receptacle) -> Goto(receptacle)
[Goto(receptacle), Take(object, from: receptacle)] -> Put(object, in/on: receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
Before you go to the new receptacle where the object is to be placed, you should take it. 
Putting an object in or on a receptacle can follow either going to the location of the receptacle or after taking an object with you. 

The actions are as follows:
1) go to receptacle 
2) take object from receptacle 
3) put object in/on receptacle 
4) open receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_put_0}
{knowagent_put_1}
Here is the task.
"""

alf_examine_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge". The guidelines are:
[Goto(receptacle)] -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
[Goto(receptacle)] -> Use(receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
To use an receptacle, you must go to the place where it is located.

The actions are as follows:
1) go to receptacle 
2) take object from receptacle
3) use receptacle 
4) open receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_examine_0}
{knowagent_examine_1}
Here is the task.
"""

alf_clean_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge". The guidelines are:
[Goto(receptacle)] -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
[Goto(receptacle), Take(object, from: receptacle)] -> Put(object, in/on: receptacle)
[Put(object, from: receptacle)] -> Clean(object, with: receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
Putting an object in or on a receptacle can follow either going to the location of the receptacle or after taking an object with you. 
To clean an object using a receptacle, the object must first be placed in or on that receptacle.

The actions are as follows:
1) go to receptacle 
2) take object from receptacle
3) open receptacle
4) put object in/on receptacle 
5) clean object with receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_clean_2}
{knowagent_clean_1}
Here is the task.
"""

alf_heat_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge". The guidelines are:
[Goto(receptacle)] -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
[Goto(receptacle), Take(object, from: receptacle)] -> Put(object, in/on: receptacle)
[Put(object, in/on: receptacle)] -> Heat(object, with: receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
Putting an object in or on a receptacle can follow either going to the location of the receptacle or after taking an object with you. 
To heat an object using a receptacle, the object must first be placed in or on that receptacle.

The actions are as follows:
1) go to receptacle 
2) take object from receptacle
3) open receptacle
4) put object in/on receptacle 
5) heat object with receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_heat_0}
{knowagent_heat_1}
Here is the task.
"""

alf_cool_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge". The guidelines are:
[Goto(receptacle)] -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
[Goto(receptacle), Take(object, from: receptacle)] -> Put(object, in/on: receptacle)
[Put(object, in/on: receptacle)] -> Cool(object, with: receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
Putting an object in or on a receptacle can follow either going to the location of the receptacle or after taking an object with you. 
To cool an object using a receptacle, the object must first be placed in or on that receptacle.

The actions are as follows:
1) go to receptacle 
2) take object from receptacle
3) open receptacle
4) put object in/on receptacle 
5) cool object with receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_cool_2}
{knowagent_cool_1}
Here is the task.
"""

alf_puttwo_prompt=f"""Interact with a household to solve a task by following the structured "Action Knowledge". The guidelines are:
Goto(receptacle) -> Open(receptacle)
[Goto(receptacle), Open(receptacle)] -> Take(object, from: receptacle)
Take(object, from: receptacle) -> Goto(receptacle)
[Goto(receptacle), Take(object, from: receptacle)] -> Put(object, in/on: receptacle)

Here's how to interpret the Action Knowledge:
Before you open a receptacle, you must first go to it. This rule applies when the receptacle is closed.
To take an object from a receptacle, you either need to be at the receptacle's location, or if it's closed, you need to open it first. 
Before you go to the new receptacle where the object is to be placed, you should take it. 
Putting an object in or on a receptacle can follow either going to the location of the receptacle or after taking an object with you. 
Ensure the first object is placed before proceeding to deposit the second object.

The actions are as follows:
1) go to receptacle 
2) take object from receptacle 
3) put object in/on receptacle 
4) open receptacle

As you tackle the question with Action Knowledge, utilize both the ActionPath and Think steps. ActionPath records the series of actions you've taken, and the Think step understands the current situation and guides your next moves.

Here are two examples.
{knowagent_puttwo_0}
{knowagent_puttwo_1}
Here is the task.
"""