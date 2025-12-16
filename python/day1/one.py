def test_turn(): 
    dial = 50; passes = 0; zeros = 0;
    inputs = [50, 210]
    for i in inputs:
        if i % 2 == 0:
            direction = True
        else:
            direction = False
        dial, cur_passes, cur_zeros = turn(dial, i, direction)
        print(f"{dial}")
        passes += cur_passes
        zeros += cur_zeros 

    print(f"new dial: {dial}, passes: {passes}, zeros: {zeros}")

def turn(dial: int, amount: int, direction: bool):
    zeros = 0

    if direction:
        new_dial = (dial + amount) % 100
        if (new_dial > 99 or new_dial < 0):
            raise ValueError("DIAL OUT OF BOUNDS")
        elif (new_dial == 0):
            zeros = zeros + 1
        passes = (dial + amount) // 100
    else:
        new_dial = (dial - amount) % 100
        if (new_dial > 99 or new_dial < 0):
            raise ValueError("DIAL OUT OF BOUNDS")
        elif (new_dial == 0):
            zeros = zeros + 1
        passes =  abs((dial - amount) // 100)
    
    return new_dial, passes, zeros

def main():
    dial = 50; passes = 0; zeros = 0;

    with open("input.txt", "r") as file:
        for line in file.readlines():
            if line[0] == "R":
                dial, cur_passes, cur_zeros = turn(dial, int(line[1:]), True)
            elif line[0] == "L":
                dial, cur_passes, cur_zeros = turn(dial, int(line[1:]), False)
            else: 
                raise ValueError("PARSED INCORRECTLY")
             
            passes += cur_passes
            zeros += cur_zeros 

    print(f"new dial: {dial}, passes: {passes}, zeros: {zeros}")

# not 6504
if __name__ == "__main__":
    main()
    test_turn()
