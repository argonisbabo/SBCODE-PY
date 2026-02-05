score = 0
absence = 0

print("Smart Score Calculator V1")
score = int(input("What is your score? : "))
absence = int(input("How many absence you did? : "))

if absence >= 5:
    print("Fail (Sorry. Too many absences.)")
elif score >= 90 and absence <= 2:
    print("Your Grade is : A")
elif score >= 80:
    print("Your Grade is : B")
elif score >= 70:
    print("Your Grade is : C")
elif score < 70:
    print("Your Grade is : F")
else :
    print("Please do more study..")
    
# I made School grade Calculator at the school! Mon / Feb / 2 / 2026 / 10 : 08 am (SB)