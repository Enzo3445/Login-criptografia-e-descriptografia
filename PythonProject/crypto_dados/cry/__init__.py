

from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()

    with open("Chave.key", "wb") as arquivo:
        arquivo.write(chave)

    print("Chave salva!")


def carregar_chave():
    with open("Chave.key", "rb") as arquivo:
        return arquivo.read()



def crytografa_texto(texto):
    chave = carregar_chave()
    fernet = Fernet(chave)
    texto_crypt = fernet.encrypt(texto.encode())

    return texto_crypt.decode()

def descriptografa_texto(texto_crypt):
    chave = carregar_chave()
    fernet = Fernet(chave)
    texto = fernet.decrypt(
        texto_crypt
    ).decode()
    return texto









