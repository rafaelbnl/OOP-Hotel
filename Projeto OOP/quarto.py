class Quarto():
    def __init__(self, numero:int, tipo:str, diaria:float, status:str):
        self.__numero = numero
        self.__tipo = tipo
        self.__diaria = diaria
        self.__status = status

    def get_numero(self):
        return self.__numero
    def get_tipo(self):
        return self.__tipo
    def get_diaria(self):
        return self.__diaria
    def get_status(self):
        return self.__status

# sem setter pra número; fixo 
    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo
    def set_diaria(self, nova_diaria):
        self.__diaria = nova_diaria
    def set_status(self, novo_status):
        status_validos = ["disponível", "ocupado"]
        if novo_status in status_validos:
            self.__status = novo_status
        else:
            print(f"\nStatus inválido! Use: {status_validos}")