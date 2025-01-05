from controllers.alunoscontroller import criarAluno
from controllers.professorcontroller import criarProfessor
from controllers.disciplinacontroller import criarDisciplina

def dashboard():
    print('------------ DASHBOARD ------------')
    print('\n Bem vindo ao servidor administrativo do IFMS \n')

    while True:
        print('O que deseja fazer?\n')
        print('1 - Cadastrar aluno\n')
        print('2 - Cadastrar professor\n')
        print('3 - Cadastrar disciplina\n')
        print('4 - Sair\n')

        opcao = int(input('Digite a opção desejada: '))

        try:
            if opcao == 1:
                criarAluno()
            elif opcao == 2:
                criarProfessor()
            elif opcao == 3:
                criarDisciplina()
            elif opcao == 4:
                break
            else:
                print('Opção inválida. Tente novamente.\n')
        except ValueError:
            print('Valores inválidos. Tente novamente.\n')
