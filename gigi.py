# This file only has the code content of
# The jupyter notebook of the previous file.

import pandas as pd

nome_arquivo = input("Digite o nome do arquivo:\n")

c = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
try:
    df = pd.read_csv( nome_arquivo, names = c)
except:
    print("Arquivo nao existe.\nSera criado:")
    df = pd.DataFrame(columns = c)[c]

menu = """
1 - visualizar
2 - ordenar
3 - alterar valor
4 - adicionar dados
5 - deletar linha
6 - salvar arquivo
7 - sair
"""
while True:
    op = input(menu)
    if op == "1":
        print(df.to_string().strip("\n"))
    elif op == "2":
        col = input("Digite o nome de uma coluna: \n")
        ordem = input("Digite a ordem, (1)crescente ou (2)decrescente. \n")

        if ordem.lower() == "crescente" or ordem == "1":
            df = df.sort_values(by = col, ascending = True)
        else:
            df = df.sort_values(by = col, ascending = False)
        df.reset_index(inplace = True)
    elif op == "3":
        al = input("Digite linha, coluna e novo valor separados por espaço.\n").split(" ")
        df.iloc[int(al[0]), int(al[1])] = float(al[2])

    elif op == "4":
        al = input("Digite o novos valores separados por espaço.\n").split(" ")
        for i in range (4):
            al[i] = float(al[i])
        df2 = pd.DataFrame([al], columns = c)[c]
        df = df.append(df2)

    elif op == "5":
        liera = input("Linha que será apagada:\n")
        df.drop(index = int(liera), inplace = True)
        df.reset_index(inplace = True)

    elif op == "6":
        df.to_csv(nome_arquivo, index = False, header = False)
        print("Arquivo salvo.")

    elif op == "7":
        print("fim.")
        break
    else:
        print("Opcao invalida." + op + ".")
