
def detectador_de_senhafraca(senha):
        if len(senha) <= 6:
            return True
        elif '123' in senha:
            return True
        elif senha.isalpha():
            return True
        elif senha.isnumeric():
            return True
        elif senha.isalpha and senha.isnumeric():
            return False
        else:
            return False