class Cliente():
    ultimo_id = 1000

    def __init__(self, nome: str, telefone: str, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
        # cria primeiro cliente com ID único = 1000
        # faz com que o próximo cliente tenha ID único incremental
        self.__id = Cliente.ultimo_id 
        Cliente.ultimo_id += 1

    @property
    def nome(self):
        """Retorna o nome do cliente."""
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        """Define o nome do cliente."""
        self.__nome = novo_nome

    @property
    def telefone(self):
        """Retorna o telefone do cliente."""
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        """Define o telefone do cliente."""
        self.__telefone = novo_telefone
    
    @property
    def email(self):
        """Retorna o email do cliente."""
        return self.__email
    
    @email.setter
    def email(self, novo_email: str):
        """Define o email do cliente."""
        self.__email = novo_email
    
    @property
    def id(self):
        """Retorna o ID único do cliente (somente leitura)."""
        return self.__id