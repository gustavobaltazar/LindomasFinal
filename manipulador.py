import pandas as pd


class manipuladorTabela():
	def __init__(self, tabela):
		self.tabela = tabela

	def inserir_linha(self):
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
		print("_-_-_Atualizando a Linha_-_-_")
		print("1- Região")
		print("2- Unidade ornamentaria")
		print("3- Ação")
		print("4- Produto")
		op_user2 = int(input("Escolha qual linha deseja alterar:\n"))
		if op_user2 == 1:
			num = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[num, 'Regiao']))
			user_troca = input("Digite o valor desejado:\n")
			self.tabela.loc[num, 'Regiao'] = user_troca
			print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num, 'Regiao']))
		elif op_user2 == 2:
			num2 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[num2, 'Unidade_Orcamentaria']))
			user_troca2 = input("Digite o valor desejado:\n")
			self.tabela.loc[num2, 'Regiao'] = user_troca2
			print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num2, 'Unidade_Orcamentaria']))
		elif op_user2 == 3:
			num3 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[num3, 'Acao']))
			user_troca3 = input("Digite o valor desejado:\n")
			self.tabela.loc[num3, 'Acao'] = user_troca3
			print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num3, 'Acao']))
		elif op_user2 == 4:
			num4 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[num4, 'Produto']))
			user_troca4 = input("Digite o valor desejado:\n")
			self.tabela.loc[num4, 'Regiao'] = user_troca4
			print("O valor depois de ser alterado é: {}\n".format(self.tabela.loc[num4, 'Produto']))

	def excluir_linha(self):
		print("_-_-_Excluindo da Linha_-_-_")
		print("1- Região")
		print("2- Unidade ornamentaria")
		print("3- Ação")
		print("4- Produto")
		op_user2 = int(input("Escolha qual linha deseja excluir:\n"))
		if op_user2 == 1:
			n = int(input("Digite um número para excluir: \n"))
			print("O valor que será excluído é esse: {}\n".format(self.tabela.loc[n, 'Regiao']))
			self.tabela.loc[n, 'Regiao'] = ""
			print("Valor excluído")
		elif op_user2 == 2:
			n2 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[n2, 'Unidade_Orcamentaria']))
			self.tabela.loc[n2, 'Regiao'] = ""
			print("Valor excluído")
		elif op_user2 == 3:
			n3 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[n3, 'Acao']))
			self.tabela.loc[n3, 'Regiao'] = ""
			print("Valor excluído")
		elif op_user2 == 4:
			n4 = int(input("Digite um número para alterar: \n"))
			print("O valor que será alterado é esse: {}\n".format(self.tabela.loc[n4, 'Produto']))
			self.tabela.loc[n4, 'Regiao'] = ""
			print("Valor excluído")