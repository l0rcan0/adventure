#intro
print("You find yourself stranded on a desolate island. You don't know how you got there, nor do your friends, but you need to get out of here. You have faint memories from where you were before though; you were with some friends from school.")

#friends
friend1=input("Who is the first friend you are with: ")
friend2=input("Who is the second friend you are with: ")
friend3=input("Who is the third friend you are with: ")

#decision 1
choicea1=(f"You agree with {friend1} and suggest you should assign roles to eachother and split up.")
choiceb1=(f"You agree with {friend2} and suggest you try and built a temporary shelter for you all.")
choicec1=(f"You agree with {friend3} and suggest everyone tries to swim away.")
print(f"You and your friends decide to have a meeting and decide what to do. {friend1} suggests that everyone splits up with different roles, {friend2} suggests that they need to prioritise shelter first, and {friend3} says that all 4 of you should try and swim away. What do you think you should do?")
print("Should you A, give everyone roles and split up?")
print("Should you B, prioritise shelter?")
print("Or should you C, try to swim away?")
choice1=input("What do you choose: ")
if choice1 == "a":
    print(choicea1)
if choice1 == "b":
    print(choiceb1)
if choice1 == "c":
    print(choicec1)

#aftermath of decision 1
