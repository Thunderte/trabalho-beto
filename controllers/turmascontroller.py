from models.turma import criarUmaTurma
from utils.codigo import gerarCodigoTurma

def criarTurma():
    print('------------ TURMAS ------------')
    print('\n Bem vindo ao servidor de cadastro de turmas \n')

    nome = str(input("Digite o nome da turma para começar:\n"))

    codigo = gerarCodigoTurma()

    turma = criarUmaTurma(nome, codigo)

    return print(f"Turma {nome} cadastrada com sucesso.\n N° codigo: {codigo}");