import sqlite3

def criarUmaTurma(nome: str, codigo: str) -> str:
    conexao = sqlite3.connect("escola.db")
     
    conn = conexao.cursor()

    data = (nome, codigo)

    conn.execute("INSERT INTO turmas(nome, codigo) VALUES (?, ?)", data)

    conexao.commit()

    return f"Turma {nome} cadastrada com sucesso.\n N° codigo: {codigo}"