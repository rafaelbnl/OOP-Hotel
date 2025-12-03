from classes import *

hotel1 = Hotel(nome="Refúgio dos Sonhos", logradouro="Rua da Paz", numero=123, rede="Accor")
refugio = Gerenciador(hotel1)

def main():
    while True:
        try: 
            print(f"""
    Sistema de gerenciamento
    1 - Criar reserva
    2 - Modificar reserva
    3 - Cancelar reserva
    4 - Listar reservas
    5 - Criar quarto
    6 - Modificar quarto
    7 - Excluir quarto
    8 - Listar quartos
    0 - Sair do sistema
    """)
            opt = int(input("Selecione uma opção: "))

            match opt:
                case 1:
                    cliente = input("Nome do cliente: ")
                    numero_quarto = int(input("Número do quarto: "))
                    checkin = input("Data de check-in (dd/mm/aaaa): ")
                    checkout = input("Data de check-out (dd/mm/aaaa): ")
                    status = input("Status (confirmada/pendente/cancelada): ")
                    refugio.criar_reserva(cliente, numero_quarto, checkin, checkout, status)
                    
                case 2:
                    id_reserva = int(input("ID da reserva: "))
                    cliente = input("Novo nome do cliente (ou Enter para manter): ")
                    numero_quarto = input("Novo número do quarto (ou Enter para manter): ")
                    numero_quarto = int(numero_quarto) if numero_quarto else None
                    checkin = input("Nova data de check-in (ou Enter para manter): ")
                    checkout = input("Nova data de check-out (ou Enter para manter): ")
                    status = input("Novo status (ou Enter para manter): ")
                    refugio.modificar_reserva(id_reserva, cliente or None, numero_quarto, checkin or None, checkout or None, status or None)
                    
                case 3:
                    id_reserva = int(input("ID da reserva a cancelar: "))
                    refugio.cancelar_reserva(id_reserva)
                    
                case 4:
                    print(refugio.listar_reservas())
                    
                case 5:
                    numero = int(input("Número do quarto: "))
                    tipo = input("Tipo do quarto: ")
                    preco = float(input("Preço da diária: "))
                    disponivel = input("Disponível? (s/n): ").lower() == 's'
                    hotel1.cadastrar_quarto(numero, tipo, preco, disponivel)
                    
                case 6:
                    numero = int(input("Número do quarto: "))
                    tipo = input("Novo tipo (ou Enter para manter): ")
                    preco = input("Novo preço (ou Enter para manter): ")
                    preco = float(preco) if preco else None
                    disponivel = input("Disponível? (s/n ou Enter para manter): ")
                    disponivel = disponivel.lower() == 's' if disponivel else None
                    hotel1.editar_quarto(numero, tipo or None, preco, disponivel)
                    
                case 7:
                    numero = int(input("Número do quarto a excluir: "))
                    hotel1.excluir_quarto(numero)
                    
                case 8:
                    print(hotel1.listar_quartos())
                    
                case 0:
                    print("Saindo do sistema...")
                    break
                    
                case _:
                    print("Opção inválida")
                    
        except ValueError:
            print("Digite apenas números válidos!")
        except Exception as e:
            print(f"Erro: {e}")

main()
