def merge_2(first, second):
    new_list = []
    merge_list = []
    for cow in second:
        second_num = second.index(cow)
        if cow in first:
            first_num = first.index(cow)
            if first_num > 0:
                merge_list.extend(first[0:first_num])
                merge_list.extend(cow)
                if second_num == 0:
                    merge_list.extend(second[second_num + 1:])
                else:
                    merge_list.extend(second[0:second_num])
            elif second_num == 0 and first_num == 0:
                merge_list = first[::-1]
                merge_list.extend(second[1:])
    if not merge_list:
        new_list.append(first)
        new_list.append(second)
    else:
        new_list.append(merge_list)
    return new_list


fin = open('lineup.in', 'r')
fout = open('lineup.out', 'w')

cow_names = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
cow_names.sort()
line_number = fin.readline().strip()

restraints = []
for line in fin:
    input = line.strip()
    order = input.split(' must be milked beside ')
    order.sort()
    restraints.append(order)

restraints.sort()

final_list = []

def merge_list(a_list):
    if len(a_list) == 1:
        final_list.extend(a_list)
    elif len(a_list) == 2:
        new_list = merge_2(a_list[0], a_list[1])
        final_list.extend(new_list)
    else:
        new_list = merge_2(a_list[0], a_list[1])
        if len(new_list) > 1:
            partial_list = []
            partial_list.append(new_list[1])
            partial_list.extend(a_list[2:])
            final_list.append(new_list[0])
        else:
            partial_list = new_list
            partial_list.extend(a_list[2:])
        merge_list(partial_list)
    return final_list

merge_list(restraints)

for cow in cow_names:
    if not any([cow in relation for relation in final_list]):
        final_list.append([cow])

new_list = sorted(final_list, key=lambda x: x[0])

for relation in new_list:
    for cow in relation:
        fout.write(cow + "\n")

fin.close()
fout.close()
