import manipulador
import pandas as pd

if __name__ == '__main__':
    tabela = pd.read_excel('planilha_final.xlsx')
    sas = manipulador.manipuladorTabela(tabela)

    while True:
        print("_-_-_Leitor de tabelas_-_-_")
        print("1- Adicionar linha na tabela")
        print("2- Exibir tabela")
        print("3- Atualizar linha na tabela")
        print("4- Excluir linha da tabela")
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        op_user = int(input("Digite a operação:\n"))

        if op_user == 1:
            sas.inserir_linha()
            break
        elif op_user == 2:
            sas.ler_tabela()
            break
        elif op_user == 3:
            sas.atualizar_linha()
            break
        elif op_user == 4:
            sas.excluir_linha()
            break
