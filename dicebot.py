import diceparse

if __name__ == '__main__':
    while True:
        try:
            i = input('[DiceBot]> ')
        except EOFError:
            break
        print(diceparse.dicebot(i))
