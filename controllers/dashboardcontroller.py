from controllers.alunoscontroller import criarAluno, pesquisarAluno
from controllers.professorcontroller import criarProfessor, pesquisarProfessor
from controllers.disciplinacontroller import criarDisciplina, pesquisarDisciplina
from controllers.turmascontroller import criarTurma
from database.main import criarBancoETabelas

def dashboard():
    print('------------ DASHBOARD ------------')
    print('\n Bem vindo ao servidor administrativo do IFMS \n')

    while True:
        print('O que deseja fazer?\n')
        print('0 - Criar tabelas no banco de dados\n')
        print('1 - Cadastrar aluno\n')
        print('2 - Cadastrar professor\n')
        print('3 - Cadastrar disciplina\n')
        print('4 - Pesquisar Aluno\n')
        print('5 - Pesquisar Professor\n')
        print('6 - Pesquisar Disciplina\n')
        print('7 - Cadastrar Turma \n')
        print('8 - Sair\n')

        opcao = int(input('Digite a opção desejada: '))

        try:
            if opcao == 0:
                criarBancoETabelas()
            elif opcao == 1:
                criarAluno()
            elif opcao == 2:
                criarProfessor()
            elif opcao == 3:
                criarDisciplina()
            elif opcao == 4:
                pesquisarAluno()
            elif opcao == 5:
                pesquisarProfessor()
            elif opcao == 6: 
                pesquisarDisciplina()
            elif opcao == 7:
                criarTurma()
            elif opcao == 8:
                print('Saindo do servidor...\n')
                break
            else:
                print('Opção inválida. Tente novamente.\n')
        except ValueError:
            print('Valores inválidos. Tente novamente.\n')