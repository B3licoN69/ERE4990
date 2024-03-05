import random

game_Play = []
total_Rolls = []
average = []
highest_Roll = []
sides = 6




dice = int(input("Dice: Enter the number of dice you want to play, Dice must exceed 4. "))

if (dice <= 4):
    print("You must enter a number higher than zero. Try again! ")
    quit()



roll = []
for i in range(0, dice):
    face = random.randint(1,sides)
    roll.append(face)

for i in range(0, dice):
    face = random.randint(1,sides)
    total_Rolls.append(face)
game_Play.append(dice)
total_Rolls.append(sum(total_Rolls) / len(total_Rolls))
highest_Roll.append(max(total_Rolls))

print(" Total Rolls: ", len(total_Rolls) - 1)
print(" Average Roll: ", sum(total_Rolls) / len(total_Rolls))
print(" Highest Roll: ", max(highest_Roll))
print(" Gameplay History: ", roll )

