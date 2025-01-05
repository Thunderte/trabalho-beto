import sqlite3

def criarUmProfessor(nome: str, codigo: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str) -> str:
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, codigo, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO professores(nome, codigo, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° codigo: {codigo}"

def professoresDisponiveis() -> str:
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   professores = conn.execute("SELECT * FROM professores")

   professores = professores.fetchall()

   return professores

def pesquisarProfessor(id: int) -> str:
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   professores = conn.execute(f"""
    SELECT professores.*, disciplinas.*
    FROM professores
    LEFT JOIN disciplinas ON professores.id = disciplinas.professor_id
    WHERE professores.id = {id}
   """)

   professor = professores.fetchone()

   return professor
