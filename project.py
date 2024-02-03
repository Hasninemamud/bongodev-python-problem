import os
files = os. listdir("submission")
submitted_roll = []
for file in files:
    div = file.split("_")
    roll = div[1]
    submitted_roll.append(roll)
try:
        while True:

            roll_to_check = input("Enter the roll to check: &  to quite enter q = ")

            if roll_to_check == "q":
                exit()

            if roll_to_check in submitted_roll:
                print(f"Roll: {roll_to_check} submit there assignment")
            else:
                print(f"Roll: {roll_to_check} not submit there assignment")
except Exception as e:
    print("Othrwise ok")

