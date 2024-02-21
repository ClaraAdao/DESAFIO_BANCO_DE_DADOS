import sqlite3

conexao = sqlite3.connect('universidade.db')

cursor = conexao.cursor()

'''1 - CRIANDO A TABELA alunos'''
#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


'''2 - INSERINDO REGISTROS EM alunos'''
#cursor.execute('INSERT INTO alunos VALUES (1,"Lucas",20,"Engenharia")')
#cursor.execute('INSERT INTO alunos VALUES (2,"Maria",20,"Biologia")')
#cursor.execute('INSERT INTO alunos VALUES (3,"Paulo",20,"Teologia")')
#cursor.execute('INSERT INTO alunos VALUES (4,"Pedro",20,"Mecânica")')
#cursor.execute('INSERT INTO alunos VALUES (5,"Sara",20,"Educação Física")')
#cursor.execute('INSERT INTO alunos VALUES (6,"Mateus",25,"Pedagogia")')
#cursor.execute('INSERT INTO alunos VALUES (7,"Miguel",23,"Engenharia")')
#cursor.execute('INSERT INTO alunos VALUES (8,"Madalena",22,"Engenharia")')
#cursor.execute('INSERT INTO alunos VALUES (9,"Caledrina",21,"Engenharia")')


'''3-CONSULTAS BÁSICAS
    a)TODOS OS REGISTROS DA TABELA alunos'''
#dados = cursor.execute('SELECT * FROM alunos')
#for aluno in dados:
#    print(aluno)

'''b)NOME E IDADE DOS ALUNOS COM MAIS DE 20 ANOS'''
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
#for aluno in dados:
#    print(aluno)

'''c)ALUNOS DE ENGENHARIA EM ORDEM ALFABÉTICA'''
#dados = cursor.execute('SELECT * FROM alunos GROUP BY nome HAVING curso="Engenharia" ORDER BY nome')
#for aluno in dados:
#    print(aluno)

'''d) NÚMERO TOTAL DE ALUNOS NA TABELA'''
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for aluno in dados:
#    print(f'Há {aluno} alunos registrados na tabela.')


'''4 - ATUALIZAÇÃO E REMOÇÃO
    a) ATUALIZANDO A IDADE DE UM ALUNO ESPECÍFICO'''
#cursor.execute('UPDATE alunos SET idade = 26 WHERE nome = "Maria"')


'''b) ROMOVENDO UM ALUNO PELO SEU ID'''
#cursor.execute('DELETE FROM alunos WHERE id=3')


'''5 - CRIANDO A TABELA clientes E INSERINDO REGISTROS'''
#cursor.execute('CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT(8,2))')
#cursor.execute('INSERT INTO clientes VALUES(1, "Felipe", 20, 1289.3)')
#cursor.execute('INSERT INTO clientes VALUES(2, "Paulo", 20, 1279.3)')
#cursor.execute('INSERT INTO clientes VALUES(3, "Sérgio", 35, 1389.3)')
#cursor.execute('INSERT INTO clientes VALUES(4, "Amora", 21, 950.38)')
#cursor.execute('INSERT INTO clientes VALUES(5, "Laura", 21, 2000.3)')
#cursor.execute('INSERT INTO clientes VALUES(6, "Romina", 21, 2000.3)')
#cursor.execute('INSERT INTO clientes VALUES(7, "Ingrid", 23, 7950.99)')
#cursor.execute('INSERT INTO clientes VALUES(8, "Pedro", 22, 10160.2)')
#cursor.execute('INSERT INTO clientes VALUES(9, "Isis", 27, 2003.45)')
#cursor.execute('INSERT INTO clientes VALUES(10, "Ismael", 33, 1387.90)')


'''6 - CONSULTAS E FUNÇÕES AGREGADAS
    a) NOME E IDADE DOS CLIENTES MAIORES DE 30 ANOS'''
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for cliente in dados:
#    print(cliente)

'''b) CALCULANDO O SALDO MÉDIO DOS CLIENTES'''
#cursor.execute('SELECT AVG(saldo) AS media_saldo FROM clientes')
#
#resultado = cursor.fetchone()
#
#media_saldo = resultado[0]
#print(f'A média do saldo dos clientes é: R$ {media_saldo:.2f}')


'''c) CLIENTE COM O MAIOR SALDO'''
#cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

## obtendo o resultado da consulta

#resultado = cursor.fetchone()

## Exibindo o maior saldo

#maior_saldo = resultado[0]

#if resultado:
#    nome_maior_saldo, maior_saldo = resultado
#    print(f"O cliente com o maior saldo é {nome_maior_saldo} com um saldo de R$ {maior_saldo}")
#else:
#    print("Não há clientes na tabela.")


'''d) QUANTIDADE DE CLIENTES COM SALDO ACIMA DE 1000'''
#cursor.execute('SELECT COUNT(saldo)  qtd_saldos FROM clientes WHERE saldo > 1000')
#
#resultado = cursor.fetchone()
#
#qtd_saldos = resultado[0]
#print(f'Existem {qtd_saldos} clientes com saldo acima de R$ 1.000,00 ')


'''7 - ATUALIZAÇÃO E ROMOÇÃO COM CONDIÇÕES
    a) ATUALIZANDO O SALDO DE UM CLIENTE ESPECÍFICO'''
#cursor.execute('UPDATE clientes SET saldo = 3980.76 WHERE nome = "Ismael"')

'''b) REMOVENDO UM CLIENTE PELO SEU ID'''
#cursor.execute('DELETE FROM clientes WHERE id = 10')


'''8 - JUNÇÃO DE TABELAS'''

#CRIANDO E INSERINDO REGISTROS EM compras

#cursor.execute('CREATE TABLE compras (id INT AUTO_INCREMENT PRIMARY KEY, produto VARCHAR(150), valor REAL, cliente_id INT, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')

#cursor.execute('INSERT INTO compras VALUES (1, "Livro", 60.00, 1)')
#cursor.execute('INSERT INTO compras VALUES (2, "Mochila", 92.50, 3)')
#cursor.execute('INSERT INTO compras VALUES (3, "Livro", 60.00, 5)')
#cursor.execute('INSERT INTO compras VALUES (4, "Caderno", 46.60, 6)')
#cursor.execute('INSERT INTO compras VALUES (5, "Calculadora", 25.39, 2)')
#cursor.execute('INSERT INTO compras VALUES (6, "Dicionário", 49.99, 9)')
#cursor.execute('INSERT INTO compras VALUES (7, "Jaleco", 80.20, 4)')
#cursor.execute('INSERT INTO compras VALUES (8, "Uniforme", 149.99, 8)')

#CONSULTA PARA EXIBIR NOME DO CLIENTE, PRODUTO E VALOR DE CADA COMPRA

#dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes, compras WHERE compras.cliente_id = clientes.id')
#for res in dados:
#    print(res)


conexao.commit()

conexao.close
