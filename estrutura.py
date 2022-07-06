from time import strftime
from tkinter.messagebox import YES
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import mysql.connector
from pip import main
from reportlab.pdfgen import canvas


numero_id = 0
func_qtd = 0

cnx = mysql.connector.connect(
    host="localhost",
    database="banco-empresa",
    user="root",
    password="",
)


def inserir_dados():
    cursor = cnx.cursor()
    nome = formulario.lineEdit.text()
    sobrenome = formulario.lineEdit_2.text()
    rg = formulario.lineEdit_3.text()
    cpf = formulario.lineEdit_4.text()
    residencia_rua = formulario.lineEdit_5.text()
    residencia_n = formulario.lineEdit_6.text()
    email = formulario.lineEdit_7.text()
    telefone = formulario.lineEdit_8.text()
    salario = formulario.lineEdit_9.text()
    cargo = formulario.comboBox.currentText()
    data = date.today()
    data_org = data.strftime('%d/%m/%y')
    print(data_org)

    cursor = cnx.cursor()
    sql = ('INSERT INTO funcionarios (func_nome,func_sobrenome, func_rg, func_cpf, func_resid_rua, func_resid_n,'
    'func_email,func_telefone,func_salario, func_cargo, func_data_contrato)'
    ' VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)')
    dados = (str(nome),str(sobrenome),rg, cpf, str(residencia_rua), residencia_n, str(email), telefone, salario,cargo,data)
    cursor.execute(sql, dados)
    cnx.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_7.setText("")
    QMessageBox.information(QMessageBox(), "Sistema YanCode", "O funcionário foi contratado com sucesso!")
    
def imprimir_dados():
   
   cursor = cnx.cursor()
   sql = "SELECT * FROM funcionarios"
   cursor.execute(sql)
   leitura_dados = cursor.fetchall()
   y = 0
   pdf = canvas.Canvas("pdf-funcionários/funcionários_contratados.pdf")
   pdf.setFont("Times-Bold", 21)
   pdf.drawString(20,800, "Banco de Dados Empresarial - Funcionários")
   pdf.setFont("Times-Bold", 13)
   pdf.drawString(0, 750, "ID")
   pdf.drawString(20, 750, "Nome")
   pdf.drawString(100, 750, "CPF")
   pdf.drawString(160, 750, "RG")
   pdf.drawString(210, 750, "Email")
   pdf.drawString(350, 750, "Salário")
   pdf.drawString(400, 750, "Cargo")
   pdf.drawString(480, 750, "Dia Contratação")
   for i in range(0, len(leitura_dados)):
        global func_qtd
        func_qtd = func_qtd + 1
        y = y + 20
        pdf.setFont("Times-Bold", 10)
        pdf.drawString(0, 750 - y, str(leitura_dados[i][0]))
        pdf.drawString(20, 750 - y, str(leitura_dados[i][1]))
        pdf.drawString(100, 750 - y, str(leitura_dados[i][4]))
        pdf.drawString(160, 750 - y, str(leitura_dados[i][3]))
        pdf.drawString(210, 750 - y, str(leitura_dados[i][7]))
        pdf.drawString(350, 750 - y, str(leitura_dados[i][9]))
        pdf.drawString(400, 750 - y, str(leitura_dados[i][10]))
        pdf.drawString(480, 750 - y, str(leitura_dados[i][11]))
    

   pdf.setFont("Times-Bold", 12) 
   pdf.drawString(20,780, "Quantidade de empregados na empresa=> {}".format(func_qtd))
   pdf.save()
   QMessageBox.information(QMessageBox(), "Sistema YanCode", "O banco de dados foi impresso em um PDF com sucesso! Os arquivos estão no diretório desse sistema na pasta 'pdf-funcionários'.")


def excluir_dados():
    linha = banco_dados.tableWidget.currentRow()

    msg = QMessageBox()
    msg.setWindowTitle("Sistema YanCode")
    msg.setText("DEMITIR FUNCIONÁRIO")
    msg.setInformativeText("Você realmente deseja demitir o funcionário?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    resposta_usuario =msg.exec_()

    if resposta_usuario == QMessageBox.Yes:
        banco_dados.tableWidget.removeRow(linha)
        cursor = cnx.cursor()
        cursor.execute("SELECT func_id from funcionarios")
        dados_lidos = cursor.fetchall()
        posicao_no_array = dados_lidos[linha][0]
        valor_id = posicao_no_array
        cursor.execute("DELETE FROM funcionarios WHERE func_id="+ str(valor_id))
        QMessageBox.information(QMessageBox(), "Sistema YanCode", "A demisão do funcinário foi feita com sucesso!")
    else:
        print("nada")


def banco_adicionar_dados():
    formulario.show()
    banco_dados.close()

def alterar_dados():
    global numero_id
    linha_clicada = banco_dados.tableWidget.currentRow()
    cursor = cnx.cursor()
    cursor.execute("SELECT func_id FROM funcionarios")
    dados_lidos = cursor.fetchall()
    posicao_selecionada_array = dados_lidos[linha_clicada][0]
    cursor.execute("SELECT * FROM funcionarios WHERE func_id="+ str(posicao_selecionada_array))
    funcionario = cursor.fetchall()
    #ASSIM QUE A VÁRIAVEL FUNCIONÁRIO CHEGAR ELA VEM DENTRO DE DOIS ARRAYS 
    # ENTÃO É PRECISO SELECIONAR A POSIÇÃO DOS COMPONENTES E DEFINILOS COMO STRING
    numero_id = posicao_selecionada_array
    id = str(funcionario[0][0])
    nome = str(funcionario[0][1])
    sobrenome = str(funcionario[0][2])
    rg = str(funcionario[0][3])
    cpf =str(funcionario[0][4])
    rua = str(funcionario[0][5])
    numero = str(funcionario[0][6])
    email = str(funcionario[0][7])
    telefone = str(funcionario[0][8])
    salario = str(funcionario[0][9])
    cargo = str(funcionario[0][10])

    alterar.lineEdit.setText(id)
    alterar.lineEdit_2.setText(nome)
    alterar.lineEdit_3.setText(sobrenome)
    alterar.lineEdit_4.setText(rg)
    alterar.lineEdit_5.setText(cpf)
    alterar.lineEdit_6.setText(rua)
    alterar.lineEdit_7.setText(numero)
    alterar.lineEdit_8.setText(email)
    alterar.lineEdit_9.setText(telefone)
    alterar.lineEdit_10.setText(salario)
    alterar.lineEdit_11.setText(cargo)
    banco_dados.close()
    
    alterar.show()

def salvar_alterar_dados():
    #TRÁS A POSIÇÃO DO ARRAY DA FUNÇÃO ACIMA
    global numero_id
    nome = alterar.lineEdit_2.text()
    sobrenome = alterar.lineEdit_3.text()
    rg = alterar.lineEdit_4.text()
    cpf = alterar.lineEdit_5.text()
    rua = alterar.lineEdit_6.text()
    numero = alterar.lineEdit_7.text()
    email = alterar.lineEdit_8.text()
    telefone = alterar.lineEdit_9.text()
    salario = alterar.lineEdit_10.text()
    cargo = alterar.lineEdit_11.text()

    msg = QMessageBox()
    msg.setWindowTitle("Sistema Yancode")
    msg.setText("ALTERAR DADOS DO FUNIONÁRIO")
    msg.setInformativeText("Você realmente deseja alterar dados do funcionário do id -> {}".format(numero_id))
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    resposta= msg.exec_()

    if resposta == QMessageBox.Yes:
        cursor = cnx.cursor()
        sql = "UPDATE funcionarios SET func_nome ='{}', func_sobrenome ='{}', func_rg= '{}', func_cpf = '{}', func_resid_rua='{}',func_resid_n='{}',func_email='{}', func_telefone='{}',func_salario='{}', func_cargo='{}' WHERE func_id = '{}'".format(nome,sobrenome,rg,cpf,rua,numero,email,telefone,salario,cargo,numero_id)
        cursor.execute(sql)
        alterar.close()
        visualizar_dados()
    else:
        banco_dados.show()
        
   
    




def visualizar_dados():
    banco_dados.show()
    formulario.close()
    cursor = cnx.cursor()
    pesquisa = banco_dados.lineEdit.text()
    if(pesquisa == ""):
        sql = "SELECT * FROM funcionarios"
    else:
        sql = (f"SELECT * FROM funcionarios WHERE func_nome LIKE '%{pesquisa}%' or func_id LIKE '%{pesquisa}%' or func_sobrenome LIKE '%{pesquisa}%'")
    cursor.execute(sql)
    contar_dados = cursor.fetchall()
    banco_dados.tableWidget.setRowCount(len(contar_dados))
    banco_dados.tableWidget.setColumnCount(12)
    banco_dados.tableWidget.setColumnWidth(0, 50)
    banco_dados.tableWidget.setColumnWidth(1, 150)
    banco_dados.tableWidget.setColumnWidth(2, 100)
    banco_dados.tableWidget.setColumnWidth(3, 80)
    banco_dados.tableWidget.setColumnWidth(4, 80)
    banco_dados.tableWidget.setColumnWidth(5, 210)
    banco_dados.tableWidget.setColumnWidth(6, 50)
    banco_dados.tableWidget.setColumnWidth(7, 210)
    banco_dados.tableWidget.setColumnWidth(11, 130)
    qt =0
    for y in range (0, len(contar_dados)):
        qt = qt + 1
    banco_dados.lineEdit_2.setText(str(qt))
#ESTRUTURA DE REPETIÇÃO QUE CONTA OS DADOS E EXIBE NAS RESPECTIVAS POSIÇÕES
    for i in range(0, len(contar_dados)):
        for j in range(0, 12):
            banco_dados.tableWidget.setItem(i, j,QtWidgets.QTableWidgetItem(str(contar_dados[i][j])))

    
    


app=QtWidgets.QApplication([])
formulario = uic.loadUi("func-registro.ui")
banco_dados = uic.loadUi("func-visualizar.ui")
alterar = uic.loadUi("func-alterar.ui")
formulario.actionVisualizar_Funcion_rios.triggered.connect(visualizar_dados)
formulario.pushButton.clicked.connect(inserir_dados)
banco_dados.pushButton_4.clicked.connect(imprimir_dados)
banco_dados.pushButton.clicked.connect(excluir_dados)
banco_dados.pushButton_8.clicked.connect(banco_adicionar_dados)
banco_dados.pushButton_2.clicked.connect(alterar_dados)
banco_dados.pushButton_5.clicked.connect(visualizar_dados)
alterar.pushButton.clicked.connect(salvar_alterar_dados)


formulario.show()
app.exec()

