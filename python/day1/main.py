position = 50
zeros = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
    
        direction = line[0]
        distance = int(line[1:])
        step = 1 if direction == "R" else -1
        
        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zeros += 1 
print(zeros)
