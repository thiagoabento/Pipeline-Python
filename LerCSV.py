import csv as csv
import sqlite3

with open('producao_alimentos.csv') as file:
    leitura = csv.reader(file)
    
    #Desconsiderando o cabeçalho do arquivo csv
    next(leitura)
    conexao = sqlite3.connect('producao.db')

    try:
        for linhacsv in leitura:
            conexao.execute(
                'INSERT INTO producao(PRODUTO, QTD_PRODUZIDA, PRECO_MEDIO, RECEITA_TOTAL) VALUES (?, ?, ?, ?)',
                linhacsv
            )
        conexao.commit()
        print("Procedimento realizado com sucesso!!!")
    except Exception as error:
        print("Ocorreu erro no processo: ", error)
    finally:
        print("Conexão finalizada...")
        conexao.close()