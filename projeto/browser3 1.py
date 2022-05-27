from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
# Widgets básicos das janelas
from PyQt5.QtWidgets import *
# Widgets WebEngine para Navegação em internet.
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5 import QtCore

# Inicializa o applicativo
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.setMinimumHeight(720)
        self.setMinimumWidth(1280)
        self.show()
        self.setWindowIcon(QIcon('C:/Users/Everton/Desktop/projeto/chrome.png'))

        Barra_navegacao = QToolBar()
        Barra_navegacao.setMinimumHeight(8)
        Barra_navegacao.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.addToolBar(Barra_navegacao)
        
        backward_button = QAction('<', self)
        backward_button.triggered.connect(self.browser.back)
        Barra_navegacao.addAction(backward_button)
        
        forward_button = QAction('>', self)
        forward_button.triggered.connect(self.browser.forward)
        backward_button.setStatusTip("Avançar")
        Barra_navegacao.addAction(forward_button)

        reload_button = QAction('🗘', self)
        reload_button.triggered.connect(self.browser.reload)
        Barra_navegacao.addAction(reload_button)

        home_button = QAction('🏠', self)
        home_button.triggered.connect(self.botao_home)
        Barra_navegacao.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.barra_navegaurl)
        Barra_navegacao.addWidget(self.url_bar)

        lupa_button = QAction('🔍', self)
        lupa_button.triggered.connect(self.lupa)
        Barra_navegacao.addAction(lupa_button)

        stop_button = QAction('🛑', self)
        stop_button.triggered.connect(self.browser.stop)
        Barra_navegacao.addAction(stop_button)
        self.browser.urlChanged.connect(self.update_url)

    def lupa(self):
        go_url = self.url_bar.text()
        self.browser.setUrl(QUrl(go_url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def botao_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))
        
    def barra_navegaurl(self):
        url = self.url_bar.text()
        self.url_bar.setPlaceholderText("Pesquisar no google ou digitar Url") 
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
app.setApplicationName("chrome de chernobyl")
window = MainWindow()
app.exec_()

