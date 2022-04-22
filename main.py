from processPecuaria import ProcessPecuaria

MENU = """
    MENU
    1 - Gerar dados de Pecuaria
    2 - Sair
"""

def main():
    is_running = True
    print(MENU)
    while(is_running):
        case = input("Digite uma opção: ").strip()
        if(case == '1'):
            ano = input('Gerar dados com base de qual ano(2009 a 2020): ').strip()
            while(int(ano) not in range(2009, 2021)):
                ano = input('Ano inválido, por favor digite um ano entre 2009 e 2020: ').strip()
            mes = input('Gerar dados de qual mês(1 a 12): ').strip()
            while(int(mes) not in range(1, 13)):
                mes = input('Mês inválido, por favor digite um mês entre 1(Janeiro) e 12(Dezembro): ').strip()
            processLoop = ProcessPecuaria(ano, mes)
            processLoop.run()
        elif(case == '2'):
            print("Obrigado!")
            is_running = False
        else:
            print("Opção não existente! tente novamente: ")

if __name__ == '__main__':
    main()