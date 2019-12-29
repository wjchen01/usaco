def is_unique(farm_number, colors):
    unique = False
    start = 0
    while True:
        if start + farm_number < len(colors) + 1:
            code = colors[start:start+farm_number]
            if colors.count(code) > 1:
                break
            else:
                start += 1
        else:
            break
    if start == len(colors) - farm_number + 1:
        unique = True
    return unique


fin = open('whereami.in', 'r')
fout = open('whereami.out', 'w')

farm_number = int(fin.readline().strip())
farms = fin.readline().strip()

for number in range(1, farm_number + 1):
    if is_unique(number, farms):
        fout.write(str(number) + "\n")
        break

fin.close()
fout.close()
