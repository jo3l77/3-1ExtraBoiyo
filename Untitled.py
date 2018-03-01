'''

import random

def randNum()
'''
'''
rand1= random.randint(1,6)
rand2= random.randint(1,6)
print(rand1, rand2)
'''
'''
     for i in range(3):
	 print(random.randint(1,6))

randNum()


tries=0

while True:
  
   if tries<6:
       for i in range(3):
           print(random.randint(1,6))
           tries = tries+1
   else:
      break


'''
'''
import random


name = input("Enter your name:")
print(name, "I am thinking of a number between 1 and 500. Can you guess the number?:")

computer_number = random.randint(1,501)

total_guesses = 0

while total_guesses<8:
     guess= int(input("Enter your guess:")
     total_guesses = total_guesses+1
     if guess<computer_number:
        print("The number I am thinking of is higher.")
     elif guess> computer_number:
        print("The number I am thinking of is lower.")
     elif guess = computer_number:
        print("Good Job! You guessed the number in ", total_guesses, "attempts.")
	break
     
     if total_guesses == 8:
	print("Sorry, you ran out of guesses.")

# College Choices  import random

def getAnswer(answerNumber):
    if answerNumber==1:
	return "NYU"
    
    elif answerNumber== 2:
       return "Stony Brook University"

0
while tries <10:
   userInput = input("What college will I go to?")
   if userInput==1:
	print(getAnswer(random.randint(1,11)))
   if userInput==2:
        print(getAnswer(random.randint(1,11)))
   if userInput==3:
	print(getAnswer(random.randint(1,11)))
   if userInput==4:
	print(getAnswer(random.randint(1,11)))
   if userInput==5:
	print(getAnswer(random.randint(1,11)))
   if userInput==6:
	print(getAnswer(random.randint(1,11)))
   if userInput==:7
	print(getAnswer(random.randint(1,11)))
   if userInput==8:
	print(getAnswer(random.randint(1,11)))
   if userInput==9:
	print(getAnswer(random.randint(1,11)))
   if userInput==10:
	print(getAnswer(random.randint(1,11)))
   tries = tries +1
'''

#Vacations Cost

#functions and parameters example


def hotel_cost(days):
   userInput= int(input("How many days do you plan to stay?"))
   return (90*days)

def plane_ride_cost(city):
    userInput= input("Enter which city you want to travel to: ")
    if city == "Charlotte":
        return(185)
    elif city=="Tampa":
        return(220)
    elif city=="Pittsburgh":
        return(175)

def rental_car_cost(days):
    cost=40*days
    if days>7:
        cost = cost-40
    elif days>=3 and days<7:
        cost=cost-20
    return cost


def trip_cost(days,city,spending_money):
    return hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city)+spending_money

print(trip_cost(6,"Tampa",2000))
