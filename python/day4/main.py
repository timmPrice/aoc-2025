grid = [list(line.strip()) for line in open("input.txt") if line.strip()]

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

rows = len(grid)
cols = len(grid[0])

total = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue
        count = 0
        for row_dir, col_dir in dirs:
            row_nrom, col_nrom = r + row_dir, c + col_dir
            if 0 <= row_nrom < rows and 0 <= col_nrom < cols and grid[row_nrom][col_nrom] == "@":
                count += 1
        if count < 4:
            total += 1

print(total)
