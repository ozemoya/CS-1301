import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]
    
else:
    fname = "in.dat"
    

def t_to_minutes(time_str):
    hours, minutes = map(int, time_str[:-2].split('.'))
    return (hours % 12 + 12 * ('PM' in time_str)) * 60 + minutes

def read_data(fname):
    with open(fname, "r") as f:
        data = f.read().splitlines()
    return data

with open('in.dat', 'r') as f:
    for line in f:
        if not line.startswith("#"):
            print(line)
       




data = read_data(fname)

total_steps, total_duration = 0, 0

for line in data:
    if line.startswith("#"):
        continue

    try:
        start_time_str, end_time_str, steps_str = line.split(':')
        start_time, end_time = map(t_to_minutes, [start_time_str, end_time_str])

        if end_time < start_time:
            print("INVALID data:", line.strip())
            continue

        
        total_duration += end_time - start_time
        
        total_steps += int(steps_str)
    except ValueError:
        print("Error processing line:", line.strip())

print("\nTotal steps:", total_steps)
if total_duration == 0:
    print("No valid data to calculate hourly steps rate.")
else:
    print("Hourly steps rate:", total_steps * 60 // total_duration)
