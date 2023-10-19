# stuff
import random

def start2():
    start = input("Enter 'start' to start: ")
    if start == "start":
        print("You find yourself stranded on a desolate island. You don't know how you got there, but you need to get out of here. You have faint memories from where you were before though; you were with some friends from school.")
    else:
        print("You can't do anything until you have typed start")
        start2()

def death():
    print("""
     __  __     ______     __  __             
    /\ \_\ \   /\  __ \   /\ \/\ \            
    \ \____ \  \ \ \/\ \  \ \ \_\ \           
     \/\_____\  \ \_____\  \ \_____\          
      \/_____/   \/_____/   \/_____/                                            
     __  __     ______     __   __   ______   
    /\ \_\ \   /\  __ \   /\ \ / /  /\  ___\  
    \ \  __ \  \ \  __ \  \ \ \'/   \ \  __\  
     \ \_\ \_\  \ \_\ \_\  \ \__|    \ \_____\ 
      \/_/\/_/   \/_/\/_/   \/_/      \/_____/                               
     _____     __     ______     _____        
    /\  __-.  /\ \   /\  ___\   /\  __-.      
    \ \ \/\ \ \ \ \  \ \  __\   \ \ \/\ \     
     \ \____-  \ \_\  \ \_____\  \ \____-     
      \/____/   \/_/   \/_____/   \/____/     
    """)
    print("Cause of death: drowning.")
    exit()
# title
print("""=================================-----------------------------------------------------------::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-------:-:--:-::
============================--------------------------------------------::::---:::::-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-:-----
==========--======------------------------------------------------------::::::::::::::::::::::::::::::::::+*++=-...-*:.:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-----
===============-=-==-----------------------------------------------------:::::::::::::::::::::::::::::.-*##*########***+...::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::------------
======================--------------------------------------------------:::::::::::::::::::::::::::..:+#****##************-::::::::::::::::::::::::::::::::::::::::--------------------------------------------
======================-------------------------------------------------------------::::::::::::::::=*#***********************:::::::::::::::::::---------------------------------------------------------------
======================================-------------------------------------------------:::::::::=*****###*********************+:::::::::::::::----------------------------------------------------------=---===
+++++++===================================================---------------------------:::::::::+*******##**************************+-+**+*=:::::-------------------------------------------=====================
+++++++++++++++++++++++++++==================================---------=------------:::::::-+************#####*****++++*+=**#####*********#**=::::::----------------============================================
++++++++++++++++++++++++++++++++++++++++++====================-=*************++**+=::::=**************#######*************+*###**#########******+=:::--+**+*-----==============================================
*************+++++++++++++++++++++++++++++++++++++++==========+##***************+=-=*******##***+===**#####*###*#****##******###############*********+++****++---==============================================
*************************+++++++++++++++++++++++++++++++====+*##**#####******+++*****#####*###*#+*****########*##****#######*#################*#*#***+++++++++*+=-==========================================+==
***********************************++++++++++++++++++++++=+*###########*****###**##########*+***+*#*#**##*###########*##**###*###############*#####*****++++++++++-==================================+++++===++
*****************************************++++++++++++++++*#####################**#######*#*#**#****###############*#**###*####*###########*##***######******+++++++=================++++++++++++===============
##**********************************************+++++***##########**########%##%%%%#*+##############**%###########*##########***###**######*######*#####********+++++======++++==++++++++++++++++++++==========
######**#******************************************########*****#########%%%%%%##***#**####*##*#####*#%##############*#*#**###**####################*######*##*+***+*+-==++++++=+=++++++++++++++++++++++++++++=
############*###*###******************+*****######*#######*#######%#%#%%%%%#*+*###########*###########%##################***#**##**+##*######*#######*#######**###******+==++++++++++++++++++++++++++++++++++++
########################**#*#####******++==+*#**######*****##%##%%%#%#*#***##################%#############%##########***###****#****-=**+*####*##**###########*#######***==+++=+++++++++++++++++++++++++++++++
################################*+++*+=**+=++**####**##**######%%%+++*####%#%%%%%%%%%%%###%###%%%############%*#####%#***+*##*****###*++##**#######*##############*########*+++++++++++++++++++++++++++++++++++
################*###########%%%%+#*****#%***+=+++++#***####%%%**++##%%%%%%%%%%%%%%%%%%%%#**#####%#*=+#*##%**##%#######*+***#*#*#########=:-*+*####################################*++++++++++++++++++++++++++++
########################+#%%%@@%%##%*#%%@%%##*+++*#%%%%%%%#-+++#*%@%%%%%%%@@%%%@@@@%%%#*#+:++*###==+*#%#%%%%%%######%#########*#%###*###%#**+****######%#############**#############**=++++++++++++++++++++++++
##################**#*###*==*##%@@@%####*#%%%%%%%%%####*=++##%%%%@@%%%#%#*###%%%%%%#%#%%%%+**%#+*#####%#%%%%%%%%%#####*+%######*%#%%#%##%%%###*+#*##*##############++=-::--++=+**-:----==++++++++++++++++=+++++
%########################%%%%%#%%%%%%%%%%#%@@%%*+=+++*%%%@%%@@%*%%%%%#*%###*##%%%%#%%%%%%%%*#%#%%#%%%#%%##%##%%%%%######%####%###%###%###%%%%#*+***#########*+====++++************+++++++++++++++++++++++++++++
##%#####################%#%%%%%%##**#####*+-=+==*#%%%%%%@@%#%######*=*#*#%%%%%%%###%%%%%%%%%%%%%%%%%%%%###%%*%###*#%%%#%####%%%########%##%%%**##*******=-==+*********************+++++++++****+*++++++++++++++
%%####%#%############*####==%#****=--===++++*%%@%%%%%%#+*#%%#****###*%%###%%%%%####%%%%%%%%%%%%%%%%###*=:--=+*++*++****####%%%%##############**######+::+***************************++++++++*+*+++*++++++++++++
%%%%###%%#%#########**=-:-#%%%%%%%%%%%%%%%%@**********#%%%%%%%%%%%#######%###+######%%%%%%%%#+####**###*#####******###*##***++++:-=-::-=+******+=::+************+******************++++++************++++++++*+
%%%%%%%%%#####%#%%####*#*-::--=-=-+====*%%%%%%%%%%%############################+++++=*###############*###*#**##*#*################****#****************************************++++***++**+*******+++**********
%%%%%%%%%%%%#%#%%%%%%#######%#%#%%%%##%%%##%%%#%####*#########################################*######*#####*#*##################*##########**##**********+***+************************+******+*****************
%%%#%%%%##%%%%%%%%%%%%%%%%%%%%%%%%%#*%%%#%###*#########################################*#****#*****###############**#***####*#####*#**#######*******************************************+*+***+*****+**********
%%%%%%%%%%%%%#%%%%#%#%%%%%%%%%%%%%%%%%#####%###%#%%%%##################################**##**#****####*#*#######*###################*######*#******************************************************************
""")
print("NOT ALL PATHS WORK.")
print("")
# intro
start2()

# friends
frienda=input("Who is the first friend you are with: ")
friendb=input("Who is the second friend you are with: ")
friendc=input("Who is the third friend you are with: ")
friend1 = frienda.title()
friend2 = friendb.title()
friend3 = friendc.title()

# decision 1 + outcomes
print(f"""You and your friends decide to have a meeting and decide what to do.
{friend1} suggests that everyone splits up with different roles,
{friend2} suggests that you need to prioritise shelter first,
and {friend3} says that all 4 of you should try and swim away.
What do you think you should do?""")
print("Should you 'a', give everyone roles and split up?")
print("Should you 'b', prioritise shelter?")
print("Or should you 'c', try to swim away?")

choice1=input("What do you choose: ")
if choice1 == "a":
    print(f"You agree with {friend1} and suggest you should assign roles to eachother and split up.")
    print("You present the 3 most important things that need to be done.")
    print("Food and water (a), shelter (b), and exploring the island (c).")
    choice2=input("What do you choose: ")
elif choice1 == "b":
    print(f"You agree with {friend2} and suggest you try and built a temporary shelter for you all.")
    print("You now need to decide what everyone should do to make the house. One can gather the materials (a), another can build the house (b), and another can explore the island to see if they can find anythign useful (c).")
    choice2b=print("What do you choose: ")
elif choice1 == "c":
    print(f"You agree with {friend3} and suggest everyone tries to swim away.\n")
    print("")
    print("You and your friends head out to the ocean and look out into the water. It seems fine, but you can't see anywhere to go, so you'll just have to wing it, and wing it you do.")
    print("You're first to jump in, and everyone quickly follows behind. Although the water is almsot crystal clear, through your eyes, it looks gloomy and trouble-enducing, yet you continue on.")
    print('After swmiming for a few more minutes, you realise that you were right. Every where you look is filled with nothing but blank skies, water and your exhausted friends; not even any clouds. "Are we gonna die?!" "Yeah probably." Everyone seems very panicked, and for good reason. Stranded in the middle of the ocean with your friends and nothing to aid you in getting to shore, your only option is to sit there and wait until your impending death.')

    death()
# aftermath of decision 1
    # explore island
if choice2b == "c":
    print(f"You decide to explore the island, {friend2} says they want to build the house, so {friend3} is left to gather the materials. {friend1} chose to help {friend3} since no one else wanted to swim with them.")
    print("")
    print("After leaving the gathering, you walk around the forrest aimlessly, seeing if you find anythign useful, and useful you found. Burried in the side of a mountian lay a dark door. With no signes of anything that could deter you away from it, so you invite yourself in.")
    print("It seemed to be an abandoned cave, and on the wall were 3 tools, all paired with mining helmets: a pickaxe, an axe and a handhelp lighter. Although they could be useful, there was no one else with you, so you could always come back to get one if you needed it, so you just took one of the mining helmets and continued down the narrow, rocky path.")
    print("As you were walking, you stumbled upon 2 pathways, one seemed to be blocked off so that forces you to go to the other one: climbing up some rocks into a tunnel.")
    print("It seems too high to climb, so you will need to go back to grab a pickaxe since it's probably the thing that could help you the most.")

    # food + water
if choice2 == "a" or "A":
    print("You say that you want to get food and water, and everyone else agrees.")
    print(f"{friend1} tells you that they noticed coconuts on some trees and some berries on a few bushes, and tell you to get some coconuts first in case the berries are posionous, however, you are faced with an immediate problem: climbing the tree. It's too smooth and too tall to climb with bare hands, especially since it's raining. This means you'll have to explore the island and look for something to help you, or you could risk climbing it.")
    choice3=input("What do you choose ('explore' or 'climb'): ")

    # climb
if choice3 == "climb" or "Climb":
    print("You chose to attempt to climb the tree.")
    print("As you struggle to climb it, your hand slips and you can't seem to regain grip, causing you to slip off and hit your head pretty hard leaving you unconcious on the ground. You now have to wait until you wake up."),
    print(""),
    print(f"After approximately 10 mins, you find yourself in a makeshift bed. You can see {friend2} out of the window doing the best they can to cook some pork over an open flame."),
    print(f"Your wounds seem taken care of and for the most part, you feel fine, so you go outside to help {friend2}."),
    print(f"You greet them and they immediately inform you on what has happened while you were 'gone;' {friend3} chose to try and swim away, but without the help of everyone else, failed. {friend1} chose to help {friend2} with shelter, but is currently gathering some more wood for their flame."),
    print(f'They also said they stumbled upon you after they came to see how you were going. "I have found a few more tools, take this knife and we can try those berries {friend1} saw earlier if you want." You agree.')
    print("If you like, you can try to re-climb the tree, or you can get some berries and bring them back to the hut.")
    choice4=input("what do you choose ('re-climb tree' or 'get berries'): ")

    # re-climb tree
    if choice4 == "re-climb tree":
        print(f"You've learn your lesson from last time and decided to use the knife given to you to aid you in climbing it. By continuously stabbing the knife into the tree and using it as leverage, you successfully climb it and gather it's coconuts. After climbing down, you head back to {friend2}'s hut.")
        print("")
        print(f'{friend2} welcomes you back. They see you got some coconuts and asked if you saw anything that would be of use to open them, "Nah I was only focusing on getting the coconuts, not opening them." You reply, "All good, we can just find a rock or something." {friend2} says, you agree.')
        print(f"You and {friend2} head out together to try and find something that would help you crack open these coconuts. While exploring, you unexpectedly stumble upon {friend3}, who seems to be doing pretty well, you greet eachother. {friend2} asks what they'd been doing, and {friend3} explains that after failing to swim away, they decided to explore the island. After exploring for a bit, they hit the jackpot; a mysterious temple, covered in moss, with a ton of supplies in it and a glowing pillar in the middle. It also has a battered up note which reads:")
        print('"Though this is nothing"')
        print('"This island holds a treasure"')
        print('"It glistens while dark"')
        print("")
        print(f'In the corner of the note, you notice fading text that also says: "Find it." You point it out to everyone and ask if anyone can decipher what it means. "I saw a cave earlier, the thing they are talking about could be in there since it glistens while dark?" {friend3} suggests. "Could be" {friend2} says.')
        print(f"What do you think?")
        choice5=input(f"Do you want to keep doing what you're doing (a), or retrace {friend3}'s steps to the cave (b): ")

    # retrace steps to cave
    if choice5 == "b":
        print('"I say we go to that cave, sounds like it could lead somewhere." You say. Both friends agree.')
        print("")
        print('"I think it was around here somewhere."')
        print(f'"Yeah, there, I see it!" You point towards a dark doorway on the side of a mountain, and everyone runs over. It is indeed the cave. There seems to be no caution signs anywhere, so you are the first person to go in, while {friend2} and {friend3} follow you. "Looks like a mine" {friend3} points out. "No way" you say sarcastically.')
        print("On the wall of the rocks, you notice 3 tools, perfect for the 3 of you. There's a 'pickaxe', an 'axe' and a 'handheld lighter' along with 3 mining helmets besides each of them.")
        choice6=input(print("Which one do you choose: "))

    # pickaxe
    if choice6 == "pickaxe":
        print("You chose the pickaxe.")
        print(f"{friend2} chooses the axe before {friend3} can, therefore leaving {friend3} with the handheld lighter. They're visibly disappointed by this, while {friend2} has triumph written all over their face.")
        print("Before anyone can complain, you run down further into the cave and both friends rush to catch up.")
        print("After exploring for a few minutes, you 3 are faced with 2 options; 1: Try climbing the wall up to an opening that seems to be safer, but carries the risk of falling, again. Or 2: Go through the windy, narrow path to the left with jagged walls and possibly more that you can't see, but it's more straight forward.")
        choice7 = print("What do you choose (1 or 2): ")

        # go left
        if choice7 == "2":
            print("Without hesitation, you go to the left path and realise: it's blocked off by masses of rock. You you're forced to go to the other path")
            print('Despite previously failing to climb something, you feel confident with this, however the concequences for failing could be much worse.')
            print(f'You decide to go first as if you fail, you have 2 people there to help you. "How about I climb on someones shoulders and use that as leverage to climb up, then I can help you 2." {friend2} and {friend3} agree.')
            print(f'{friend3} volunteers to help you climb up and heaves you up onto their shoulders. "I will hold onto the wall while you move our from under me and push my feet up, then I will be able to reach the top and climb up." You tell {friend3}. "Yeah that could work." You follow out with the plan, {friend3} pushes your feet up, allowing you to climb up to the top. "Nice!"')
            print(f'"Ok, who is next?" {friend2} volunteers to go next. They repeat the steps until {friend2} is up, with a bit of your assistance. All {friend3} needs is both of your help and they are up, which you do.')
            print("")

            # crystal + temple
            print(f'After a few minutes of walking down the somewhat compact tunnel, you reach an massive, open area, almost like a dome. It is quite steep but is not an issue. {friend2} points out something glistening in a tiny crevice. All 3 of you sprint over to it, and {friend3} being the smallest, sticks their hand in a pulls out a vibrant crystal and a piece of paper, similar to the hint from before. It reads:')
            print('"You have done well in this quest. Your final challenge is to locate a temple in the middle of the island, and place this crystal in the socket at the center."')
            print(f'"I know where that is! Follow me." You and {friend3} obey and follow {friend3}.')
            print(f'"Here it is." You arrive at pressumably the temple the note was talking about, and carefully creep inside. All the walls seem like they are closing in on you, even though they are not. Moss is hanging from the ceiling and mould is littering every surface of the place, except for a mini pillar with a shape carved into it, perfect for the crystal you have found. The pillar was the opposite of everything else in the temple, it radiated an indistinguashable aura and had a bright yellow glow, almost like the sun. Before anyone can say anything, {friend3} places the crystal on the pillar and in classic movie fashion, your vision is filled with white.')
            print("")

            # ending
            print("After regaining conciousness, you look around and realise; it was all a dream, but you have the same crystal from the dream. Confused about everything, you get up and ask both your parents if they know what the crystal is and that you don't know why you have it. They are just as confused as you are, and have no idea what the crystal is.")
            print("You think for a bit, and decide to go to a pawn shop, and see what you could get for it.")
            print("")
            print("Although they are professionals, they can't tell what it is either, therefore they can't give you an offer. You leave the pawn shop confused and holding a mysterious piece of rock.")
            print("")
            print(f"After walking for a bit, not knowing what to do, you realise: what happened to {friend1}? And that the tools on the wall were useless.")
            print("...")

        # climb to top path
        if choice7 == "1":
            print('"You wanna try climbing this thing?" "Sure." Despite previously failing to climb something, you want to redeem yourself with this, however the concequences for failing could be much worse.')
            print(f'You decide to go first as if you fail, you have 2 people there to help you. "How about I climb on someones shoulders and use that as leverage to climb up, then I can help you 2." {friend2} and {friend3} agree.')
            print(f'{friend3} volunteers to help you climb up and heaves you up onto their shoulders. "I will hold onto the wall while you move our from under me and push my feet up, then I will be able to reach the top and climb up." You tell {friend3}. "Yeah that could work." You follow out with the plan, {friend3} pushes your feet up, allowing you to climb up to the top. "Nice!"')
            print(f'"Ok, who is next?" {friend2} volunteers to go next. They repeat the steps until {friend2} is up, with a bit of your assistance. All {friend3} needs is both of your help and they are up, which you do.')
            print("")

            # crystal + temple
            print(f'After a few minutes of walking down the somewhat compact tunnel, you reach an massive, open area, almost like a dome. It is quite steep but is not an issue. {friend2} points out something glistening in a tiny crevice. All 3 of you sprint over to it, and {friend3} being the smallest, sticks their hand in a pulls out a vibrant crystal and a piece of paper, similar to the hint from before. It reads:')
            print('"You have done well in this quest. Your final challenge is to locate a temple in the middle of the island, and place this crystal in the socket at the center."')
            print(f'"I know where that is! Follow me." You and {friend3} obey and follow {friend3}.')
            print(f'"Here it is." You arrive at pressumably the temple the note was talking about, and carefully creep inside. All the walls seem like they are closing in on you, even though they are not. Moss is hanging from the ceiling and mould is littering every surface of the place, except for a mini pillar with a shape carved into it, perfect for the crystal you have found. The pillar was the opposite of everything else in the temple, it radiated an indistinguashable aura and had a bright yellow glow, almost like the sun. Before anyone can say anything, {friend3} places the crystal on the pillar and in classic movie fashion, your vision is filled with white.')
            print("")

            # ending
            print("After regaining conciousness, you look around and realise; it was all a dream, but you have the same crystal from the dream. Confused about everything, you get up and ask both your parents if they know what the crystal is and that you don't know why you have it. They are just as confused as you are, and have no idea what the crystal is.")
            print("You think for a bit, and decide to go to a pawn shop, and see what you could get for it.")
            print("")
            print("Although they are professionals, they can't tell what it is either, therefore they can't give you an offer. You leave the pawn shop confused and holding a mysterious piece of rock.")
            print("")
            print(f"After walking for a bit, not knowing what to do, you realise: what happened to {friend1}? And that the tools on the wall were useless.")
            print("...")
















