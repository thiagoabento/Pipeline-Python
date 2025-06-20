import csv
import sqlite3

with open('producao_alimentos.csv') as arquivo:
    leitura = csv.reader(arquivo)
    next(leitura)
    conexao = sqlite3.connect('producao.db')
    conexao.execute('DROP TABLE IF EXISTS producao')

    conexao.execute('CREATE TABLE producao ('\
                    'PRODUTO TEXT, '\
                    'QTD_PRODUZIDA INTEGER, PRECO_MEDIO REAL, RECEITA_TOTAL REAL)')

    try:
        for linhacsv in leitura:
            if int(linhacsv[1] ) > 10:
                 conexao.execute('INSERT INTO producao(PRODUTO, QTD_PRODUZIDA, PRECO_MEDIO, RECEITA_TOTAL) VALUES(?,?,?,?)',linhacsv)
        conexao.commit()
        print("Procedimento realizado com sucesso!!!")
    except Exception as error:
        print("Ocorreu erro no processo: ", error)
    finally:
        print("Conexão finalizada...")
        conexao.close()


