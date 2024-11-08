# Problem 1: Student Grade Catergorization

# Make them a variable
score = []
score_count = 0 # Used to count how many times

#Use while loop = true to stop when it isnt true
while True:
    score = input("Enter a integer score: ")
    score_count += 1 # Adds 1 to every time you input a score
    if score >= "90": # Use scores to categorize the score
        print("Excellent")
    elif score >= "70":
        print("Good")
    elif score >= "50":
        print("Pass")
    else:
        print("Fail")
        if score < "0":
            break # Stops the program when negative 
print(f"Score count: {score_count}") # Prints amount of scores inputed




# Problem 2: Even and Odd Counter with Conditions

# prompts user to enter a starting and ending number
sNum = int(input("Give me a starting number: "))
eNum = int(input("Give me an ending number: "))

import math

countE = 0
countO = 0

for num in range(sNum, eNum): # puts the inputtted numbers into a list and is gone through until the ending number
    if num % 2 == 0 and num > 10: # finds a number with the specifications
        print(f"special even: {num}") # prints each speical even number
        countE += 1 
    if num % 2 == 1 and num < 20: # finds a number with the specifications
        print(f"special odd: {num}") # prints each speacial odd number
        countO += 1

print(f"Total amount of special even #'s: {countE}") # prints the total amounts of speacil even numbers
print(f"Total amount of special odd #'s: {countO}") # prints the total amount of speacil even numbers
