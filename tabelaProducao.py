import sqlite3

conexao = sqlite3.connect('producao.db')
cursor = conexao.cursor()
sql = 'CREATE TABLE producao ('\
                                'PRODUTO TEXT, '\
                                'QTD_PRODUZIDA INTEGER, PRECO_MEDIO REAL, RECEITA_TOTAL REAL)'

cursor.execute(sql)
conexao.close()

print("Script executado com sucesso!!!")