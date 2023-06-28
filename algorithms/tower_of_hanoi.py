def hanoi(tower_list, pile_list, disk_number):
    cnt = 0
    passed_list = [tower_list[:]]

    while True:

        for disk in range(1, disk_number+1):

            #If the current disk is not on the top of the stake, move to the next disk
            if tower_list.index(tower_list[disk-1]) != disk-1:
                continue

            idx = pile_list.index(tower_list[disk-1])

            #Clockwise-> center -> right -> left ...Turn in the order of)
            if (disk_number % 2 == 0 and disk % 2 == 1) or (disk_number % 2 == 1 and disk % 2 == 0) :

                if idx+1 >= len(pile_list):
                    idx = -1

                if pile_list[idx+1] not in tower_list or tower_list.index(pile_list[idx+1]) > disk-1:
                    tower_list[disk-1] = pile_list[idx+1]
                    passed_list.append(tower_list[:])
                    cnt += 1


            #Counterclockwise-> right -> center -> left ...Turn in the order of)
            else:

                if 0 >= idx:
                    idx = len(pile_list)

                if pile_list[idx-1] not in tower_list or tower_list.index(pile_list[idx-1]) > disk-1:
                    tower_list[disk-1] = pile_list[idx-1]
                    passed_list.append(tower_list[:])
                    cnt += 1

            if tower_list == ['r'] * disk_number:
                return cnt, passed_list

if __name__ == '__main__':
    disk_number = int(input())
    pile_list = ['l', 'c', 'r']
    tower_list = ['l'] * (disk_number)

    cnt, passed_list = hanoi(tower_list, pile_list, disk_number)

    print(passed_list)