from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from logger import LogManagement
import operator

class MeuApp(QMainWindow):
    num1 = 0
    num2 = 0
    numResult = 0
    op = None
    operacoes = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }


    def __init__(self):
        super().__init__()
        loadUi('interface.ui', self)
        self.setAcoes()


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
        
        self.btnAdicao.clicked.connect(lambda: self.definirOperacao("+"))
        self.btnSubtracao.clicked.connect(lambda: self.definirOperacao("-"))
        self.btnMultiplicacao.clicked.connect(lambda: self.definirOperacao("*"))
        self.btnDivisao.clicked.connect(lambda: self.definirOperacao('/'))

        self.btnLimpar.clicked.connect(self.limparDisplay)
        self.btnInverter.clicked.connect(self.inverter)
        self.btnPorcentagem.clicked.connect(self.porcentagem)

        self.btnResultado.clicked.connect(self.mostraResultado)
        
    
    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.entrada.setText( value )


    def pegarDisplay(self):
        value = self.entrada.text()
        value = value.replace(',', '.')
        try:value = int(value)
        except:value = float(value)
        return value


    def btnClicado1(self, btn):
        if self.pegarDisplay() == 0:
            self.mostrarDisplay( btn.text() )
        else:
            ultimoValor = str( self.pegarDisplay() )
            self.mostrarDisplay(ultimoValor + btn.text())



    def btnClicado(self, btn):
        #Digitando virgula
        if btn.text() == ',':
            if isinstance(self.pegarDisplay(), int):
                ultimoValor = str( self.pegarDisplay() )
                self.mostrarDisplay( ultimoValor + btn.text() )

        #Digitando numeros
        else:
            # Se for numero inteiros
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    self.mostrarDisplay( btn.text() )
                else:
                    ultimoValor = str( self.pegarDisplay() )
                    self.mostrarDisplay(ultimoValor + btn.text())
            
            # Se for numero float
            else:
                if self.entrada.text()[-1] == ",":
                    ultimoValor = self.entrada.text()
                    self.mostrarDisplay(ultimoValor + btn.text())
                
                else:
                    ultimoValor = str( self.pegarDisplay() )
                    self.mostrarDisplay(ultimoValor + btn.text())



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
        self.op = self.operacoes[operacao]
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)


    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op(self.num1, self.num2)
        else:
            print('nao tem operacao feita')
    

    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()

            self.numResult = self.op(self.num1, self.num2)
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
