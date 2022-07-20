from time import strftime
from tkinter.messagebox import YES
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import mysql.connector
from pip import main
from reportlab.pdfgen import canvas
from tkinter import *
import inicial

cnx = mysql.connector.connect(
    host="localhost",
    database="banco-empresa",
    user="root",
    password="",
)

def checagem_dados(self):
    cursor = cnx.cursor()
    user = login.lineEdit.text()
    passw = login.lineEdit_2.text()
    sql = ("SELECT log_nome, log_email, log_data_criacao FROM login  WHERE log_usuario ='{}' and log_senha ='{}'".format(user, passw))
    cursor.execute(sql,)
    resultado = cursor.fetchall()
   

    if resultado == "" or user =="" or passw=="":
        msg = QMessageBox()
        msg.setWindowTitle("Sistema YanCode")
        msg.setText("MENSAGEM DO SISTEMA")
        msg.setInformativeText("PRENCHA TODOS OS CAMPOS PARA ENTRAR NO SISTEMA!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    elif resultado:
        nome = resultado[0][0]
        data = resultado[0][2]
        email = resultado[0][1]
        QMessageBox.information(QMessageBox(), "Sistema YanCode", "Você foi logado com sucesso, seja Bem-Vindo {} ao sistema!".format(nome))
        inicial.inicial_tela(nome, email, str(data))
        login.close()
        

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Sistema YanCode")
        msg.setText("MENSAGEM DO SISTEMA")
        msg.setInformativeText("Usuário ou senha digitados estão incorretos, insira-os novamente!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    

    
    

app = QtWidgets.QApplication([])
login = uic.loadUi("login-inicial.ui")
login.pushButton.clicked.connect(checagem_dados)


login.show()
app.exec()