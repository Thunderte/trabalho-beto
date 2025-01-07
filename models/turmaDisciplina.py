import sqlite3

def cadastrarDisciplinaEmTurma(turma_id: int, disciplina_id: int) -> str:
    conexao = sqlite3.connect("escola.db");

    conn = conexao.cursor()

    data = (turma_id, disciplina_id)

    conn.execute("INSERT INTO turmas_disciplinas (turma_id, disciplina_id) VALUES (?, ?)", data)

    conexao.commit()

    return f"Disciplina cadastrada com sucesso na turma."

def disciplinasEmUmaTurma(turma_id: int):
    conexao = sqlite3.connect("escola.db");

    conn = conexao.cursor()

    data = (turma_id,)

    conn.execute("""
    SELECT disciplinas.nome, disciplinas.codigo
    FROM turmas_disciplinas
    LEFT JOIN turmas ON turmas.id = turmas_disciplinas.turma_id
    LEFT JOIN disciplinas ON disciplinas.id = turmas_disciplinas.disciplina_id
    WHERE turmas_disciplinas.turma_id = ?
    """, data)

    disciplinas = conn.fetchall()

    return disciplinas
