from cliente import Cliente
from quarto import Quarto

class Reserva:
    ultimo_id = 1
    
    def __init__(self, cliente: Cliente, quarto: Quarto, checkin: str, checkout: str, status:str):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__checkin = checkin
        self.__checkout = checkout
        self.__status = status
        self.__id = Reserva.ultimo_id
        Reserva.ultimo_id += 1

    @property
    def cliente(self):
        """Retorna o cliente da reserva."""
        return self.__cliente

    @cliente.setter
    def cliente(self, novo_cliente: Cliente):
        """Define o cliente da reserva."""
        self.__cliente = novo_cliente

    @property
    def quarto(self):
        """Retorna o quarto da reserva."""
        return self.__quarto
    
    @quarto.setter
    def quarto(self, novo_quarto: Quarto):
        """Define o quarto da reserva."""
        self.__quarto = novo_quarto

    @property
    def checkin(self):
        """Retorna a data de check-in da reserva."""
        return self.__checkin
    
    @checkin.setter
    def checkin(self, nova_data_checkin: str):
        """Define a data de check-in da reserva."""
        self.__checkin = nova_data_checkin

    @property
    def checkout(self):
        """Retorna a data de check-out da reserva."""
        return self.__checkout
    
    @checkout.setter
    def checkout(self, nova_data_checkout: str):
        """Define a data de check-out da reserva."""
        self.__checkout = nova_data_checkout

    @property
    def status(self):
        """Retorna o status da reserva."""
        return self.__status
    
    @status.setter
    def status(self, novo_status: str):
        """Define o status da reserva."""
        status_validos = ["ativa", "cancelada", "concluída"]
        if novo_status in status_validos:
            self.__status = novo_status
        else:
            print(f"\nStatus inválido! Use: {status_validos}")

    @property
    def id(self):
        """Retorna o ID único da reserva (somente leitura)."""
        return self.__id