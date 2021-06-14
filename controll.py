from PyQt5 import uic, QtWidgets

def mainFunction():
    codigo = form.lineEdit.text()
    descricao = form.lineEdit_2.text()
    preco = form.lineEdit_3.text()

    print("Código:", codigo)
    print("Descrição:", descricao)
    print("Preço: R$", preco)

    if form.radioButton.isChecked():
        print("Categoria: Periféricos")
    elif form.radioButton_2.isChecked():
        print("Categoria: Hardware")
    elif form.radioButton_3.isChecked():
        print("Categoria: Acessórios")
    
    print("")

app = QtWidgets.QApplication([])
form = uic.loadUi("form window.ui")
form.pushButton.clicked.connect(mainFunction)

form.show()
app.exec()