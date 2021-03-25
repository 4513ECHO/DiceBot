import yacc

def main():
    while True:
        try:
            data = input("[DiceBot]> ")
        except EOFError:
            break
        result = yacc.parse(data)
        print("  [%s] -> " % data + str(result))

main()
