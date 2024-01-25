from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QProgressBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, QTimer
import json
import terminal
import extrator
import planilha as excel_core

estilo_button = 'font-size: 30px;'
caminho_json = "assets/json/pastas.json"
planilhas = ""
projetos = ""
with open(caminho_json, 'r') as arquivo:
    dados = json.load(arquivo)
    projetos = dados["projetos"]
    planilha = dados["planilha"]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        
        self.progress_bar = QProgressBar(self)

        box_principal = QLabel("", self)
        box_principal.setStyleSheet("border: 2px solid black;")
        box_principal.setGeometry(5, 200, 950, 700)

        box_logs = QLabel("", self)
        box_logs.setStyleSheet("border: 2px solid black;")
        box_logs.setGeometry(1000, 200, 850, 700)

        logs = QLabel("", self)
        logs.setStyleSheet("border: 2px solid black; font-size: 20px; padding: 10px;")
        logs.setGeometry(1100, 250, 680, 500)

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('Extração de projetos - AV2')

        caminho_projetos = QLabel(projetos, self)
        caminho_projetos.setStyleSheet("border: 1px solid black;")
        caminho_projetos.setGeometry(50, 400, 400, 50)

        caminho_planilha = QLabel(planilha, self)
        caminho_planilha.setStyleSheet("border: 1px solid black;")
        caminho_planilha.setGeometry(500, 400, 400, 50)

        self.texto_log = logs
        self.caminho_projetos_label = caminho_projetos
        self.caminho_planilhas_label = caminho_planilha

        btn_select_path_project = QPushButton('Selecionar Pasta de Projetos', self)
        btn_select_path_project.setGeometry(50, 500, 400, 50)
        btn_select_path_project.clicked.connect(self.selecionar_pasta_projeto)
        btn_select_path_project.setStyleSheet(estilo_button)

        icone_pasta = QIcon('assets/icons/pasta.png')
        btn_select_path_project.setIcon(icone_pasta)

        btn_select_path_planilha = QPushButton('Selecionar Pasta de Planilhas', self)
        btn_select_path_planilha.setGeometry(500, 500, 400, 50)
        btn_select_path_planilha.clicked.connect(self.selecionar_pasta_planilha)
        btn_select_path_planilha.setStyleSheet(estilo_button)

        icone_pasta = QIcon('assets/icons/excel.png')
        btn_select_path_planilha.setIcon(icone_pasta)

        btn_extrair = QPushButton('Extrair Dados', self)
        btn_extrair.setGeometry(280, 700, 350, 50)
        btn_extrair.setStyleSheet('font-size: 35px;')

        btn_extrair.clicked.connect(self.extrair_dados)

    def selecionar_pasta_projeto(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta Dos Projetos", options=options)

        if folder_path:
            self.caminho_projetos_label.setText(folder_path)
            with open(caminho_json, 'r') as arquivo:
                dados = json.load(arquivo)

            dados['projetos'] = f'{self.caminho_projetos_label.text()}'
            with open(caminho_json, 'w') as arquivo:
                json.dump(dados, arquivo, indent=2)

    def selecionar_pasta_planilha(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta Dos Projetos", options=options)

        if folder_path:
            self.caminho_planilhas_label.setText(folder_path)
            with open(caminho_json, 'r') as arquivo:
                dados = json.load(arquivo)

            dados['planilha'] = f'{self.caminho_planilhas_label.text()}'
            with open(caminho_json, 'w') as arquivo:
                json.dump(dados, arquivo, indent=2)


    def extrair_dados(self):
        self.texto_log.setText("")
        verificar_planilha = extrator.verificar_caminho(self.caminho_planilhas_label.text())
        terminal.app_logs(f"{verificar_planilha[1]} PLANILHAS.", self.texto_log)
        verificar_projeto = extrator.verificar_caminho(self.caminho_projetos_label.text())
        terminal.app_logs(f"{verificar_projeto[1]} PROJETOS.", self.texto_log)

        if verificar_projeto[0] and verificar_planilha[0]:
            terminal.app_logs(f"Criando planilha...",  self.texto_log)
            excel_core.criar_planilha(self.caminho_planilhas_label.text())
            terminal.app_logs(f"Contabilizando projetos...",  self.texto_log)
            self.projetos = extrator.catalogar_projetos(self.caminho_projetos_label.text())
            terminal.app_logs(f"Total de arquivos: {len(self.projetos)}",   self.texto_log)
            terminal.app_logs(f"Iniciando extração . . .",   self.texto_log)
            extrator.carregar_projetos(self.projetos, self.texto_log, self.caminho_projetos_label.text())
            terminal.app_logs(f"extração finalizada!",   self.texto_log)
      
            

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
