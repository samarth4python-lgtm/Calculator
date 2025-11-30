print("Loaded")
n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))
e = str(input("Please enter what type of eqation you want to use: "))
if e == "addition":
    a = n1 + n2
    print(f"Your awnswer is {a})")
elif e =="multiplication":
    a = n1 * n2
    print(f"Your awnswer is {a}")
elif e =="subtraction":
    a = n1 - n2
    print(f"Your awnswer is {a}")
elif e == "division":
    a = n1 / n2
    print(f"Your awnswer is {a}")
else:
    print("Sorry,the math type you entered is not a math type in this file.Please go back to Calculator")

