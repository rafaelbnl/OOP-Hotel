from classes import Cliente, Quarto, Hotel, Gerenciador, Reserva

hotel1 = Hotel(nome="Refúgio dos Sonhos", logradouro="Rua da Paz", numero=123, rede="Accor")
refugio = Gerenciador(hotel1)

def main():
    while True:
        menu = input(f"""
            Sistema de gerenciamento
            1 - Fluxo de clientes
            2 - Fluxo de quartos
            3 - Fluxo de reservas
            0 - Sair do sistema
            """)
        match menu:
            case "1":
                while True:
                    menu_clientes = input("""
                        MENU CLIENTES
                    1 - Cadastrar cliente
                    2 - Listar clientes
                    3 - Editar clientes
                    4 - Excluir cliente
                    5 - Voltar
                    """)
                    match menu_clientes:
                        case "1":
                            mensagem = hotel1.cadastrar_cliente()
                            print(mensagem)
                        case "2":
                            mensagem = hotel1.listar_clientes()    
                            print(mensagem)
                        case "3":
                            mensagem = hotel1.editar_cliente()
                            print(mensagem)
                        case "4":
                            mensagem = hotel1.excluir_cliente()
                            print(mensagem)
                        case "5":
                            break
                        case _:
                            print("Opção inválida")
            case "2":
                while True:
                    menu_quartos = input("""
                        MENU quartos
                    1 - Cadastrar quarto
                    2 - Listar quartos
                    3 - Editar quarto
                    4 - Excluir quarto
                    5 - Voltar
                    """)
                    match menu_quartos:
                        case "1":
                            mensagem = hotel1.cadastrar_quarto()
                            print(mensagem)
                        case "2":
                            mensagem = hotel1.listar_quartos()    
                            print(mensagem)
                        case "3":
                            mensagem = hotel1.editar_quarto()
                            print(mensagem)
                        case "4":
                            mensagem = hotel1.excluir_quarto()
                            print(mensagem)
                        case "5":
                            break
                        case _:
                            print("Opção inválida")
            case "3":
                while True:
                    menu_reservas = input("""
                        1 - Criar reserva
                        2 - Listar reservas
                        3 - Editar reserva
                        4 - Excluir reserva
                        5 - Voltar
                        """)
                    match menu_reservas:
                        case "1":
                            mensagem = refugio.criar_reserva()
                            print(mensagem)
                        case "2":
                            mensagem = refugio.listar_reservas()    
                            print(mensagem)
                        case "3":
                            mensagem = refugio.editar_reserva()
                            print(mensagem)
                        case "4":
                            mensagem = refugio.excluir_reserva()
                            print(mensagem)
                        case "5":
                            break
                        case _:
                            print("Opção inválida")
            case "0":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")


main()
