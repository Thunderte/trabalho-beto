from models.professor import professoresDisponiveis
from models.professor import pesquisarProfessor
from models.disciplina import criarUmaDisciplina

def criarDisciplina():
    print('------------ DISCIPLINAS ------------')
    print('\n Bem vindo ao servidor de cadastro de disciplinas \n')

    nome = str(input("Digite o nome da disciplina para comecar:\n"))

    todosProfessores = professoresDisponiveis()

    professores = []

    for i in range(0, len(todosProfessores)):
      professores.append({ 'id': todosProfessores[i][0], 'nome': todosProfessores[i][1] })

    print("Professores disponiveis no IFMS:\n")
    print("Modelo de impressão: [numero] - [nome]\n")
    for i in range(0, len(professores)):
      print(f"{professores[i]['id']} - {professores[i]['nome']}")

    professor = int(input("Qual o numero do professor da disciplina?\n"))

    professorPesquisado = pesquisarProfessor(professor)

    if(professorPesquisado == None):
        print('Error: professor não encontrado')
        exit()

    cargaHoraria = int(input("Qual a carga horária da disciplina?\n"))

    disciplina = criarUmaDisciplina(nome, professor, cargaHoraria);

    return print(disciplina);