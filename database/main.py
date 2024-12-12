import sqlite3

connect = "";

def criarBancoETabelas():
   conexao = sqlite3.connect("escola.db");
   
   conn = conexao.cursor()

   conn.execute("CREATE TABLE alunos(id, nome, matricula, data_nascimento, sexo, endereco, telefone, email)")

def criarUmAluno(nome: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str):
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   matricula: str = "123456-A";

   data = [(nome, matricula, data_nascimento, sexo, endereco, telefone, email)]

   conn.execute("INSERT INTO alunos(nome, matricula, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)")

   return f"Aluno {nome} cadastro com sucesso.\n N° matricula: {matricula}"