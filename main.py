from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from os import path

class MeuApp(QMainWindow):
    num1 = 0
    num2 = 0
    numResult = 0
    op = None

    def __init__(self):
        super().__init__()
        loadUi( self.localPath('interface.ui'), self)
        self.setAcoes()

    def localPath(self, relativo):
        return f'{path.dirname(path.realpath(__file__))}\\{relativo}'

    def setAcoes(self):
        self.btn0.clicked.connect(lambda: self.btnClicado(self.btn0))
        self.btn1.clicked.connect(lambda: self.btnClicado(self.btn1))
        self.btn2.clicked.connect(lambda: self.btnClicado(self.btn2))
        self.btn3.clicked.connect(lambda: self.btnClicado(self.btn3))
        self.btn4.clicked.connect(lambda: self.btnClicado(self.btn4))
        self.btn5.clicked.connect(lambda: self.btnClicado(self.btn5))
        self.btn6.clicked.connect(lambda: self.btnClicado(self.btn6))
        self.btn7.clicked.connect(lambda: self.btnClicado(self.btn7))
        self.btn8.clicked.connect(lambda: self.btnClicado(self.btn8))
        self.btn9.clicked.connect(lambda: self.btnClicado(self.btn9))
        self.btnVirgula.clicked.connect(lambda: self.btnClicado(self.btnVirgula))
        
        self.btnAdicao.clicked.connect(lambda: self.definirOperacao(self.adicao))
        self.btnSubtracao.clicked.connect(lambda: self.definirOperacao(self.subtracao))
        self.btnMultiplicacao.clicked.connect(lambda: self.definirOperacao(self.multiplicacao))
        self.btnDivisao.clicked.connect(lambda: self.definirOperacao(self.divisao))

        self.btnPorcentagem.clicked.connect(self.porcentagem)
        self.btnInverter.clicked.connect(self.inverter)

        self.btnResultado.clicked.connect(self.mostraResultado)
        self.btnLimpar.clicked.connect(self.limparDisplay)
        
    
    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.entrada.setText( value )


    def pegarDisplay(self):
        value = self.entrada.text()
        value = value.replace(',', '.')
        try:value = int(value)
        except:value = float(value)
        return value


    def btnClicado(self, btn):
        ultimoValor = str( self.pegarDisplay() )
        #Digitando virgula
        if btn.text() == ',':
            if isinstance(self.pegarDisplay(), float):
                return
        #Digitando numeros
        else:
            # Se for numero inteiros
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    ultimoValor = ''
            # Se for numero float
            else:
                if self.entrada.text()[-1] == ",":
                    ultimoValor = self.entrada.text()
        self.mostrarDisplay(ultimoValor + btn.text())


    def adicao(self):
        print(f'Soma({self.num1}+{self.num2}) = ', end='')
        return self.num1 + self.num2


    def subtracao(self):
        print(f'Sub({self.num1} - {self.num2})= ', end='')
        return self.num1 - self.num2


    def multiplicacao(self):
        print(f'Mult({self.num1} * {self.num2})= ', end='')
        return self.num1 * self.num2


    def divisao(self):
        print(f'Div({self.num1} / {self.num2})= ', end='')
        return self.num1 / self.num2
    

    def porcentagem(self):
        percento = self.pegarDisplay() / 100
        if self.op == self.adicao or self.op == self.subtracao:
            percento = self.num1 * percento
        self.mostrarDisplay(percento)


    def inverter(self):
        numAtual = self.pegarDisplay()
        numAtual *= -1
        self.mostrarDisplay(numAtual)


    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)


    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()
        else:
            print('nao tem operacao feita')
    

    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()

            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)
            print(self.numResult)
        

    def limparDisplay(self):
        self.num1 = 0
        self.num2 = 0
        self.numResult = 0
        self.op = None
        self.mostrarDisplay(0)



if __name__ == '__main__':
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()
