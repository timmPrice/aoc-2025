def read_file(): 
    batteries = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            batteries.append(line.strip())
    return batteries

def test():
    # should be 357..
    testcase = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    total = joltage(testcase)
    total2 = max_joltage(testcase)
    print(total)
    print(total2)

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

def max_joltage(batteries):
    total = 0
    k = 12
    for bat in batteries:
        n = len(bat)
        remove = n - k 
        stack = []

        for ch in bat:
            while remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                remove -= 1
            stack.append(ch)

        if remove > 0:
            stack = stack[:-remove]
        
        best: str = "".join(stack[:k])
        total += int(best)
    return total

def main():
    batteries = read_file()
    total = joltage(batteries)
    total2 = max_joltage(batteries)
    
    print(total)
    print(total2)

if __name__ == "__main__":
    main()
    test()
