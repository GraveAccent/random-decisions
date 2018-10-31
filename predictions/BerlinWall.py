#!/usr/bin/env python3
# How many years will the Berlin Wall still exist?
# The program below is trying to make a prediction from a single data point.
print("Please imagine that the current time is before 1989.")
answer = input("What year is this year?\n")
year = int(answer)
diff = year - 1961
print("The Berlin Wall will still exist", diff, "years.")
