import sqlite3

conexao = sqlite3.connect('Aula44.db')
c = conexao.cursor()


c.execute('CREATE TABLE IF NOT EXISTS usuario(id integer, nome text)')

requisicao = "SELECT * FROM usuario WHERE nome = ?"

for linha in c.execute(requisicao, ('Rodrigo',)):
    print(linha)
