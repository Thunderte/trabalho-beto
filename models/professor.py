import sqlite3

def criarUmProfessor(nome: str, codigo: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str) -> str:
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, codigo, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO professores(nome, codigo, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° codigo: {codigo}"