
print("***************************Question 1*****************************")
# 1. Write a Python function is_multiple(x,y) which returns True if x is a multiple of y and False if
# x is NOT a multiple of y.
def is_multiple(x, y):
   if x and y % x == 0:
    return True
   else:
    return False
x = int(input("enter a number {X}:"))
y = int(input("enter its multiple {Y}:"))
print(is_multiple(x,y))


# 2. Write a Python function sum_squares(x) which returns the sum of all squares from 0 up to
#and including the square of x (do not use the Math module for this question).
#def sum_squares(x):
print("***************************Question 2*****************************")
def sum_squares(x):
    sum = 0
    for i in range(1,x+1):
     sum += (i*i)
    return "Sum of Squares: "+ str(sum)
x = int(input("Enter a number: "))
print(sum_squares(x))


# 3. Write the Python function create_list(x,y) which returns a list containing x0 up to xy
# . E.g create_list(2,8) returns the list [1,2,4,8,16,32,64,128,256] ie [20, 21, 22, 23, 24, 25, 26, 27
# , 28].
# Be sure to use a loop and NOT just make an assignment.
print("***************************Question 3*****************************")
def create_list(x, y):
    mylist = []
    mylist.append(1)
    number = 1
    for i in range(1, y + 1):
        number = number * x
        mylist.append(number)
    return mylist
x = int(input("X: "))
y = int(input("Y: "))
print(create_list(x, y))


print("***************************Question 4*****************************")
# 4.Write a Python function num_vowels(text) which will return the number of vowels in the string “text”
def num_vowels(text):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in text:
        if char in vowels:
            count = count + 1
    return "Number of vowels: " + str(count)
text = input("Enter a string: ")

text = text.lower()
print(num_vowels(text))


# 5. Write a Python function distinct(data) which returns True if the letters in data are different
# and False if they are not.
print("***************************Question 5*****************************")
def distinct(data):
    if len(set(data.lower())) == len(data):
        return True
    else:
         return False

data =input("Enter a string: ")
print(distinct(data))
print("***************************THE END*****************************")
