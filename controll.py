from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

#Connecting database
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "product_registration"
)

def mainFunction():
    codigo = form.lineEdit.text()
    descricao = form.lineEdit_2.text()
    preco = form.lineEdit_3.text()
    categoria = ""

    print("Código:", codigo)
    print("Descrição:", descricao)
    print("Preço: R$", preco)

    if form.radioButton.isChecked():
        categoria = "Periféricos"
        print("Categoria:", categoria)
    elif form.radioButton_2.isChecked():
        categoria = "Hardware"
        print("Categoria:", categoria)
    elif form.radioButton_3.isChecked():
        categoria = "Acessórios"
        print("Categoria:", categoria)
    
    cursor = banco.cursor()
    command_sql = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    data = (str(codigo), str(descricao), str(preco), categoria)
    cursor.execute(command_sql, data)
    banco.commit()

    #Cleaning fields
    form.lineEdit.setText("")
    form.lineEdit_2.setText("")
    form.lineEdit_3.setText("")
    
    print("")

#Function to show product list screen
def call_show_products():
    show_products.show()
    cursor = banco.cursor()
    command_sql = "SELECT * FROM produtos"
    cursor.execute(command_sql)
    data_read = cursor.fetchall()

    #Create the table in window "show products.ui"
    show_products.tableWidget.setRowCount(len(data_read))
    show_products.tableWidget.setColumnCount(5)

    #Implementing database elements
    for i in range(0, len(data_read)):
        for j in range(0, 5):
            show_products.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data_read[i][j])))

#Function to create PDF of products
def create_pdf():
    cursor = banco.cursor()
    command_sql = "SELECT * FROM produtos"
    cursor.execute(command_sql)
    data_read = cursor.fetchall()
    y = 0

    pdf = canvas.Canvas("Cadastro de produtos.pdf")
    pdf.setFont("Times-Bold", 20)
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "CODIGO")
    pdf.drawString(210, 750, "PRODUTO")
    pdf.drawString(310, 750, "PREÇO")
    pdf.drawString(410, 750, "CATEGORIA")

    for i in range(0, len(data_read)):
        y += 50
        pdf.drawString(10, 750 - y, str(data_read[i][0]))
        pdf.drawString(110, 750 - y, str(data_read[i][1]))
        pdf.drawString(210, 750 - y, str(data_read[i][2]))
        pdf.drawString(310, 750 - y, str(data_read[i][3]))
        pdf.drawString(410, 750 - y, str(data_read[i][4]))

    pdf.save()
    print("PDF saved successfully.")

app = QtWidgets.QApplication([])
form = uic.loadUi("form window.ui")
show_products = uic.loadUi("show products.ui")
form.pushButton.clicked.connect(mainFunction)
form.pushButton_2.clicked.connect(call_show_products)
show_products.pushButton.clicked.connect(create_pdf)

form.show()
app.exec()
