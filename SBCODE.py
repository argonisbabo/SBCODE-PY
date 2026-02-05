#This is my first password system for website

print("This is Terminal website for practice")
print("Sign up : 1 , Login : 2 , Exit : 3")

sort = int(input("Please enter what do you want : "))
useridck = 0
userpwck = 0

while True:
    if sort == 1:
        print("This is sign up page.")
        userid = input("Please enter your ID : ")
        userpw = input("Please enter your password : ")
        print("Welcome! Now you can login on the website.")
        print(" ")
        print("This is Terminal website for practice")
        print("Sign up : 1 , login : 2 , exit : 3")
        sort = int(input("Please enter what do you want : "))
    elif sort == 2:
        print("This is login page.")
        useridck = input("Please enter your ID : ")
        userpwck = input("Please your password : ")
        if userid == useridck and userpw == userpwck:
            print(f"Welcome! ID : {useridck}")
            break
        elif userid != useridck or userpw != userpwck:
            print("Your ID or Password something has wrong!")
    else:
        print("Close the terminal website.")
        break
    
#made by SB Wed/Feb/4/2026 10:04am / Sign up and Login system!!! I think this is wonderful system to me.
