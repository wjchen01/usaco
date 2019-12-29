def small_list(places):
    pairings = []
    for num in range(1, len(places)):
        pairings.append([places[0], places[num]])
    return pairings


def cro_list(places):
    pairings = []
    for num in range(len(places)):
        pairings.extend(small_list(places[num:]))
    return pairings

def main():
    fin = open('gymnastics.in', 'r')
    fout = open('gymnastics.out', 'w')

    stats = list(map(int, fin.readline().strip().split()))
    game_number = stats[0]

    large_list = []
    for number in range(game_number):
        game_stats = list(map(int, fin.readline().strip().split()))
        large_list.extend(cro_list(game_stats))

    large_list = ['%i_%i' %(x[0], x[1]) for x in large_list]

    count = 0
    for num in set(large_list):
        if large_list.count(num) == game_number:
            count += 1

    fout.write(str(count) + '\n')

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()