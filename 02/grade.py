score = int(input("Enter Score"))
if score >=90:
    print("Grade: A")
if score >=80:
    print("Grade: B")
if score >=70:
    print("Grade: C")
if score >=60:
    print("Grade: D")
#if no elif used the if prints all matching print stmts
    ####################################

#score = int(input("Enter Score"))
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >=60:
    print("Grade: D")
else:
    print("F")