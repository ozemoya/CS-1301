import sys
pirates = {}

if len(sys.argv) > 1:
    fname = sys.argv[1]
    
else:
    fname = "onepiece.dat"
    
with open('onepiece.dat', "r") as f:
    for line in f:
        pirate, crew, Beri, df, Status = line.strip().split(':')
        pirates.append((pirate, crew, Beri, df, Status))
        print(line)
    