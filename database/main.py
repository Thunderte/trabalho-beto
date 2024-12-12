import sqlite3

def criarBancoETabelas():
   conexao = sqlite3.connect("escola.db");
   
   conn = conexao.cursor()

   conn.execute("CREATE TABLE alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, matricula TEXT NOT NULL, data_nascimento DATE, sexo TEXT NOT NULL, endereco TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)")

def criarUmAluno(nome: str, matricula: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str):
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, matricula, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO alunos(nome, matricula, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° matricula: {matricula}"

def pesquisarAlunos(id):
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   alunos = conn.execute("SELECT * FROM alunos WHERE id = 1")

   aluno = alunos.fetchone()

   return print(aluno)