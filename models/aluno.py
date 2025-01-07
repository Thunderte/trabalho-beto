
import sqlite3

def criarUmAluno(nome: str, matricula: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str) -> str:
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, matricula, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO alunos(nome, matricula, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° matricula: {matricula}"

def pesquisarAlunos(id):
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   alunos = conn.execute(f"SELECT * FROM alunos WHERE id = {id}")

   aluno = alunos.fetchone()

   return aluno

def alunosDisponiveis() -> str:
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   alunos = conn.execute("SELECT * FROM alunos")

   alunos = alunos.fetchall()

   return alunos
