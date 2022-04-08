from ProcessLoopFor import ProcessLoop

MENU = """
    MENU
    1 - range(1000, 10000, 100)
    2 - range(1000, 6000, 100)
    3 - range(100, 600, 100)
    4 - range(10, 60, 10)
    5 - range(1000000, 6000000, 100000)
    6 - Sair
""" 

cases = {
    '1': range(1000, 10000, 100),
    '2': range(1000, 6000, 100),
    '3': range(100, 600, 100),
    '4': range(10, 60, 10),
    '5': range(1000000, 6000000, 100000)
}

def main():
    is_running = True
    print(MENU)
    while(is_running):
        case = input("Digite o número do caso: ").strip()
        if(case in cases.keys() or case == '6'):
            processLoop = ProcessLoop(cases[case], case)
            processLoop.run()
        else:
            print("Opção não existente! tente novamente: ")

if __name__ == '__main__':
    main()