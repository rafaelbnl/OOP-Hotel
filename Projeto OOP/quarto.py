class Quarto():
    def __init__(self, numero:int, tipo:str, diaria:float, status:str):
        self.__numero = numero
        self.__tipo = tipo
        self.__diaria = diaria
        self.__status = status

    @property
    def numero(self):
        """Retorna o número do quarto."""
        return self.__numero
    @numero.setter
    def numero(self, novo_numero:int):
        """Define o número do quarto."""
        self.__numero = novo_numero

    @property
    def tipo(self):
        """Retorna o tipo do quarto."""
        return self.__tipo
    @tipo.setter
    def tipo(self, novo_tipo:str):
        """Define o tipo do quarto."""
        self.__tipo = novo_tipo

    @property
    def diaria(self):
        """Retorna o valor da diária do quarto."""
        return self.__diaria
    @diaria.setter
    def diaria(self, nova_diaria:float):
        """Define o valor da diária do quarto."""
        self.__diaria = nova_diaria

    @property
    def status(self):
        """Retorna o status do quarto."""
        return self.__status
    @status.setter
    def status(self, novo_status:str):
        """Define o status do quarto."""
        status_validos = ["disponível", "ocupado"]
        if novo_status in status_validos:
            self.__status = novo_status
        else:
            print(f"\nStatus inválido! Use: {status_validos}")

