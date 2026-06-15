import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit


from crypto_dados.cry import crytografa_texto, descriptografa_texto

from senha.forte import *




import sqlite3


class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface")
        self.resize(400, 300)

        # Widgets e inputs
        self.texto = QLabel("coloque os seus dados aqui em baixo")
        self.input_nome = QLineEdit()

        self.input_nome.setPlaceholderText("digite seu nome")

        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("digite seu email")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("digite sua senha")

        self.botao = QPushButton("aperte o botao para os dados irem para o a database")

        self.input_chave =   QLineEdit()
        self.input_chave.setPlaceholderText("digite chave")
        #Interface mais questionario ao usuario




        # Evento
        self.botao.clicked.connect(self.criar_conta)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.input_email)
        layout.addWidget(self.input_password)
        layout.addWidget(self.input_chave)
        layout.addWidget(self.botao)



        self.setLayout(layout)

    def criar_conta(self):
        
        nome = self.input_nome.text()

        email = self.input_email.text()

        password = self.input_password.text()
        if detectador_de_senhafraca(password):
            print("senha fraca")
            
        else:
            chave = self.input_chave.text()

            
            if not nome or not email or not password:
                print("preencha todos os campos")
                return
            
            self.conn = sqlite3.connect('DataBase3')
            self.cursor = self.conn.cursor()

            

            self.cursor.execute("""create table if not exists dados (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nome TEXT,
             email TEXT,
             password TEXT)""")
            self.conn.commit()
            

            try:

                self.cursor.execute("""
                    INSERT INTO dados(nome, email, password)
                    VALUES (?, ?, ?)
                """, (
                    crytografa_texto(nome),
                    crytografa_texto(email),
                    crytografa_texto(password)
                ))

                self.conn.commit()

                print("2")

            except Exception as erro:
                print(erro)

        #Criando conta e criptografia no banco de daods








            print("Conta criada!")
            
            self.cursor.execute("SELECT * FROM dados")
            # Limpa inputs
            self.input_nome.clear()
            self.input_email.clear()
            self.input_password.clear()
            self.input_chave.clear()
            #limpando os input apos o usuario clicar no butão
            

            dados  = self.cursor.fetchall()
            for linha in dados:
                print(linha)
                

            return chave






    import sys
    print(sys.path)



# Inicialização
app = QApplication(sys.argv)

janela = Janela()

janela.show()

app.exec()


def criar_conta():
    return None
