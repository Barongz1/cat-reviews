"""Make the AI Judge Laugh: Cat Reviews Its Human — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one funny one-star review, under 200 characters, from a house cat about its human.
"""
import os

LINE = "One star. He wakes me at 6 AM to feed me, then complains that I woke him up at 6 AM. The audacity is unreal."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
