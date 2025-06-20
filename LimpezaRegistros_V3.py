import csv
import sqlite3

def retirarPontoValor(valor):
    return valor.replace('.','')

with open('producao_alimentos.csv', 'r') as arquivo:
    leitura = csv.reader(arquivo)
    next(leitura)

    conexao = sqlite3.connect('producao.db')
    conexao.execute('DROP TABLE IF EXISTS producao')

    conexao.execute('CREATE TABLE producao(PRODUTO TEXT, QTD_PRODUZIDA INTEGER, PRECO_MEDIO REAL,'\
                    'RECEITA_TOTAL REAL, MARGEM_LUCRO REAL )')
    try:
        for linhascsv in leitura:
            if int(linhascsv[1]) > 10:
                linhascsv[3] = retirarPontoValor(linhascsv[3])
                margem_lucro = (float(linhascsv[3]) / float(linhascsv[1])) - float(linhascsv[2])

                conexao.execute('INSERT INTO producao(PRODUTO, QTD_PRODUZIDA, PRECO_MEDIO, '\
                        'RECEITA_TOTAL, MARGEM_LUCRO) VALUES(?,?,?,?,?)', (linhascsv[0],linhascsv[1],linhascsv[2],linhascsv[3],margem_lucro))

        conexao.commit()
        print("Processo executado com sucesso!!")

    except Exception as error:
         print("Ocorreu erro no processo: ",error)

    finally:
        print("Conexão finalizada...")
        conexao.close()
