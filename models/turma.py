import sqlite3

def criarUmaTurma(nome: str, codigo: str) -> str:
    conexao = sqlite3.connect("escola.db")
     
    conn = conexao.cursor()

    data = (nome, codigo)

    conn.execute("INSERT INTO turmas(nome, codigo) VALUES (?, ?)", data)

    conexao.commit()

    return f"Turma {nome} cadastrada com sucesso.\n N° codigo: {codigo}"

def turmasDisponiveis() -> str:
    conexao = sqlite3.connect("escola.db")

    conn = conexao.cursor()

    turmas = conn.execute("SELECT * FROM turmas")

    turmas = turmas.fetchall()

    return turmas

def pesquisarTurma(id: int) -> str:
    conexao = sqlite3.connect("escola.db")

    conn = conexao.cursor()

    turmas = conn.execute(f"""
     SELECT turmas.*, alunos.*
     FROM turmas
     LEFT JOIN turmas_alunos ON turmas.id = turmas_alunos.turma_id
     LEFT JOIN alunos ON turmas_alunos.aluno_id = alunos.id
     WHERE turmas.id = {id}
    """)

    turma = turmas.fetchone()

    return turma
