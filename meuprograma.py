import sys
from consultas import listar_cursos_por_unidade, dados_de_um_curso
from coleta import coletar_dados

def main():
    if len(sys.argv) != 2:
        print("Uso: python meuprograma.py <numero_de_unidades>")
        sys.exit(1)

    try:
        numero_unidades = int(sys.argv[1])
    except ValueError:
        print("O parâmetro deve ser um número inteiro.")
        sys.exit(1)

    print(f"\nColetando dados das {numero_unidades} primeiras unidades da USP...\n")
    unidades = coletar_dados(numero_unidades)

    while True:
        print("\nConsultas disponíveis:")
        print("1 - Listar cursos por unidade")
        print("2 - Mostrar dados de um curso")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_cursos_por_unidade(unidades)
        elif opcao == "2":
            nome = input("Digite o nome do curso: ")
            dados_de_um_curso(unidades, nome)
        elif opcao == "3":
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
