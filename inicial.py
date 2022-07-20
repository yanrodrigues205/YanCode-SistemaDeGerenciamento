from http import client
from time import strftime
from tkinter.messagebox import YES
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QTableWidget, QVBoxLayout
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
nome = []
valor = []


def produtos_setor():
    tela_inicial.close()
    tela_inicial.show()
    lista = tela_inicial.comboBox.currentText()
    cursor = cnx.cursor()
    sql = (f"SELECT * FROM produtos WHERE prod_tipo LIKE '%{lista}%'")
    cursor.execute(sql)
    contar_linhas = cursor.fetchall()
    tela_inicial.tableWidget.setRowCount(len(contar_linhas))
    tela_inicial.tableWidget.setColumnCount(5)
    tela_inicial.tableWidget.setColumnWidth(0, 10)
    tela_inicial.tableWidget.setColumnWidth(1,145)
    tela_inicial.tableWidget.setColumnWidth(2,50)
    tela_inicial.tableWidget.setColumnWidth(3,70)
    tela_inicial.tableWidget.setColumnWidth(4,90)
    for i in range(len(contar_linhas)):
        for y in range(0, 5):
            tela_inicial.tableWidget.setItem(i, y, QtWidgets.QTableWidgetItem(str(contar_linhas[i][y])))

def produtos_lista():
    cursor = cnx.cursor()
    pesquisa = tela_inicial.lineEdit.text()
    if pesquisa == "":
        sql = ("SELECT * FROM produtos")
    else:
        sql = (f"SELECT * FROM produtos WHERE prod_nome LIKE '%{pesquisa}%' or prod_marca LIKE '%{pesquisa}%'")
    cursor.execute(sql)
    contar_linhas = cursor.fetchall()
    tela_inicial.tableWidget.setRowCount(len(contar_linhas))
    tela_inicial.tableWidget.setColumnCount(5)
    tela_inicial.tableWidget.setColumnWidth(0, 10)
    tela_inicial.tableWidget.setColumnWidth(1,145)
    tela_inicial.tableWidget.setColumnWidth(2,50)
    tela_inicial.tableWidget.setColumnWidth(3,70)
    tela_inicial.tableWidget.setColumnWidth(4,90)
    for i in range(len(contar_linhas)):
        for y in range(0, 5):
            tela_inicial.tableWidget.setItem(i, y, QtWidgets.QTableWidgetItem(str(contar_linhas[i][y])))


def inicial_tela(nome, email, data):
    tela_inicial.label_4.setText(nome)
    tela_inicial.label_5.setText(email)
    tela_inicial.label_6.setText(data)
    tela_inicial.show()
    app.exec()    
  
def cadastro_usuario():
    call(["python", "users_estrutura.py"])

def contratar_func():
    call(["python", "estrutura.py"]) 

unidade = []
quantidade = 1

def adicionar_carrinho():
    global quantidade
    linha_selecionada = tela_inicial.tableWidget.currentRow()
    cursor = cnx.cursor()
    cursor.execute("SELECT prod_id FROM produtos")
    leitura = cursor.fetchall()
    id = leitura[linha_selecionada][0]
    cursor.execute("SELECT * FROM produtos WHERE prod_id = "+str(id))
    produto = cursor.fetchall()
    tela_inicial.tableWidget_2.setColumnCount(3)
    cliente = produto[0][1]
    
    if cliente in nome:
        quantidade = quantidade + 1
        if len(nome) >= 2: 
            quantidade = 1
            for i in range(0, len(nome)):
                tela_inicial.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(quantidade))) 
        else:
            for i in range(0, len(nome)):
                tela_inicial.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(quantidade)))       
    else:
        nome.append(cliente)
        tela_inicial.tableWidget_2.setRowCount(len(nome))
        valor.append(produto[0][2])
        for i in range(0, len(nome)):
            print(nome[i])
            tela_inicial.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(nome[i])))
                
        for i in range(0, len(nome)):
            tela_inicial.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(quantidade)))
        
            
        for i in range(0, len(valor)):
            print(valor[i])
            tela_inicial.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(valor[i])))
           
        
        
 
        

def visualizar_clientes():
    cliente.show()
    linha_click = cliente.tableWidget.currentRow()
    cursor = cnx.cursor()
    sql = ("SELECT * FROM clientes")
    cursor.execute(sql)
    contar_dados = cursor.fetchall()
    cliente.tableWidget.setRowCount(len(contar_dados))
    for i in range(0, len(contar_dados)):
        for y in range(0, 8):
            cliente.tableWidget.setItem(i, y, QtWidgets.QTableWidgetItem(str(contar_dados[i][y])))
def sair():
    msg = QMessageBox()
    msg.setWindowTitle("Sistema YanCode")
    msg.setText("MENSAGEM DO SISTEMA")
    msg.setInformativeText("Você realmente deseja sair do sistema?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    resposta = msg.exec_()
    if resposta == QMessageBox.Yes:
        exit()
    else:
        print("clicou no botão sair, mas recusou a saída")    
    
def selecionar_cliente():
    linha = cliente.tableWidget.currentRow()
    cursor = cnx.cursor()
    cursor.execute("SELECT cli_id from clientes")
    leitura = cursor.fetchall()
    id = leitura[linha][0]
    cursor.execute("SELECT * FROM clientes WHERE cli_id="+ str(id))
    cliente_selecionado = cursor.fetchall()
    cli_id = str(cliente_selecionado[0][0])
    cli_nome = str(cliente_selecionado[0][1])
    tela_inicial.lineEdit_2.setText(cli_id)
    tela_inicial.lineEdit_3.setText(cli_nome)
    cliente.close()

def finalizar(self):
    super.finalizar()
    layout = QVBoxLayout()
    self.setLayout(layout)

    table = QTableWidget

app = QtWidgets.QApplication([])
login = uic.loadUi("login-inicial.ui")
tela_inicial = uic.loadUi("tela-inicial.ui")
finalizar_compra = uic.loadUi("finalizar_compra.ui")
cliente = uic.loadUi("clientes-visualizar.ui")
produtos_lista()

cliente.pushButton.clicked.connect(selecionar_cliente)
tela_inicial.pushButton_8.clicked.connect(produtos_lista)
tela_inicial.pushButton_12.clicked.connect(produtos_setor)
tela_inicial.pushButton_11.clicked.connect(sair)
tela_inicial.pushButton_3.clicked.connect(cadastro_usuario)
tela_inicial.pushButton_4.clicked.connect(contratar_func)
tela_inicial.pushButton_5.clicked.connect(visualizar_clientes)
tela_inicial.pushButton_9.clicked.connect(adicionar_carrinho)
tela_inicial.pushButton_14.clicked.connect(finalizar)







