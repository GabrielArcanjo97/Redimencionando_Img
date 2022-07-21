import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QFileDialog # vai pegar a imagem
from PyQt5.QtGui import QPixmap # vai maniplar a imagem


# Criando a classe e importando a classe de design para construir o design da janela que precisa
class RedimencioarImg(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self) #função da classe Ui_MainWindow do design
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem) #está ativando o botão btnEscolherArquivo e selecionar imagem
        self.btnRedimencionar.clicked.connect(self.redimencionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'/home/gabriel.morais/Imagens'
            #options=QFileDialog.DontUseNativeDialog
        )
        #abrir a imagem
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem) #criando uma imagem original para não afetar a imagem original quando alterar alguma coisa
        self.labelImg.setPixmap(self.original_img) # adicionando a imagem no labelImg
        self.inputLargura.setText(str(self.original_img.width())) # pegando largura da imagem original, a setText espera uma string, e o width retorna um int
        self.inputAltura.setText(str(self.original_img.height())) # pegando altura da imagem original, a setText espera uma string, e o height retorna um int


    #Redimenconando imagem e salvando, sem alter a imagem original
    def redimencionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap((self.nova_imagem))
        self.inputLargura.setText(str(self.nova_imagem.width())) # pegando largura da imagem original, a setText espera uma string, e o width retorna um int
        self.inputAltura.setText(str(self.nova_imagem.height())) # pegando altura da imagem original, a setText espera uma string, e o height retorna um int

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'/home/gabriel.morais/Desktop'
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')

# Instanciando a classe RedimencioarImg e falando para ela mostrar a janela construida
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimencionar = RedimencioarImg()
    redimencionar.show()
    qt.exec_()

