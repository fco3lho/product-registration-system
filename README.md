# Sistema de registro de produtos
<b>Este programa tem como objetivo simular um registro real de produtos de varejo em um banco de dados utilizando Python 3.9.5, MySQL 5.7.14, QtDesigner e WAMPServer 3.0.6.</b>

## Importação de bibliotecas Python
Para Windows, abra o Prompt de Comando e insira os seguintes comandos:
```
  pip install PyQt5
  pip install mysql-connector-python
  pip install reportlab
```

## Criação interface QtDesigner
Crie suas interfaces à seu gosto desde que as mesmas tenham todos os botões e campos necessários para inserir os dados dos produtos a serem registrados, excluídos ou editados, e salve oo códigos das interfaces no mesmo diretório que o código Python que dará vida as interfaces.

## Criação de um banco de dados
<b>1</b> - Após a instalação do WAMPServer 3.0.6, execute o WAMPServer e aguarde todos os serviços estarem executando.</br>

<b>2</b> - Abra o Prompt de Comando e execute o comando ```C:\wamp64\bin\mysql\mysql5.7.14\bin\mysql.exe mysql -u root -p -h localhost``` se a instalação do WAMPServer foi para o diretório padrão, se não basta alterar o diretório do comando.</br>

<b>3</b> - Se tudo ocorrer bem, aparecerá a seguinte mensagem no seu terminal: ```Enter password: ```. Basta pressionar Enter, pois para adentrar ao terminal MySQL não é necessário uma senha.</br>

<b>4</b> - Após entrar ao terminar MySQL, insira o comando ```create database product_registration``` para criar um banco de dados no servidor.</br>

<b>5</b> - Para utilizar o banco de dados criado, insira o comando ```use product_registration```.</br>

<b>6</b> - Para criar uma tabela dentro do banco de dados criado, insira o seguinte comando:
```
CREATE TABLE produtos (
     id INT NOT NULL AUTO_INCREMENT,
     codigo INT,
     descricao VARCHAR(50),
     preco DOUBLE,
     categoria VARCHAR(25),
     PRIMARY KEY (id)

);
```
<b>Feito todos esses processos, você terá criado um banco de dados e uma tabela dentro do banco de dados, que será utilizada para salvar os produtos inseridos na interface do programa.</b>

## Uso de um ambiente virtual (venv)
<b>Foi upado um ambiente virtual do programa, para caso ocorra a clonagem do repositório ou download dos códigos para uso, não haja conflito de versões em diferentes sistemas.</b>
