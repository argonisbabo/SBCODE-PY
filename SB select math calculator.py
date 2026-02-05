select = 0
fun = 0
a = 0
b = 0

print("multiply : 1, add : 2, minus : 3")
select = (int(input("What do you want function of math? : ")))

if select == 1:
    print("Please enter about number for multiply")
    a = int(input("first number : "))
    b = int(input("second number : "))
    print(f"{a} multiply {b} is {a * b}")
elif select == 2:
    print("Please enter about first number for add")
    a = int(input("first number : "))
    b = int(input("second number : "))
    print(f"{a} add {b} is {a + b}")
else:
    print("Please enter about first number for minus")
    a = int(input("first number : "))
    b = int(input("second number : "))
    print(f"{a} minus {b} is {a - b}")
    
    #made by seungbeom. Mon Feb 2 / 2026 / 9 : 50 am at school.

