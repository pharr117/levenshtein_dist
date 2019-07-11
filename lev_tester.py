import random
from levenshtein_dist import *

def main():
    file = open("10k.txt", "r")
    lines = []
    lines = file.read()
    lines = lines.split("\n")
    file.close()
    combos = []
    for x in range(100):
        combos.append((random.choice(lines), random.choice(lines)))

    for combo in combos:
        rec = levenshtein_dist_rec(*combo)
        dp = levenshtein_dist_dp(*combo)
        if rec != dp:
            print("\n\nError, mismatch...")
        print("Recursive: " + str(combo) + " " + str(rec))
        print("Dynamic: " + str(combo) + " " + str(dp))
        if rec != dp:
            print("\n")
if __name__ == "__main__":
    main()
