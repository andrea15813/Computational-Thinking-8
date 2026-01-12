SZA_points=0
Tylerthecreator_points=0
SabrinaCarpenter_points=0
Laufey_points=0
OliviaRodrigo_points=0
Katseye_points=0
KendrickLamar_points=0
Drake_points=0

answer1=input("How would you discribe yourself A-funny, B-nice, C-problematic, D-selfcentered")
if answer1== "A" or "a":
    SZA_points+=1
    Katseye_points+=1
elif answer1== "B" or "b":
    Laufey_points+=1
    OliviaRodrigo_points+=1
elif answer1== "C" or "c":
    KendrickLamar_points+=1
    Drake_points+=1
elif answer1== "D" or "d":
    SabrinaCarpenter_points+=1
    Tylerthecreator_points+=1

answer2=input("What do you do for fun? A-Dance, B-Play sports, C-Watch TV, D-Sing")
if answer2== "A" :
    Katseye_points+=1
    Tylerthecreator_points+=1
elif answer2== "B":
    Drake_points+=1
    SZA_points+=1
elif answer2== "C":
    KendrickLamar_points+=1
elif answer2== "D":
    Laufey_points+=1
    SabrinaCarpenter_points+=1
    OliviaRodrigo_points+=1

answer3=input("What's your dream job? A-Singer/dancer, B-Actor, C-teacher, D-athlete")
if answer3== "A":
    SabrinaCarpenter_points+=2
    Katseye_points+=1
    SZA_points+=1
    Tylerthecreator_points+=1
elif answer3== "B":
    SabrinaCarpenter_points+=1
    OliviaRodrigo_points+=1
elif answer3== "C":
    Laufey_points+=1
    KendrickLamar_points+=1
elif answer3== "D":
    SZA_points+=1
    Drake_points+=1

answer4=input("What's your favorite class in school? A-math, B-english, C-dance, D- PE, E-science")
if answer4== "A":
    OliviaRodrigo_points+=1
    SZA_points+=1
elif answer4=="B":
    Laufey_points+=1
    KendrickLamar_points+=1
elif answer4=="C":
    Katseye_points+=1
elif answer4=="D":
    Drake_points+=1
elif answer4=="E":
    SabrinaCarpenter_points+=1
    Tylerthecreator_points+=1

answer5=input("what is your favorite food. A-Pizza, B-sushi, C-pasta, D-waffles")
if answer5=="A":
    Drake_points+=1
    KendrickLamar_points+=1
elif answer5=="B":
    OliviaRodrigo_points+=1
    Katseye_points+=1
elif answer5=="C":
    SabrinaCarpenter_points+=1
    Laufey_points+=1
elif answer5=="D":
    SZA_points+=1
    Tylerthecreator_points+=1

print(f"Your score is {SZA_points}sza, {Tylerthecreator_points}tyler, {Katseye_points}katseye, {OliviaRodrigo_points}olivia, {SabrinaCarpenter_points}sabrina, {KendrickLamar_points} kendrick, {Drake_points}drake, {Laufey_points}laufey")

# endofquiz:
if SZA_points>Tylerthecreator_points and SZA_points>Laufey_points and SZA_points>SabrinaCarpenter_points and SZA_points>Katseye_points and SZA_points>OliviaRodrigo_points and SZA_points>Drake_points and SZA_points>KendrickLamar_points :
    print ("You got SZA. You are athletic, pretty, nice and very talented")
elif Tylerthecreator_points>SZA_points and Tylerthecreator_points>Laufey_points and Tylerthecreator_points>SabrinaCarpenter_points and Tylerthecreator_points>Katseye_points and Tylerthecreator_points>OliviaRodrigo_points and Tylerthecreator_points>Drake_points and Tylerthecreator_points>KendrickLamar_points:
    print ("You got Tyler the creator. You are probably funny, smart and have a good sense of humor")
elif Laufey_points>SZA_points and Laufey_points>Tylerthecreator_points and Laufey_points>SabrinaCarpenter_points and Laufey_points>Katseye_points and Laufey_points>OliviaRodrigo_points and Tylerthecreator_points>Drake_points and Tylerthecreator_points>KendrickLamar_points:
    print ("You got Laufey. You're probably very smart, relaxed and caring")
elif SabrinaCarpenter_points>SZA_points and SabrinaCarpenter_points>Tylerthecreator_points and SabrinaCarpenter_points>Laufey_points and SabrinaCarpenter_points>Katseye_points and SabrinaCarpenter_points>OliviaRodrigo_points and SabrinaCarpenter_points>Drake_points and SabrinaCarpenter_points>KendrickLamar_points:
    print("you got sabrina carprenter. You are probably a good singer and a funny person")
elif Katseye_points>SZA_points and Katseye_points>Tylerthecreator_points and Katseye_points>Laufey_points and Katseye_points>SabrinaCarpenter_points and Katseye_points>OliviaRodrigo_points and Katseye_points>Drake_points and Katseye_points>KendrickLamar_points:
    print("You got katseye. You are very passionate about dancing and you're very funny")
elif OliviaRodrigo_points>SZA_points and OliviaRodrigo_points>Tylerthecreator_points and OliviaRodrigo_points>Laufey_points and OliviaRodrigo_points>Katseye_points and OliviaRodrigo_points>SabrinaCarpenter_points and OliviaRodrigo_points>Drake_points and OliviaRodrigo_points>KendrickLamar_points:
    print ("You got Olivia Rodrigo, you are very nice, talented, and a bit shy")
elif Drake_points>SZA_points and Drake_points>Tylerthecreator_points and Drake_points>Laufey_points and Drake_points>SabrinaCarpenter_points and Drake_points>Katseye_points and Drake_points>OliviaRodrigo_points and Drake_points>KendrickLamar_points:
    print ("You got drake. You like sports and kids.")
elif KendrickLamar_points>SZA_points and KendrickLamar_points>Tylerthecreator_points and KendrickLamar_points>Laufey_points and KendrickLamar_points>SabrinaCarpenter_points and KendrickLamar_points>Katseye_points and KendrickLamar_points>OliviaRodrigo_points and KendrickLamar_points>Drake_points:
    print ("You got kendrick lamar, you are probably a hater, but skilled")
