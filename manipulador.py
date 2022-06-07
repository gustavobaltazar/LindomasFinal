import pandas as pd

class manipuladorTabela():
    def __init__(self, tabela):
        self.tabela = tabela

    def inserir_linha(self):
        df = pd.read_excel('planilha_final.xlsx', header=0).fillna("")
        data = pd.DataFrame
        df = df.convert_dtypes()

        column_names = ['Acao', 'Localizador', 'Descricao_Acao', 'Descricao_Localizador']
        baseDf = pd.DataFrame(columns=column_names)

        print("_-_-_Inserindo na tabela_-_-_")
        acao = int(input("Digite o número da ação: \n"))
        localizador = int(input("Digite o número do localizador: \n"))
        desc_acao = input("Digite a descrição da ação: \n")
        desc_localizador = input("Digite a descrição do localizador: \n")
        qtd = self.tabela['Acao'].count()
        self.tabela.loc[qtd + 1, 'Acao'] = acao
        self.tabela.loc[qtd + 1, 'Localizador'] = localizador
        self.tabela.loc[qtd + 1, 'Descricao_Acao'] = desc_acao
        self.tabela.loc[qtd + 1, 'Descricao_Localizador'] = desc_localizador
        self.tabela.to_excel('planilha_resultado.xlsx', index=False)

        inputDf = pd.DataFrame({'Acao': acao,
                                'Localizador': localizador,
                                'Descricao_Acao': desc_acao,
                                'Descricao_localizador': desc_localizador}, index=[0])

        baseDf = pd.concat([baseDf, inputDf], ignore_index=True)

        print(data(baseDf))

        updateDf = pd.concat([df, baseDf], ignore_index=True).replace(to_replace=pd.NA, value=None)
        headersList = ['Acao', 'Localizador', 'Descricao_Acao', 'Descricao_Localizador']
        print(data(updateDf[headersList]))

        updateDf.to_excel('planilha_resultado.xlsx', encoding='utf-8', index=False)

    def ler_tabela(self):
        print("_-_-_Exibindo Tabela_-_-_")
        print("1- Região")
        print("2- Unidade ornamentaria")
        print("3- Ação")
        print("4- Produto")
        op_usuario = int(input("Escolha uma operação: \n"))

        if op_usuario == 1:
            print(self.tabela[['Regiao', 'Descricao_Localizador']].head(100))
            op_user_pesquisa = int(input("Deseja pesquisar por região ou descrição do localizador?\n"
                                         "1- Região\n"
                                         "2- Descrição do localizador \n"))
            if op_user_pesquisa == 1:
                op_user_reg = input("Digite a informação que deseja localizar")
                pesquisa = self.tabela.loc[self.tabela['Regiao'] == op_user_reg].head(30)
                print(pesquisa['Regiao'])
            elif op_user_pesquisa == 2:
                op_user_desc_loc = input("Digite a informação que deseja localizar")
                pesquisa = self.tabela.loc[self.tabela['Descricao_Localizador'] == op_user_desc_loc].head(30)
                print(pesquisa['Descricao_Localizador'])

        elif op_usuario == 2:
            op_user_uni = int(input("Deseja pesquisar por Unidade orçamentaria ou Descrição da unidade?\n"
                                    "1- Unidade orçamentaria\n"
                                    "2- Descriçao da unidade\n"))
            if op_user_uni == 1:
                user_resp_uni = input("Digite a informação que deseja localizar")
                pesquisa2 = self.tabela.loc[self.tabela['Unidade_Orcamentaria'] == f'{user_resp_uni}'].head(30)
                print(pesquisa2['Unidade_Orcamentaria'])
            elif op_user_uni == 2:
                user_resp_desc = input("Digite a informação que deseja localizar\n")
                pesquisa2 = self.tabela.loc[self.tabela['Descricao_Unidade_Orcamentaria'] ==
                                            f'{user_resp_desc}'].head(30)
                print(pesquisa2['Descricao_Unidade_Orcamentaria'])

            print(self.tabela[['Unidade_Orcamentaria', 'Descricao_Unidade_Orcamentaria']].head(30))

        elif op_usuario == 3:
            op_user_ac = int(input("Deseja pesquisar por ação ou tipo de ação?\n"
                                   "1- Ação\n"
                                   "2- Tipo de ação\n"))
            if op_user_ac == 1:
                user_resp_acao = input("Digite a informação que deseja localizar:\n")
                pesquisa3 = self.tabela.loc[self.tabela['Acao'] == f'{user_resp_acao}'].head(30)
                print(pesquisa3['Acao'])
            elif op_user_ac == 2:
                user_resp_tip = input("Digite a informação que deseja localizar:\n")
                pesquisa3 = self.tabela.loc[self.tabela['Tipo_Acao'] == f'{user_resp_tip}'].head(30)
                print(pesquisa3['Tipo_Acao'])
            print(self.tabela[['Acao', 'Tipo_Acao']].head(30))
        elif op_usuario == 4:
            op_user_prod = int(input("Deseja pesquisar por produto ou tipo de crédito?\n"
                                     "1- Produto\n"
                                     "2- Tipo de crédito\n"))
            if op_user_prod == 1:
                user_resp_prod = input("Digite a informação que deseja localizar:\n")
                pesquisa4 = self.tabela.loc[self.tabela['Produto'] == f'{user_resp_prod}'].head(30)
                print(pesquisa4['Acao'])
            if op_user_prod == 2:
                user_resp_tip_cre = input("Digite a informação que deseja localizar:\n")
                pesquisa4 = self.tabela.loc[self.tabela['Tipo_Credito'] == f'{user_resp_tip_cre}'].head(30)
                print(pesquisa4['Tipo_Credito'])
            print(self.tabela[['Produto', 'Tipo_Credito']].head(30))

    def atualizar_linha(self):
        df3 = pd.read_excel('planilha_final.xlsx', header=0).fillna("")
        data3 = pd.DataFrame
        df3 = df3.convert_dtypes()

        column_names3 = ['Regiao', 'Unidade_Orcamentaria', 'Acao', 'Produto']
        baseDf3 = pd.DataFrame(columns=column_names3)

        print(df3)

        print("_-_-_Atualizando a planilha_-_-_")

        num = int(input("Digite um número para alterar na coluna região: \n"))
        num2 = int(input("Digite um número para alterar na coluna Unidade_Orcamentaria: \n"))
        num3 = int(input("Digite um número para alterar na coluna Ação: \n"))
        num4 = int(input("Digite um número para alterar na coluna Produto: \n"))

        print("O valor que será alterado na coluna região é esse: {}\n".format(self.tabela.loc[num, 'Regiao']))
        print("O valor que será alterado na coluna Unidade_Orcamentaria é esse: {}\n".format(self.tabela.loc[num2, 'Unidade_Orcamentaria']))
        print("O valor que será alterado na coluna Ação é esse: {}\n".format(self.tabela.loc[num3, 'Acao']))
        print("O valor que será alterado na coluna Produto é esse: {}\n".format(self.tabela.loc[num4, 'Produto']))

        user_troca = input("Digite o valor desejado para Região:\n")
        user_troca2 = input("Digite o valor desejado para Unidade_Orcamentaria:\n")
        user_troca3 = input("Digite o valor desejado para Ação:\n")
        user_troca4 = input("Digite o valor desejado para Produto:\n")

        self.tabela.loc[num, 'Regiao'] = user_troca
        self.tabela.loc[num2, 'Unidade_Orcamentaria'] = user_troca2
        self.tabela.loc[num3, 'Acao'] = user_troca3
        self.tabela.loc[num4, 'Produto'] = user_troca4

        print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num, 'Regiao']))
        print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num2, 'Unidade_Orcamentaria']))
        print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num3, 'Acao']))
        print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num4, 'Produto']))

        inputDf3 = pd.DataFrame({'Regiao': user_troca,
                                'Unidade_Orcamentaria': user_troca2,
                                'Acao': user_troca3,
                                'Produto': user_troca4}, index=[0])

        baseDf3 = pd.concat([baseDf3, inputDf3], ignore_index=True)

        updateDf3 = pd.concat([baseDf3, df3], ignore_index=True).replace(to_replace=pd.NA, value=None)

        headersList3 = ['Regiao', 'Unidade_Orcamentaria', 'Acao', 'Produto']
        print(data3(baseDf3[headersList3]))

        updateDf3.to_excel('planilha_resultado.xlsx', encoding='utf-8', index=False)

    def excluir_linha(self):
        df2 = pd.read_excel('planilha_final.xlsx', header=0).fillna("")
        data2 = pd.DataFrame(df2)
        print("_-_-_Excluindo da Linha_-_-_")
        op_user2 = int(input("Escolha qual linha deseja excluir:\n"))
        data2 = data2.drop([op_user2], axis=0)
        print(data2)
        data2.to_excel('planilha_resultado.xlsx', encoding='utf-8', index=False)

