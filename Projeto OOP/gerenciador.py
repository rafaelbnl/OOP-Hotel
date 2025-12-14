from hotel import Hotel
from reserva import Reserva

class Gerenciador():
    def __init__(self, hotel:Hotel):
        self.__hotel = hotel
        self.__lista_de_reservas = []

    def get_hotel(self):
        return self.__hotel
    
    def get_lista_de_reservas(self):
        return self.__lista_de_reservas
    
    def verificar_disponibilidade(self):
        return self.__hotel.listar_quartos()

    def criar_reserva(self):
        # Buscar cliente
        try:
            nome_cliente = input("Digite o nome do cliente: ")
            cliente_encontrado = None
            for cliente in self.__hotel.get_lista_de_clientes():
                if cliente.get_nome().lower() == nome_cliente.lower():
                    cliente_encontrado = cliente
                    break
        except Exception as e:
            return f"Erro ao buscar cliente: {e}"
        
        if not cliente_encontrado:
            return f"\nCliente '{nome_cliente}' não encontrado. Cadastre o cliente primeiro."
        
        # Buscar quarto
        try:
            numero_quarto = int(input("Digite o numero do quarto alocado: "))
            quarto_encontrado = None
            for quarto in self.__hotel.get_lista_de_quartos():
                if quarto.get_numero() == numero_quarto:
                    quarto_encontrado = quarto
                    break
        except Exception as e:
            return f"Erro ao buscar quarto: {e}"
        
        if not quarto_encontrado:
            return f"\nQuarto {numero_quarto} não encontrado."
        
        if quarto_encontrado.get_status().lower() != "disponível":
            return f"\nQuarto {numero_quarto} não está disponível."
        try:
            checkin = input("Digite a data do check-in: ")
            checkout = input("Digite a data do check-out: ")
            status = "Ativa"
        except Exception as e:
            return f"Erro ao criar reserva: {e}"
        
        reserva = Reserva(cliente=cliente_encontrado, quarto=quarto_encontrado, checkin=checkin, checkout=checkout, status=status)
        quarto_encontrado.set_status("ocupado")
        self.__lista_de_reservas.append(reserva)
        return f"\nReserva criada com sucesso! ID: {reserva.get_id()}"

    def listar_reservas(self):
        if not self.__lista_de_reservas:
            return "Não há reservas cadastradas"
        for reserva in self.__lista_de_reservas:
            cliente = reserva.get_cliente()
            quarto = reserva.get_quarto()
            print(f"""
                    ===INFORMAÇÕES DA RESERVA====================
                    ID da Reserva: {reserva.get_id()}
                    Cliente: {cliente.get_nome().title()}
                    Quarto: {quarto.get_numero()}
                    Check-in: {reserva.get_checkin()}
                    Check-out: {reserva.get_checkout()}
                    Status: {reserva.get_status()}
                    ============================================
                    """)

    def editar_reserva(self):
        try:
            reserva_modificada = int(input("Digite o ID da reserva a modificar: "))
            for reserva in self.__lista_de_reservas:
                if reserva.get_id() == reserva_modificada:
                    try:
                        while True:
                            modificar = input("""Modificar:
                                                1 - Check-in
                                                2 - Check-out
                                                3 - Status
                                                4 - Voltar
                                                """)
                            match modificar:
                                case "1":
                                    novo_checkin = input("Digite a nova data de check-in: ")
                                    reserva.set_checkin(novo_checkin)
                                    return "\nCheck-in modificado"
                                case "2":
                                    novo_checkout = input("Digite a nova data de check-out: ")
                                    reserva.set_checkout(novo_checkout)
                                    return "\nCheck-out modificado"
                                case "3":
                                    novo_status = input("Digite o novo status da reserva: ")
                                    reserva.set_status(novo_status)
                                    return "\nStatus modificado"
                                case "4":
                                    return "\nOperação cancelada"
                                case _:
                                    print("\nOpção inválida")
                    except Exception as e:
                        return f"Erro ao editar reserva: {e}"
        except Exception as e:
            return f"Erro ao editar reserva: {e}"

    def excluir_reserva(self):
        try:
            reserva_cancelada = int(input("Digite o ID da reserva a cancelar: "))
            for reserva in self.__lista_de_reservas:
                if reserva.get_id() == reserva_cancelada:
                    quarto = reserva.get_quarto()
                    quarto.set_status("disponível")
                    self.__lista_de_reservas.remove(reserva)
                    return f"Reserva {reserva_cancelada} cancelada"
        except Exception as e:
            return f"Erro ao cancelar reserva: {e}"