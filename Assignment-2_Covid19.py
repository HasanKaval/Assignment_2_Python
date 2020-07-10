age = (input("Are you a cigarette addict older than 75 years old? yes/no : ")).lower().strip(" ") == "yes"
chronic = (input("Do you have a severe chronic disease? yes/no : ")).lower().strip(" ") == "yes"
immune = (input("Is your immune system too weak? yes/no : ")).lower().strip(" ") == "yes"
if age or chronic or immune:
    print("You are in risky group")
else:
    print("You are not in risky group")
