from PyQt5 import uic, QtWidgets
import mysql.connector

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

app = QtWidgets.QApplication([])
form = uic.loadUi("form window.ui")
show_products = uic.loadUi("show products.ui")
form.pushButton.clicked.connect(mainFunction)
form.pushButton_2.clicked.connect(call_show_products)

form.show()
app.exec()
