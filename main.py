import random
from art import logo, vs
from data import data
import os

os.system('cls||clear')

a = random.randint(0, 49)
b = random.randint(0, 49)

score = 0

game_over = False

print(logo)
print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}.")
print(vs)
print(f"Against B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}.")
choice = input("Who has more followers? Type 'A' or 'B': ")

def lose():
    os.system('cls||clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    game_over = True
    
while not game_over:
    if choice == "A" or 'a':
        if data[a]['follower_count'] > data[b]['follower_count']:
            score += 1
            os.system('cls||clear')
            print(logo)
            print(f"You're right! Current score: {score}.")
            print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}.")
            print(vs)
            b = random.randint(0, 49)
            print(f"Against B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}.")
            choice = input("Who has more followers? Type 'A' or 'B': ")
        else:
            lose()
            break
    elif choice == "B" or "b":
        if data[a]['follower_count'] < data[b]['follower_count']:
            score += 1
            os.system('cls||clear')
            print(logo)
            print(f"You're right! Current score: {score}.")
            a = b
            print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}.")
            print(vs)
            b = random.randint(0, 49)
            print(f"Against B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}.")
            choice = input("Who has more followers? Type 'A' or 'B': ")
        else:
            lose()
            break