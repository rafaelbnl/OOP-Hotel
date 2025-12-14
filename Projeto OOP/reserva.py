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

    def get_cliente(self):
        return self.__cliente
    def get_quarto(self):
        return self.__quarto
    def get_checkin(self):
        return self.__checkin
    def get_checkout(self):
        return self.__checkout
    def get_status(self):
        return self.__status
    def get_id(self):
        return self.__id
# sem setter pra mudar id; fixo
    def set_cliente(self, novo_cliente):
        self.__cliente = novo_cliente
    def set_quarto(self, novo_quarto):
        self.__quarto = novo_quarto
    def set_checkin(self, novo_checkin):
        self.__checkin = novo_checkin
    def set_checkout(self, novo_checkout):
        self.__checkout = novo_checkout
    def set_status(self, novo_status):
        self.__status = novo_status