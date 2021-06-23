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

number_id = None #Serves to exchange information in different functions / Global variable.

#Main function
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

#Deleting data
def delete_data():
    
    #Deleting in window "show_products.ui"
    line = show_products.tableWidget.currentRow()
    show_products.tableWidget.removeRow(line)

    #Deleting in database "produtos"
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    data_read = cursor.fetchall()
    value_id = data_read[line][0]
    cursor.execute("DELETE FROM produtos WHERE id=" + str(value_id))

#Editing data
def data_edit():
    global number_id

    line = show_products.tableWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    data_read = cursor.fetchall()
    value_id = data_read[line][0]
    cursor.execute("SELECT * FROM produtos WHERE id=" + str(value_id))
    product = cursor.fetchall()

    number_id = value_id

    data_editor.show()
    data_editor.lineEdit.setText(str(product[0][0]))
    data_editor.lineEdit_2.setText(str(product[0][1]))
    data_editor.lineEdit_3.setText(str(product[0][2]))
    data_editor.lineEdit_4.setText(str(product[0][3]))
    data_editor.lineEdit_5.setText(str(product[0][4]))

#Saving edited data
def data_save():
    global number_id

    #Values ​​entered in lineEdit.
    codigo = data_editor.lineEdit_2.text()
    descricao = data_editor.lineEdit_3.text()
    preco = data_editor.lineEdit_4.text()
    categoria = data_editor.lineEdit_5.text()

    #Updating data in database
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria = '{}' WHERE id = {}".format(codigo, descricao, preco, categoria, number_id))

    #Updating data in windows
    show_products.close()
    data_editor.close()
    call_show_products()

#Connecting buttons and windows with functions
app = QtWidgets.QApplication([])
form = uic.loadUi("form window.ui")
show_products = uic.loadUi("show products.ui")
data_editor = uic.loadUi("data edit.ui")

form.pushButton.clicked.connect(mainFunction)
form.pushButton_2.clicked.connect(call_show_products)
show_products.pushButton.clicked.connect(create_pdf)
show_products.pushButton_2.clicked.connect(delete_data)
show_products.pushButton_3.clicked.connect(data_edit)
data_editor.pushButton_3.clicked.connect(data_save)

#Show windows
form.show()
app.exec()