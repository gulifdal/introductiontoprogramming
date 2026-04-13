# starter.py — Event Log Reporter
# Project 3 | Intermediate | 35–45 minutes
#
# Run from this folder: Gül İfdal Aldemir - Sudenaz Soytürk - Yunus Enmre Ekici
#   python starter.py

import csv

# --- Step 1: Set up storage variables -----------------------
bookings = []
event_counts = {}

# --- Step 2: Read the CSV
with open("bookings.csv", "r") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    reader.fieldnames = [field.strip() for field in reader.fieldnames]

    for row in reader:
        # TODO: Get the event name from the row
        event_name = row.get ("event" , row.get ("Event" , "Unknown")).strip()

        # TODO: Append event name to the bookings list
        bookings.append(event_name)

        # TODO: Increment the count for this event in event_counts
        if event_name in event_counts:
            event_counts[event_name] += 1
        else:
            event_counts[event_name] = 1

# --- Step 3: Analyze the data -------------------------------
# TODO: Calculate total_bookings, most_popular, and least_popular
total_bookings = len(bookings)

if event_counts:
    most_popular = max(event_counts, key=event_counts.get)
    least_popular = min(event_counts, key=event_counts.get)
else:
    most_popular = "None"
    least_popular = "None"

# --- Step 4: Print the report -------------------------------
print("=== event Booking Analysis ===")
print(f"{'Total Bookings:':<20} {total_bookings}")
print(f"{'Most Popular:':<20} {most_popular} ({event_counts.get(most_popular,0)} bookings)")
print(f"{'Least Popular:':<20} {least_popular} ({event_counts.get(least_popular,0)} bookings)")

print("\n--- Bookings per Event ---")
for event, count in event_counts.items():
    print(f"{event:<20}: {count}")

print("\n" + "-" * 30)
