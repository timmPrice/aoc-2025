def read_file(path: str):
    ranges = []
    with open(path, "r") as file:
        ranges = file.readline().strip().split(",")
        
    return ranges

def trav_pattern(ranges):
    total = 0
    for r in ranges:
        a, b = r.split("-")
        a = int(a); b = int(b)
        while a <= b: 
            # s = str(a)
            # if len(s) % 2 == 0:
            #     mid: int = len(s) // 2
            #     if s[:mid] == s[mid:]:
            #         total += a
            if is_valid(str(a)):
                total += a
            a += 1
    return total

def is_valid(a: str) -> bool:
    return a in (a + a)[1:-1]


def main(): 
    ranges = read_file("input.txt")
    total = trav_pattern(ranges)
    print(total)

if __name__ == "__main__":
    main()
