n = 0
Sum = 0
num = input("Please enter a number: ") num = int(num)
minimum = num while (num != -1):
n = n + 1
if (minimum >= num):
minimum = num Sum += num
num = input("Enter the next number: ") num = int(num)
if (n == 0):
print("Minimum = -1 \nAverage = -1")
 
else:
 print ("The number of inputs are " + str(n) + ".") print ("The minimum number is " + str(minimum)+ ".")
print ("The summation of all numbers is " + str(Sum) + ".") print ("Average is " + str(Sum / n))

'# it looks like I learned how to use git today',
