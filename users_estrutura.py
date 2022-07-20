from time import strftime
from tkinter.messagebox import YES
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import mysql.connector
from pip import main
from reportlab.pdfgen import canvas
from subprocess import call

cnx = mysql.connector.connect(
    host="localhost",
    database="banco-empresa",
    user="root",
    password="",
)
def open_inserir():
    users.show()

def inserir():
    banco_dados.close()
    setor = users.comboBox.currentText()
    nome = users.lineEdit.text()
    email = users.lineEdit_2.text()
    usuario = users.lineEdit_3.text()
    senha = users.lineEdit_4.text()
    senha2 = users.lineEdit_5.text()


    if senha != senha2:
        QMessageBox.information(QMessageBox(), "Sistema YanCode", "As senhas não conhecidem, digite senhas iguais para concluir o cadastro!")
    elif senha == senha2:
        cursor = cnx.cursor()
        data = date.today()
        sql = ("INSERT INTO login (log_nome, log_email, log_usuario, log_senha, log_setor, log_data_criacao) VALUES (%s, %s, %s, %s, %s, %s)")
        dados = (str(nome), str(email), str(usuario), str(senha), setor, data)
        print(dados)
        cursor.execute(sql, dados)
        cnx.commit()
        QMessageBox.information(QMessageBox(), "Sistema YanCode", "O usuário foi cadastrado com sucesso!")
        users.close()
    visualizar_users()

def visualizar_users():
    banco_dados.show()
    cursor = cnx.cursor()
    sql = ("SELECT * FROM login")
    cursor.execute(sql)
    contagem = cursor.fetchall()
    banco_dados.tableWidget.setRowCount(len(contagem))
    banco_dados.tableWidget.setColumnCount(7)
    banco_dados.tableWidget.setColumnWidth(0, 40)
    banco_dados.tableWidget.setColumnWidth(1,200)
    banco_dados.tableWidget.setColumnWidth(2,220)
    banco_dados.tableWidget.setColumnWidth(3,100)
    banco_dados.tableWidget.setColumnWidth(4,100)
    banco_dados.tableWidget.setColumnWidth(5, 220)
    banco_dados.tableWidget.setColumnWidth(6, 130)
    for i in range(0, len(contagem)):
        for j in range(0, 7):
            banco_dados.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(contagem[i][j])))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    banco_dados = uic.loadUi("user-visualizar.ui")
    users = uic.loadUi("user-registro.ui")
    banco_dados.pushButton_2.clicked.connect(open_inserir)
    users.pushButton.clicked.connect(inserir)
    visualizar_users()
    app.exec()
