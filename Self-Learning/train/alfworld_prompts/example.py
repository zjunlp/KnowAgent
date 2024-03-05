knowagent_put_0="""You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1. 
Your task is to: find some apple and put it in sidetable.
> Think: To solve the task, I need to first find where the apple is and then take that apple. Next, I'll go to a sidetable and put the apple on it. 

> ActionPath: Start
> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtables (1-3), sidetables (1), countertops (1), sinkbasins (1), garbagecan (1). I can check one by one, starting with fridge 1. 
> go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1.
> go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check the next diningtable. 
> go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check the next diningtable.
> go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1. 
> go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1. 
> go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1 next. 
> go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll check garbagecan 1 next. 
> go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> ActionPath: Start->Goto(garbagecan 1)
> Think: Now I find an apple (3) in garbagecan (1). Next, I need to take it.
> take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)
> Think: Now I get an apple (3). Next, I need to go to the target receptacle: sidetable 1.
> go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)->Goto(sidetable 1)
> Think: Next, I need to put apple 3 in/on sidetable 1.
> put apple 3 in/on sidetable 1
You put the apple 3 in/on the sidetable 1.
"""

knowagent_put_1="""You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a countertop 1, a garbagecan 1, a handtowelholder 2, a handtowelholder 1, a sinkbasin 2, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.
Your task is to: put some spraybottle on toilet.
> Think: To solve the task, I need to first find and then take a sparybottle. Next, put it on toilet. 

> ActionPath: Start
> Think: First I need to find a spraybottle. A spraybottle is more likely to appear in cabinet (1-4), countertop (1), toilet (1), sinkbasin (1-2), garbagecan (1). I can check one by one, starting with cabinet 1.
> go to cabinet 1
On the cabinet 1, you see a cloth 1, a soapbar 1, a soapbottle 1.

> Think: No spraybottle found on cabinet 1, I'll check the next cabinet.
> go to cabinet 2
The cabinet 2 is closed.
> open cabinet 2
You open the cabinet 2. The cabinet 2 is open. In it, you see a candle 1, and a spraybottle 2.

> ActionPath: Start->Goto(cabinet 2)
> Think: Now I find a spraybottle (2) in cabinet (2). Next, I need to take it.
> take spraybottle 2 from cabinet 2
You pick up the spraybottle 2 from the cabinet 2.

> ActionPath: Start->Goto(cabinet 2)->Take(spraybottle 2, from: cabinet 2)
> Think: Now I get a spraybottle (2). Next, I need to go to toilet 1 to continue with the task.
> go to toilet 1
On the toilet 1, you see a soapbottle 2.

> ActionPath: Start->Goto(cabinet 2)->Take(spraybottle 2, from: cabinet 2)->Goto(toilet 1)
> Think: Next, I need to put spraybottle 2 in/on toilet 1.
> put spraybottle 2 in/on toilet 1
You put the spraybottle 2 in/on the toilet 1.
"""

knowagent_examine_0="""You are in the middle of a room. Looking quickly around you, you see a bed 1, a drawer 10, a drawer 9, a drawer 8, a drawer 7, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a dresser 1, a garbagecan 1, a shelf 9, a shelf 8, a shelf 7, a shelf 6, a shelf 5, a shelf 4, a shelf 3, a shelf 2, and a shelf 1.
Your task is to: examine the pen with the desklamp.
> Think: To solve the task, I need to first find and take a pen, then find and use a desklamp. 

> ActionPath: Start
> Think: First I need to find a pen. A pen is more likely to appear in drawer (1-10), shelf (1-9), bed (1), garbagecan (1). I can check one by one, starting with drawer 1.
> go to drawer 1
The drawer 1 is closed.
> open drawer 1
You open the drawer 1. The drawer 1 is open. In it, you see nothing.

> Think: No pen found in drawer 1, I'll check the next drawer. 
> go to drawer 2
The drawer 2 is closed.
> open drawer 2
You open the drawer 2. The drawer 2 is open. In it, you see nothing.

> Think: No pen found in drawer 2, I'll check the next drawer. 
> go to drawer 3
The drawer 3 is closed.
> open drawer 3
You open the drawer 3. The drawer 3 is open. In it, you see nothing.

> Think: No pen found in drawer 3, I'll check the next drawer. 
> go to drawer 4
The drawer 4 is closed.
> open drawer 4
You open the drawer 4. The drawer 4 is open. In it, you see a cd 3, a keychain 1, and a pen 2.

> ActionPath: Start->Goto(drawer 4)
> Think: Now I find a pen (2) in drawer (4). Next, I need to take it.
> take pen 2 from drawer 4
You pick up the pen 2 from the drawer 4.

> ActionPath: Start->Goto(drawer 4)->Take(pen 2, from: drawer 4)
> Think: Now I get a pen (2). Next, I need to find a desklamp to continue the task. A desklamp is more likely to appear in dresser (1), shelf (1-9), bed (1), garbagecan (1), drawer (1-10). I can check one by one, starting with dresser 1. 
> go to dresser 1
On the dresser 1, you see a alarmclock 2, a alarmclock 1, a book 1, a cd 1, a creditcard 1, a desklamp 1, a keychain 2, a pen 3, and a pen 1.

> ActionPath: Start->Goto(drawer 4)->Take(pen 2, from: drawer 4)->Goto(dresser 1)
> Think: Now I find a desklamp (1) on the dresser (1). Next, I need to use it.
> use desklamp 1
You turn on the desklamp 1.
"""

knowagent_examine_1="""You are in the middle of a room. Looking quickly around you, you see a bed 1, a desk 1, a drawer 3, a drawer 2, a drawer 1, a garbagecan 1, a safe 1, a shelf 5, a shelf 4, a shelf 3, a shelf 2, a shelf 1, a sidetable 2, and a sidetable 1.
Your task is to: look at bowl under the desklamp.
> Think: To solve the task, I need to first find and take a bowl, then find and use a desklamp. 

> ActionPath: Start
> Think: First I need to find a bowl. A bowl is more likely to appear in drawer (1-3), desk (1), sidetable (1-2), shelf (1-5), garbagecan (1). I can check one by one, starting with drawer 1.
> go to drawer 1
On the drawer 1, you see nothing.

> Think: No bowl found in drawer 1, I'll check the next drawer. 
> go to drawer 2
The drawer 2 is closed.
> open drawer 2
You open the drawer 2. The drawer 2 is open. In it, you see nothing.

> Think: No bowl found in drawer 2, I'll check the next drawer. 
> go to drawer 3
The drawer 3 is closed.
> open drawer 3
You open the drawer 3. The drawer 3 is open. In it, you see nothing.

> Think: No bowl found in drawer 3, I'll check desk 1. 
> go to desk 1
On the desk 1, you see a alarmclock 2, a book 1, a cellphone 1, a keychain 1, a laptop 2, a laptop 1, and a pen 3.

> Think: No bowl found on desk 1, I'll check sidetable 1. 
> go to sidetable 1
On the sidetable 1, you see a cd 1, a pen 1, and a pencil 1.

> Think: No bowl found on sidetable 1, I'll check shelf 1 next. 
> go to shelf 1
On the shelf 1, you see nothing.

> Think: No bowl found on shelf 1, I'll check the next shelf. 
> go to shelf 2
On the shelf 2, you see a bowl 1.

> ActionPath: Start->Goto(shelf 2)
> Think: Now I find a bowl (1) on the shelf (2). Next, I need to take it.
> take bowl 1 from shelf 2
You pick up the bowl 1 from the shelf 2.

> ActionPath: Start->Goto(shelf 2)->Take(bowl 1, from: shelf 2)
> Think: Now I get a bowl (1). Next, I need to find a desklamp to continue the task. A desklamp is more likely to appear in desk (1), sidetable (1-2), shelf (1-5), bed (1), drawer (1-3). I can check one by one, starting with desk 1.
> go to desk 1
On the desk 1, you see a alarmclock 2, a book 1, a cellphone 1, a keychain 1, a laptop 2, a laptop 1, and a pen 3.

> Think: No desklamp found on desk 1, I'll check the sidetable 1 next. 
> go to sidetable 1
On the sidetable 1, you see a cd 1, a pen 1, and a pencil 1.

> Think: No desklamp found on sidetable 1, I'll check the next sidetable. 
> go to sidetable 2
On the sidetable 2, you see a alarmclock 1, a desklamp 1, and a pen 2.

> ActionPath: Start->Goto(shelf 2)->Take(bowl 1, from: shelf 2)->Goto(sidetable 2)
> Think: Now I find a desklamp (1) on the sidetable (2). Next, I need to use it.
> use desklamp 1
You turn on the desklamp 1.
"""

knowagent_clean_0="""You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Think: To solve the task, I need to first find and take an apple, then go to a sinkbasin and clean it with sinkbasin, then put it in sidetable.

> ActionPath: Start
> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1. 
> go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check the next diningtable. 
> go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check the next diningtable. 
> go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1. 
> go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1. 
> go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check the sinkbasin 1. 
> go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check the garbagecan 1. 
> go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> ActionPath: Start->Goto(garbagecan 1)
> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)
> Think: Now I get an apple (3). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)->Goto(sinkbasin 1)
> Think: Next I'll clean apple (3) with it.
> clean apple 3 with sinkbasin 1
You clean the apple 3 using the sinkbasin 1.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)->Goto(sinkbasin 1)->Clean(apple 3, with: sinkbasin 1)
> Think: Next, I need to go to sidetable 1.
> go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> ActionPath: Start->Goto(garbagecan 1)->Take(apple 3, from: garbagecan 1)->Goto(sinkbasin 1)->Clean(apple 3, with: sinkbasin 1)->Goto(sidetable 1)
> Think: Next, I need to put apple 3 in/on sidetable 1.
> put apple 3 in/on sidetable 1
You put the apple 3 in/on the sidetable 1.
"""

knowagent_clean_1="""You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.
> Think: To solve the task, I need to first find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. 

> ActionPath: Start
> Think: First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1.
> go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.

> Think: No lettuce found in fridge 1, I'll check the diningtable (1). 
> go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> ActionPath: Start->Goto(diningtable 1)
> Think: Now I find a lettuce (1) on the diningtable (1). Next, I need to take it.
> take lettuce 1 from diningtable 1
You pick up the lettuce 1 from the diningtable 1.

> ActionPath: Start->Goto(diningtable 1)->Take(lettuce 1, from: diningtable 1)
> Think: Now I get a lettuce (1). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.

> ActionPath: Start->Goto(diningtable 1)->Take(lettuce 1, from: diningtable 1)->Goto(sinkbasin 1)
> Think: Next I'll clean the lettuce (1) with sinkbasin 1.
> clean lettuce 1 with sinkbasin 1
You clean the lettuce 1 using the sinkbasin 1.

> ActionPath: Start->Goto(diningtable 1)->Take(lettuce 1, from: diningtable 1)->Goto(sinkbasin 1)->Clean(lettuce 1, with: sinkbasin 1)
> Think: Now I clean a lettuce (1). Next, I need to go to diningtable 1.
> go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> ActionPath: Start->Goto(diningtable 1)->Take(diningtable 1, from: diningtable 1)->Goto(sinkbasin 1)->Clean(lettuce 1, with: sinkbasin 1)->Goto(diningtable 1)
> Think: Next, I need to put the lettuce (1) in/on diningtable 1.
> put lettuce 1 in/on diningtable 1
You put the lettuce 1 in/on the diningtable 1.
"""

knowagent_clean_2 = """"You are in the middle of a room. Looking quickly around you, you see a bathtubbasin 1, a garbagecan 1, a handtowelholder 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.
Your task is to: clean some soapbar and put it in toilet.
> Think: To solve the task, I need to find and take a soapbar, then clean it with sinkbasin, then put it in toilet.

> ActionPath: Start
> Think: First I need to find a soapbar. A soapbar is more likely to appear in toilet (1), bathtubbasin (1), sinkbasin (1), shelf (1-3), garbagecan (1). I can check one by one, starting with toilet 1.
> go to toilet 1
On the toilet 1, you see a soapbar 4, and a soapbar 3.

> ActionPath: Start->Goto(toilet 1)
> Think: Now I find a soapbar (4). Next, I need to take it.
> take soapbar 4 from toilet 1
You pick up the soapbar 4 from the toilet 1.

> ActionPath: Start->Goto(toilet 1)->Take(soapbar 4, from: toilet 1)
> Think: Now I take a soapbar (4). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see nothing.

> ActionPath: Start->Goto(toilet 1)->Take(soapbar 4, from: toilet 1)->Goto(sinkbasin 1)
> Think: Next I'll clean soapbar 4 with sinkbasin 1.
> clean soapbar 4 with sinkbasin 1
You clean the soapbar 4 using the sinkbasin 1.

> ActionPath: Start->Goto(toilet 1)->Take(soapbar 4, from: toilet 1)->Goto(sinkbasin 1)->Clean(soapbar 4, with: sinkbasin 1)
> Think: Now I clean a soapbar (4). Next, I need to go to toilet 1.
> go to toilet 1
On the toilet 1, you see a soapbar 3.

> ActionPath: Start->Goto(toilet 1)->Take(soapbar 4, from: toilet 1)->Goto(sinkbasin 1)->Clean(soapbar 4, with: sinkbasin 1)->Goto(toilet 1)
> Think: Next, I need to put it in/on toilet 1.
> put soapbar 4 in/on toilet 1
You put the soapbar 4 in/on the toilet 1.
"""

knowagent_heat_0="""You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a hot apple in fridge.
> Think: To solve the task, I need to first find and take an apple, then heat it with microwave, then put it in fridge.

> ActionPath: Start
> Think: First I need to find an apple. An apple is more likely to appear in fridge (1), diningtable (1), coffeetable (1), drawer (1), cabinet (1-13), garbagecan (1). I can check one by one, starting with fridge 1. 
> go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a cup 1, and a egg 1.

> Think: No apple found in fridge 1, I'll check diningtable 1. 
> go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a fork 3, a fork 2, a fork 1, a mug 2, a peppershaker 3, a plate 2, a pot 1, a soapbottle 3, a spatula 1, a spoon 3, a spoon 2, a spoon 1, a winebottle 3, and a winebottle 2.

> ActionPath: Start->Goto(diningtable 1)
> Think: Now I find an apple (1) on the diningtable (1). Next, I need to take it.
> take apple 1 from diningtable 1
You pick up the apple 1 from the diningtable 1.

> ActionPath: Start->Goto(diningtable 1)->Take(apple 1, from: diningtable 1)
> Think: Now I get an apple (1). Next, I need to go to a microwave (1).
> go to microwave 1
The microwave 1 is closed.

> ActionPath: Start->Goto(diningtable 1)->Take(apple 1, from: diningtable 1)->Goto(microwave 1)
> Think: Next, I need to heat apple (1) with microwave (1).
> heat apple 1 with microwave 1
You heat the apple 1 using the microwave 1.

> ActionPath: Start->Goto(diningtable 1)->Take(apple 1, from: diningtable 1)->Goto(microwave 1)->Heat(apple 1, with: microwave 1)
> Think: Now I heat an apple (1). Next, I need to go to fridge 1.
> go to fridge 1
The fridge 1 is open. In it, you see a cup 1, and a egg 1.

> ActionPath: Start->Goto(diningtable 1)->Take(apple 1, from: diningtable 1)->Goto(microwave 1)->Heat(apple 1, with: microwave 1)->Goto(fridge 1)
> Think: Next, I need to put apple 1 in/on fridge 1.
> put apple 1 in/on fridge 1
You put the apple 1 in/on the fridge 1.
"""

knowagent_heat_1="""You are in the middle of a room. Looking quickly around you, you see a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a diningtable 1, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: heat some egg and put it in diningtable.
> Think: To solve the task, I need to first find and take an egg, then heat it with microwave, then put it in diningtable. 

> ActionPath: Start
> Think: First I need to find an egg. An egg is more likely to appear in fridge (1), countertop (1-3), diningtable (1), stoveburner (1-4), toaster (1), garbagecan (1), cabinet (1-10). I can check one by one, starting with fridge 1.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, and a potato 3.

> Think: No egg found in fridge 1, I'll check countertop 1. 
> go to countertop 1
On the countertop 1, you see a bread 1, a fork 1, and a saltshaker 1.

> Think: No egg found on countertop 1, I'll check the next countertop. 
> go to countertop 2
On the countertop 2, you see nothing.

> Think: No egg found on countertop 2, I'll check the next countertop. 
> go to countertop 3
On the countertop 3, you see a bowl 1, a butterknife 1, a egg 2, a kettle 2, a plate 1, a sink 1, and a spatula 2.

> ActionPath: Start->Goto(countertop 3)
> Think: Now I find an egg (2) on the countertop (3). Next, I need to take it.
> take egg 2 from countertop 3
You pick up the egg 2 from the countertop 3.

> ActionPath: Start->Goto(countertop 3)->Take(egg 2, from: countertop 3)
> Think: Now I get an egg (2).  Next, I need go to a microwave (1).
> go to microwave 1
The microwave 1 is closed.

> ActionPath: Start->Goto(countertop 3)->Take(egg 2, from: countertop 3)->Goto(microwave 1)
> Think: Now I need to heat an egg (2) with the microwave (1).
> heat egg 2 with microwave 1
You heat the egg 2 using the microwave 1.

> ActionPath: Start->Goto(countertop 3)->Take(egg 2, from: countertop 3)->Goto(microwave 1)->Heat(egg 2, with: microwave 1)
> Think: Now I heat an egg (2). Next, I need to go to diningtable 1.
> go to diningtable 1
On the diningtable 1, you see a apple 2, a bread 3, a egg 1, a kettle 1, a knife 1, a mug 1, a papertowelroll 1, a peppershaker 2, a potato 1, a soapbottle 1, and a spatula 1.

> ActionPath: Start->Goto(countertop 3)->Take(egg 2, from: countertop 3)->Goto(microwave 1)->Heat(egg 2, with: microwave 1)->Goto(diningtable 1)
> Think: Next, I need to put egg 2 in/on diningtable 1.
> put egg 2 in/on diningtable 1
You put the egg 2 in/on the diningtable 1.
"""

knowagent_cool_0="""You are in the middle of a room. Looking quickly around you, you see a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a drawer 9, a drawer 8, a drawer 7, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a cool mug in shelf.
> Think: To solve the task, I need to first find and take a mug, then cool it with fridge, then put it in shelf.

> ActionPath: Start
> Think: First I need to find a mug. A mug is more likely to appear in countertop (1-3), coffeemachine (1), cabinet (1-9), shelf (1-3), drawer (1-9). I can check one by one, starting with countertop 1. 
> go to countertop 1
On the countertop 1, you see a knife 1, a pan 2, a pan 1, and a plate 1.

> Think: No mug found on countertop 1, I'll check the next countertop. 
> go to countertop 2
On the countertop 2, you see a apple 2, a butterknife 2, a fork 3, a houseplant 1, a knife 2, a lettuce 3, a spatula 1, and a winebottle 1.

> Think: No mug found on countertop 2, I'll check the next countertop. 
> go to countertop 3
On the countertop 3, you see a apple 1, a book 1, a bread 1, a butterknife 3, a glassbottle 2, a glassbottle 1, a knife 3, a lettuce 2, a lettuce 1, a papertowelroll 1, a plate 3, a spoon 1, a statue 1, and a vase 2.

> Think: No mug found on countertop 3, I'll check coffeemachine 1.  
> go to coffeemachine 1
On the coffeemachine 1, you see nothing.

> Think: No mug found on coffeemachine 1, I'll check cabinet 1.
> go to cabinet 1
The cabinet 1 is closed.
> open cabinet 1
You open the cabinet 1. The cabinet 1 is open. In it, you see nothing.

> Think: No mug found in cabinet 1, I'll check the next cabinet.
> go to cabinet 2
The cabinet 2 is closed.
> open cabinet 2
You open the cabinet 2. The cabinet 2 is open. In it, you see nothing.

> Think: No mug found in cabinet 2, I'll check the next cabinet.
> go to cabinet 3
The cabinet 3 is closed.
> open cabinet 3
You open the cabinet 3. The cabinet 3 is open. In it, you see a pot 1.

> Think: No mug found in cabinet 3, I'll check the next cabinet. 
> go to cabinet 4
On the cabinet 4, you see nothing.

> Think: No mug found in cabinet 4, I'll check the next cabinet.
> go to cabinet 5
The cabinet 5 is closed.
> open cabinet 5
You open the cabinet 5. The cabinet 5 is open. In it, you see nothing.

> Think: No mug found in cabinet 5, I'll check the next cabinet.
> go to cabinet 6
The cabinet 6 is closed.
> open cabinet 6
You open the cabinet 6. The cabinet 6 is open. In it, you see a mug 3.

> ActionPath: Start->Goto(cabinet 6)
> Think: Now I find a mug (3) in cabinet 6. Next, I need to take it.
> take mug 3 from cabinet 6
You pick up the mug 3 from the cabinet 6.

> ActionPath: Start->Goto(cabinet 6)->Take(mug 3, from: cabinet 6)
> Think: Now I get a mug (3). Next, I need to go to a fridge (1).
> go to fridge 1
The fridge 1 is closed.

> ActionPath: Start->Goto(cabinet 6)->Take(mug 3, from: cabinet 6)->Goto(fridge 1)
> Think: Next I need cool mug (3) with fridge (1).
> cool mug 3 with fridge 1
You cool the mug 3 using the fridge 1.

> ActionPath: Start->Goto(cabinet 6)->Take(mug 3, from: cabinet 6)->Goto(fridge 1)->Cool(mug 3, with: fridge 1)
> Think: Now I cool the mug. Next, I need to go to shelf 1.
> go to shelf 1
On the shelf 1, you see a cup 2, a cup 1, a peppershaker 1, and a saltshaker 1.

> ActionPath: Start->Goto(cabinet 6)->Take(mug 3, from: cabinet 6)->Goto(fridge 1)->Cool(mug 3, with: fridge 1)->Goto(shelf 1)
> Think: Next, I need to put mug 3 in/on shelf 1.
> put mug 3 in/on shelf 1
You put the mug 3 in/on the shelf 1.
"""

knowagent_cool_1="""You are in the middle of a room. Looking quickly around you, you see a cabinet 16, a cabinet 15, a cabinet 14, a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 2, a countertop 1, a diningtable 1, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a safe 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: cool some pan and put it in stoveburner.
> Think: To solve the task, I need to first find and take a pan, then cool it with fridge, then put it in stoveburner.

> ActionPath: Start
> Think: First I need to find a pan. An pan is more likely to appear in stoveburner (1-4), sinkbasin (1), diningtable (1), countertop (1-2), cabinet (1-16), drawer (1-5). I can check one by one, starting with stoveburner 1.
> go to stoveburner 1
On the stoveburner 1, you see nothing.

> Think: No pan found on stoveburner 1, I'll check the next stoveburner. 
> go to stoveburner 2
On the stoveburner 2, you see a pot 1.

> Think: No pan found on stoveburner 2, I'll check the next stoveburner.
> go to stoveburner 3
On the stoveburner 3, you see a pan 1.

> ActionPath: Start->Goto(stoveburner 3)
> Think: Now I find a pan (1). Next, I need to take it.
> take pan 1 from stoveburner 3
You pick up the pan 1 from the stoveburner 3.

> ActionPath: Start->Goto(stoveburner 3)->Take(pan 1, from: stoveburner 3)
> Think: Now I get a pan (1). Next, I need to go to a fridge (1).
> go to fridge 1
The fridge 1 is closed.

> ActionPath: Start->Goto(stoveburner 3)->Take(pan 1, from: stoveburner 3)->Goto(fridge 1)
> Think: Next I need to cool a pan (1) with fridge (1).
> cool pan 1 with fridge 1
You cool the pan 1 using the fridge 1.

> ActionPath: Start->Goto(stoveburner 3)->Take(pan 1, from: stoveburner 3)->Goto(fridge 1)->Cool(pan 1, with: fridge 1)
> Think: Now I cool a pan (1). Next, I need to go to stoveburner (1).
> go to stoveburner 1
On the stoveburner 1, you see nothing.

> ActionPath: Start->Goto(stoveburner 3)->Take(pan 1, from: stoveburner 3)->Goto(fridge 1)->Cool(pan 1, with: fridge 1)->Goto(stoveburner 1)
> Think: Next I need to put pan (1) in/on stoveburner (1).
> put pan 1 in/on stoveburner 1
You put the pan 1 in/on the stoveburner 1.
"""

knowagent_cool_2="""You are in the middle of a room. Looking quickly around you, you see a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 2, a countertop 1, a diningtable 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: cool some potato and put it in diningtable.
> Think: To solve the task, I need to find and take a potato, then cool it with fridge, then put it in diningtable.

> ActionPath: Start
> Think: First I need to find a potato. A potato is more likely to appear in fridge (1), diningtable (1), countertop (1-2), cabinet (1-12), drawer (1-3), garbagecan (1). I can check one by one, starting with fridge 1.
> go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a apple 1, a bowl 1, a lettuce 2, and a lettuce 1.

> Think: No potato found in fridge 1, I'll check diningtable 1 next. 
> go to diningtable 1
On the diningtable 1, you see a apple 3, a bread 1, a butterknife 3, a egg 2, a fork 1, a knife 2, a knife 1, a mug 1, a peppershaker 3, a plate 1, a potato 4, a potato 2, a saltshaker 2, a soapbottle 2, and a tomato 3.

> ActionPath: Start->Goto(fridge 1)
> Think: Now I find a potato (2). Next, I need to take it.
> take potato 2 from diningtable 1
You pick up the potato 2 from the diningtable 1.

> ActionPath: Start->Goto(fridge 1)->Take(potato 2, from: diningtable 1)
> Think: Now I take a potato (2). Next, I need to go to a fridge (1).
> go to fridge 1
The fridge 1 is open. In it, you see a apple 1, a bowl 1, a lettuce 2, and a lettuce 1.

> ActionPath: Start->Goto(fridge 1)->Take(potato 2, from: diningtable 1)->Goto(fridge 1)
> Think: Next, I need to cool potato 2 with fridge 1.
> cool potato 2 with fridge 1
You cool the potato 2 using the fridge 1.

> ActionPath: Start->Goto(fridge 1)->Take(potato 2, from: diningtable 1)->Goto(fridge 1)->Cool(potato 2, with: fridge 1)
> Think: Now I cool a potato (2). Next, I need to go to diningtable 1.
> go to diningtable 1
On the diningtable 1, you see a apple 3, a bread 1, a butterknife 3, a egg 2, a fork 1, a knife 2, a knife 1, a mug 1, a peppershaker 3, a plate 1, a potato 4, a saltshaker 2, a soapbottle 2, and a tomato 3.

> ActionPath: Start->Goto(fridge 1)->Take(potato 2, from: diningtable 1)->Goto(fridge 1)->Cool(potato 2, with: fridge 1)->Goto(diningtable 1)
> Think:  Next, I need to put potato 2 in/on diningtable 1.
> put potato 2 in/on diningtable 1
You put the potato 2 in/on the diningtable 1.
"""

knowagent_puttwo_0="""You are in the middle of a room. Looking quickly around you, you see a armchair 2, a armchair 1, a bed 1, a countertop 1, a diningtable 1, a drawer 2, a drawer 1, a dresser 1, a garbagecan 1, a laundryhamper 1, and a sidetable 1.
Your task is to: put two creditcard in dresser.
> Think: To solve the task, I need to find and take the first creditcard, then put it in dresser, then find and take the second creditcard, then put it in dresser. I cannot hold more than one object at the same time.

> ActionPath: Start
> Think: First I need to find the first creditcard. A creditcard is more likely to appear in drawer (1-2), coutertop (1), sidetable (1), diningtable (1), armchair (1-2), bed (1). I can check one by one, starting with drawer 1.
> go to drawer 1
The drawer 1 is closed.
> open drawer 1
You open the drawer 1. The drawer 1 is open. In it, you see a book 1, a cd 1, and a pen 1.

> Think: No creditcard found in drawer 1, I'll check the next drawer. 
> go to drawer 2
The drawer 2 is closed.
> open drawer 2
You open the drawer 2. The drawer 2 is open. In it, you see nothing.

> Think: No creditcard found in drawer 2, I'll check countertop 1 next. 
> go to countertop 1
On the countertop 1, you see a cellphone 2, a creditcard 4, a creditcard 3, a creditcard 2, a mirror 1, a pencil 2, and a pencil 1.

> ActionPath: Start->Goto(countertop 1)
> Think: Now I find the first creditcard (2). Next, I need to take it. I can find the second creditcard (3) later in countertop 1.
> take creditcard 2 from countertop 1
You pick up the creditcard 2 from the countertop 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)
> Think: Now I get the first creditcard (2). Next, I need to go to dresser 1. And remember I can find the second creditcard (3) later in countertop 1.
> go to dresser 1
On the dresser 1, you see a mug 1, and a television 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)->Goto(dresser 1)
> Think: Next, I need to put creditcard 2 in/on dresser 1. And remember I can find the second creditcard (3) later in countertop 1.
> put creditcard 2 in/on dresser 1
You put the creditcard 2 in/on the dresser 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)->Goto(dresser 1)->Put(creditcard 2, in/on: dresser 1)
> Think: Next, I need to find the second creditcard. I can directly go to countertop 1.
> go to countertop 1
On the countertop 1, you see a cellphone 2, a creditcard 4, a creditcard 3, a mirror 1, a pencil 2, and a pencil 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)->Goto(dresser 1)->Put(creditcard 2, in/on: dresser 1)->Goto(countertop 1)
> Think: Now I find the second creditcard (3). Next, I need to take it.
> take creditcard 3 from countertop 1
You pick up the creditcard 3 from the countertop 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)->Goto(dresser 1)->Put(creditcard 2, in/on: dresser 1)->Goto(countertop 1)->Take(creditcard 3, from: countertop 1)
> Think: Now I get the second creditcard (3). Next, I need to go to dresser 1.
> go to dresser 1
On the dresser 1, you see a creditcard 2, a mug 1, and a television 1.

> ActionPath: Start->Goto(countertop 1)->Take(creditcard 2, from: countertop 1)->Goto(dresser 1)->Put(creditcard 2, in/on: dresser 1)->Goto(countertop 1)->Take(creditcard 3, from: countertop 1)->Goto(dresser 1)
> Think: Next, I need to put creditcard 3 in/on dresser 1.
> put creditcard 3 in/on dresser 1
You put the creditcard 3 in/on the dresser 1.
"""

knowagent_puttwo_1="""You are in the middle of a room. Looking quickly around you, you see a coffeetable 1, a diningtable 1, a drawer 4, a drawer 3, a drawer 2, a drawer 1, a dresser 1, a garbagecan 1, a sidetable 2, a sidetable 1, and a sofa 1.
Your task is to: put two cellphone in sofa.
> Think: To solve the task, I need to find and take the first cellphone, then put it in sofa, then find and take the second cellphone, then put it in sofa. I cannot hold more than one object at the same time.

> ActionPath: Start
> Think: First I need to find the first cellphone. A cellphone is more likely to appear in coffeetable (1), diningtable (1), sidetable (1-2), drawer (1-4), sofa (1), dresser (1), garbagecan (1). I can check one by one, starting with coffeetable 1.
> go to coffeetable 1
On the coffeetable 1, you see a box 1, a cellphone 3, and a plate 1.

> ActionPath: Start->Goto(coffeetable 1)
> Think: Now I find the first cellphone (3). Next, I need to take it.
> take cellphone 3 from coffeetable 1
You pick up the cellphone 3 from the coffeetable 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)
> Think: Now I get the first cellphone (3). Next, I need to go to sofa 1.
> go to sofa 1
On the sofa 1, you see a newspaper 2, a pillow 1, a remotecontrol 2, and a remotecontrol 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)->Goto(sofa 1)
> Think: Next, I need to put it in/on sofa 1.
> put cellphone 3 in/on sofa 1
You put the cellphone 3 in/on the sofa 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)->Goto(sofa 1)->Put(cellphone 3, in/on: sofa 1)
> Think: Now I put the first cellphone in sofa. Next, I need to find the second cellphone. I have visited coffeetable (1), so the second cellphone is more likely to appear in diningtable (1), sidetable (1-2), drawer (1-4), sofa (1), dresser (1), garbagecan (1). I can check one by one, starting with coffeetable 1. 
> go to diningtable 1
On the diningtable 1, you see a cellphone 2, a keychain 2, a laptop 1, a statue 2, and a statue 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)->Goto(sofa 1)->Put(cellphone 3, in/on: sofa 1)->Goto(diningtable 1)
> Think: Now I find the second cellphone (2). Next, I need to take it.
> take cellphone 2 from diningtable 1
You pick up the cellphone 2 from the diningtable 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)->Goto(sofa 1)->Put(cellphone 3, in/on: sofa 1)->Goto(diningtable 1)->Take(cellphone 2, from: diningtable 1)
> Think: Now I get the second cellphone (2). Next, I need to go to sofa 1.
> go to sofa 1
On the sofa 1, you see a cellphone 3, a newspaper 2, a pillow 1, a remotecontrol 2, and a remotecontrol 1.

> ActionPath: Start->Goto(coffeetable 1)->Take(cellphone 3, from: coffeetable 1)->Goto(sofa 1)->Put(cellphone 3, in/on: sofa 1)->Goto(diningtable 1)->Take(cellphone 2, from: diningtable 1)->Goto(sofa 1)
> Think: Next, I need to put cellphone 2 in/on it.
> put cellphone 2 in/on sofa 1
You put the cellphone 2 in/on the sofa 1.
"""
