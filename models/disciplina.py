import sqlite3

def criarUmaDisciplina(nome: str, codigo: str, professor_id: int, carga_horaria: int) -> str:
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    data = (nome, codigo, professor_id, carga_horaria)

    conn.execute("INSERT INTO disciplinas (nome, codigo, professor_id, carga_horaria) VALUES (?, ?, ?)", data)

    conexao.commit()

    return f"Disciplina {nome} cadastrada com sucesso."