# starter.py — Grade Tracker
# Project 2 | Easy | 25–30 minutes
#
# Run from this folder: SUDENAZ SOYTÜRK   GÜL İFDAL ALDEMİR
#   python starter.py

import csv
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "grades.csv"

# --- Step 1: Storage variables ---
scores = []
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

highest = {"name": "", "score": -1}
lowest = {"name": "", "score": 101}

# --- Step 2: Read the CSV ---
with open(csv_path, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:

        # TODO: Get the student's name and score from the row
        name = row["name"]
        score = int(row["score"])

        # TODO: Add the score to the scores list
        scores.append(score)

        # TODO: Update the highest score if needed
        if score > highest["score"]:
            highest["name"] = name
            highest["score"] = score

        # TODO: Update the lowest score if needed
        if score < lowest["score"]:
            lowest["name"] = name
            lowest["score"] = score

        # TODO: Determine the letter grade
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"

        # TODO: Increase the correct grade counter
        grade_counts[letter] += 1

# --- Step 3: Calculate average ---
# TODO: Calculate the class average
if len(scores) > 0:
    average = round(sum(scores) / len(scores), 1)
else:
    average = 0

# --- Step 4: Print the report ---
print("=== Quiz Grade Summary ===")
print(f"{'Total Students:':<20} {len(scores)}")
print(f"{'Average Score:':<20} {average}")
print(f"{'Highest Score:':<20} {highest['name']} ({highest['score']})")
print(f"{'Lowest Score:':<20} {lowest['name']} ({lowest['score']})")

print("\n--- Grade Distribution ---")
for grade in ["A", "B", "C", "D", "F"]:
    print(f"{grade}: {grade_counts[grade]}")

print("\n" + "-" * 30)