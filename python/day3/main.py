def read_file(): 
    batteries = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            batteries.append(line.strip())
    return batteries

def test():
    # should be 357..
    testcase = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
    total = joltage(testcase) 
    print(total)  

def joltage(batteries):
    total = 0
    for bat in batteries:
        bat = str(bat); length = len(bat); high: int = 0
        for i in range(0, len(bat) - 1):
            for j in range(i + 1, len(bat)):
                front = bat[i]
                back = bat[j]
                current = front + back
                if int(current) > high:
                    high = int(current)
        total += high 
    return total

def main():
    batteries = read_file()
    total = joltage(batteries)
    print(total)

if __name__ == "__main__":
    main()
    test()
