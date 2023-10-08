age = int(input("enter the age of the child"))
category = str
if age >= 6 and age <= 7 : 
    category = "poussin"
elif age >= 8 and age <= 9 :
    category = "Pupille"
elif age >= 10 and age <= 11 :
    category = "Minime"
else :
    category = "Cadet"
print("the category of the child is", category)