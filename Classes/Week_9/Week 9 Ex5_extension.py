# Generate 100 random coin flips
# Track total heads and total tails each flip
# Write a CSV file with a row for each flip

import csv, random, os

# Check if the file already exists
if os.path.exists("flips.csv"):
    is_file = "yes"
else:
    is_file = "no"

with open("flips.csv", "a") as file:
    writer = csv.writer(file, lineterminator = "\n")
    
    total_heads = 0
    total_tails = 0
    
    # Only write header row if this is a new file
    if is_file == "no":
        header = ["Flip number", "Heads/tails", "Total heads", "Total tails"]
        writer.writerow(header)
    
    for i in range(1, 101, 1):
        flip = random.randrange(1, 3)
        
        # Heads
        if flip == 1:
            total_heads = total_heads + 1
            output = [i, "Heads", total_heads, total_tails]
            writer.writerow(output)
            
        # Tails
        else:
            total_tails = total_tails + 1
            output = [i, "Tails", total_heads, total_tails]
            writer.writerow(output)
            
print("Complete!")