


import sqlite3
import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QApplication
)

from crypto_dados.cry import descriptografa_texto


class TelaAdmin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Painel do Administrador")
        self.resize(700, 400)

        self.tabela = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.tabela)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.carregar_dados()

    def carregar_dados(self):
        conn = sqlite3.connect("DataBase3")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, password
            FROM dados
        """)

        usuarios = cursor.fetchall()

        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "Email",
            "Senha"
        ])

        self.tabela.setRowCount(len(usuarios))

        for linha, usuario in enumerate(usuarios):
            id_usuario = usuario[0]
            nome = descriptografa_texto(usuario[1])
            email = descriptografa_texto(usuario[2])
            senha = descriptografa_texto(usuario[3])

            print(id_usuario, nome, email, senha)

            self.tabela.setItem(linha, 0, QTableWidgetItem(str(id_usuario)))
            self.tabela.setItem(linha, 1, QTableWidgetItem(nome))
            self.tabela.setItem(linha, 2, QTableWidgetItem(email))
            self.tabela.setItem(linha, 3, QTableWidgetItem(senha))

            self.tabela.setItem(
                linha, 0,
                QTableWidgetItem(str(id_usuario))
            )

            self.tabela.setItem(
                linha, 1,
                QTableWidgetItem(nome)
            )

            self.tabela.setItem(
                linha, 2,
                QTableWidgetItem(email)
            )

            self.tabela.setItem(
                linha, 3,
                QTableWidgetItem(senha)
            )

        conn.close()

app = QApplication(sys.argv)

janela = TelaAdmin()

janela.show()

app.exec()

