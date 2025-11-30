import time
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = compute_lcm(num1, num2)
print("The LCM of ",num1," and ",num2," is ",lcm)

def gcf(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
gcf = gcf(num1, num2)
print("The G.C.F. is",gcf)
time.sleep(5)
print("Sending you to calculator")
