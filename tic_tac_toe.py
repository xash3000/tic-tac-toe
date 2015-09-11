#!/usr/bin/python3.4

import random
import time

arr = [1,2,3,4,5,6,7,8,9]

def printGrid(a):
    #don't change this , be carefu
    print('''




    ''')
    print(a[0], '      |', a[1], '      |', a[2])
    print('        |         |')
    print('-------------------------')
    print(a[3], '      |', a[4], '      |', a[5])
    print('        |         |')
    print('-------------------------')
    print(a[6], '      |', a[7], '      |', a[8])
    print('        |         |')
    print('''






    ''')

def whoStart():
    return random.choice([1,0])


def symbolForPlayers():
    return random.choice(['X','O'])

def isSomeOneWin(arr, sym):
    return ((arr[0] == sym  and arr[1] == sym and arr[2] == sym) or
    (arr[3] == sym and arr[4] == sym and arr[5] == sym) or
    (arr[6] == sym and arr[7] == sym and arr[8] == sym) or
    (arr[0] == sym and arr[3] == sym and arr[6] == sym) or
    (arr[1] == sym and arr[4] == sym and arr[7] == sym) or
    (arr[2] == sym and arr[5] == sym and arr[8] == sym) or
    (arr[0] == sym and arr[4] == sym and arr[8] == sym) or
    (arr[2] == sym and arr[4] == sym and arr[6] == sym)
    )


def isBoardFull(arr):
    return all([arr[i] != i+1 for i in range(len(arr) - 1)])

def isGameover(sym1,sym2,player1,player2):
    global arr

    if isSomeOneWin(arr, sym1):
        print('{} is the winner'.format(player1))
        return True
    if isSomeOneWin(arr, sym2):
        print('{} is the winner'.format(player2))
        return True
    if isBoardFull(arr):
        print('GAME OVER')
        return True
    return False


def main():
    global arr
    player1 = input('Enter player1 name : ')
    player2 = input('Enter player2 name : ')
    sym1 = symbolForPlayers()
    if sym1 == 'X':
        sym2 = 'O'
    else:
        sym2 = 'X'
    print('{} is {}       {} is {}'.format(player1, sym1, player2, sym2))
    time.sleep(1)
    firstMove = whoStart()
    if firstMove == 0:
        print('{} will start first'.format(player1))
        while True:

            isGameover(sym1,sym2,player1,player2)
            if isGameover(sym1,sym2,player1,player2):
                break

            printGrid(arr)

            #player1 turn
            print('it\'s {} turn'.format(player1))
            p1c = int(input('Choose number from 1 to 9 : '))
            while arr[p1c - 1] == 'X' or arr[p1c - 1] == 'O':
                p1c = int(input('Look at the board and Choose number from 1 to 9 : '))
            arr[p1c - 1] = sym1

            isGameover(sym1,sym2,player1,player2)
            if isGameover(sym1,sym2,player1,player2):
                break

            printGrid(arr)

            #player2 turn
            print('it\'s {} turn'.format(player2))
            p2c = int(input('Choose number from 1 to 9 : '))
            while arr[p2c - 1] == 'X' or arr[p2c - 1] == 'O':
                p2c = int(input('Look at the board and Choose number from 1 to 9 : '))
            arr[p2c - 1] = sym2


    if firstMove == 1:
        while True:
            isGameover(sym1,sym2,player1,player2)
            if isGameover(sym1,sym2,player1,player2):
                break

            printGrid(arr)

            #player2 turn
            print('it\'s {} turn'.format(player2))
            p2c = int(input('Choose number from 1 to 9 : '))
            while arr[p2c - 1] == 'X' or arr[p2c - 1] == 'O':
                p2c = int(input('Look at the board and Choose number from 1 to 9 : '))
            arr[p2c - 1] = sym2

            isGameover(sym1,sym2,player1,player2)
            if isGameover(sym1,sym2,player1,player2):
                break

            printGrid(arr)

            #player1 turn
            print('it\'s {} turn'.format(player1))
            p1c = int(input('Choose number from 1 to 9 : '))
            while arr[p1c - 1] == 'X' or arr[p1c - 1] == 'O':
                p1c = int(input('Look at the board and Choose number from 1 to 9 : '))
            arr[p1c - 1] = sym1

    again = input('do you want to play again : ')
    if again.lower()[0] == 'y':
        arr = [1,2,3,4,5,6,7,8,9]
        main()


if __name__ == '__main__':
    main()
