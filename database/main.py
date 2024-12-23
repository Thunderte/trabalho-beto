import sqlite3

def criarBancoETabelas():
   conexao = sqlite3.connect("escola.db");
   
   conn = conexao.cursor()

   conn.execute("CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, matricula TEXT NOT NULL, data_nascimento DATE, sexo TEXT NOT NULL, endereco TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)")
   conn.execute("CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, codigo TEXT NOT NULL, data_nascimento DATE, sexo TEXT NOT NULL, endereco TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)")

