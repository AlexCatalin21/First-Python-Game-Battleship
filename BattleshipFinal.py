from prettytable import PrettyTable
hitsP1 = 0
hitsP2 = 0

a1 = [[0, 1, 2, 3, 4, 5, 6],
      ['A', '', '', '', '', '', ''],
      ['B', '', '', '', '', '', ''],
      ['C', '', '', '', '', '', ''],
      ['D', '', '', '', '', '', ''],
      ['E', '', '', '', '', '', ''],
      ['F', '', '', '', '', '', '']]
a2 = [[0, 1, 2, 3, 4, 5, 6],
      ['A', '', '', '', '', '', ''],
      ['B', '', '', '', '', '', ''],
      ['C', '', '', '', '', '', ''],
      ['D', '', '', '', '', '', ''],
      ['E', '', '', '', '', '', ''],
      ['F', '', '', '', '', '', '']]
b1 = [[0, 1, 2, 3, 4, 5, 6],
      ['A', '', '', '', '', '', ''],
      ['B', '', '', '', '', '', ''],
      ['C', '', '', '', '', '', ''],
      ['D', '', '', '', '', '', ''],
      ['E', '', '', '', '', '', ''],
      ['F', '', '', '', '', '', '']]
b2 = [[0, 1, 2, 3, 4, 5, 6],
      ['A', '', '', '', '', '', ''],
      ['B', '', '', '', '', '', ''],
      ['C', '', '', '', '', '', ''],
      ['D', '', '', '', '', '', ''],
      ['E', '', '', '', '', '', ''],
      ['F', '', '', '', '', '', '']]


def createTable(list):
    x = PrettyTable()
    x.hrules = True
    x.header = False
    x.add_column('q', list[0], 'c')
    x.add_column('q', list[1], 'c')
    x.add_column('q', list[2], 'c')
    x.add_column('q', list[3], 'c')
    x.add_column('q', list[4], 'c')
    x.add_column('q', list[5], 'c')
    x.add_column('q', list[6], 'c')
    print(x)


def placement(list):
    ship = 3
    while ship > 0:
        orientation = input(
            'Select orientation: H for horizontal, V for vertical: ')
        a = input('Select a position from the column starting from A to F: ')
        if a == 'A' or a == 'a':
            a = 1
        elif a == 'B' or a == 'b':
            a = 2
        elif a == 'C' or a == 'c':
            a = 3
        elif a == 'D' or a == 'd':
            a = 4
        elif a == 'E' or a == 'e':
            a = 5
        elif a == 'F' or a == 'f':
            a = 6
        b = int(input('Select a position from the line starting from 1 to 6: '))
        if (orientation == 'v' or orientation == 'V') and (b == 1 or b == 6):
            print('You are out of border')
        elif (orientation == 'h' or orientation == 'H') and (a == 1 or a == 6):
            print('You are out of border')
        else:
            if orientation == 'h' or orientation == 'H':
                list[a][b] = chr(164)
                list[a - 1][b] = chr(164)
                list[a + 1][b] = chr(164)
            if orientation == 'v' or orientation == 'V':
                list[a][b] = chr(164)
                list[a][b + 1] = chr(164)
                list[a][b-1] = chr(164)
            ship = ship - 1
            createTable(list)


def attack(placeList: list, showList: list):
    global hitsP1
    global hitsP2
    a = input('Attack a position from the column starting from  A to F: ')
    if a == 'A' or a == 'a':
        a = 1
    elif a == 'B' or a == 'b':
        a = 2
    elif a == 'C' or a == 'c':
        a = 3
    elif a == 'D' or a == 'd':
        a = 4
    elif a == 'E' or a == 'e':
        a = 5
    elif a == 'F' or a == 'f':
        a = 6
    b = int(input('Attack a position from the line starting from 1 to 6: '))

    if placeList[a][b] == chr(164):
        showList[a][b] = chr(164)
        placeList[a][b] = 0
        print('You hit a piece of boat')
        createTable(showList)
        if placeList == b1:
            hitsP1 = hitsP1 + 1
        else:
            hitsP2 = hitsP2 + 1
    elif placeList[a][b] == 0 or showList[a][b] == 'x':
        print('Already hit')

    else:
        print('Nothing here!')
        showList[a][b] = 'x'
        createTable(showList)


print("Placement phase for Player1")
placement(a1)
print('.\n' * 20)
print("Placement phase for Player2")
placement(b1)
print('.\n' * 20)


while hitsP1 < 9 and hitsP2 < 9:
    print("Player1 attack")
    attack(b1, b2)
    print("Hits of Player1:", hitsP1)
    if hitsP1 == 9:
        print('Player1 won')
    else:
        print("Player2 attack")
        attack(a1, a2)
        print("Hits of Player2:", hitsP2)
        if hitsP2 == 9:
            print('Player2 won')