from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QProgressBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, QTimer
from datetime import datetime
import terminal
import extrator

estilo_button = 'font-size: 30px;'
hora_atual = datetime.now()
hora_atual = hora_atual.strftime("%H:%M:%S")

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

        caminho_projetos = QLabel("extração de AV2/AV2", self)
        caminho_projetos.setStyleSheet("border: 1px solid black;")
        caminho_projetos.setGeometry(50, 400, 400, 50)

        caminho_planilha = QLabel("extração de AV2/planilhas", self)
        caminho_planilha.setStyleSheet("border: 1px solid black;")
        caminho_planilha.setGeometry(500, 400, 400, 50)

        self.texto_log = logs
        self.caminho_projetos_label = caminho_projetos
        self.caminho_planilhas_label = caminho_planilha

        # Botão para abrir o diálogo de seleção de pasta
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

        # Diálogo para seleção de pasta
        folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta Dos Projetos", options=options)

        if folder_path:
            print(f"Pasta selecionada: {folder_path}")
            self.caminho_projetos_label.setText(folder_path)

    def selecionar_pasta_planilha(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        # Diálogo para seleção de pasta
        folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta Dos Projetos", options=options)

        if folder_path:
            print(f"Pasta selecionada: {folder_path}")
            self.caminho_planilhas_label.setText(folder_path)


    def extrair_dados(self):
        verificar_planilha = extrator.verificar_caminho(self.caminho_planilhas_label.text())
        self.texto_log.setText(terminal.app_logs(f"PLANILHA: {verificar_planilha[1]} {hora_atual}"))
        verificar_projeto = extrator.verificar_caminho(self.caminho_projetos_label.text())
        self.texto_log.setText(terminal.app_logs(f"PROJETO: {verificar_projeto[1]} {hora_atual}"))
      
    # def start_progress(self):
    #     # Configurar o temporizador para atualizar a barra de progresso a cada 100 ms
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.update_progress)
    #     self.timer.start(100)

    def update_progress(self):
        # Atualizar o valor da barra de progresso
        current_value = self.progress_bar.value()
        new_value = current_value + 1
        self.texto_log.setText(terminal.app_logs(new_value))

        if new_value > 100:
            new_value = 0  # Reiniciar quando atingir 100%

        self.progress_bar.setValue(new_value)
            

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.progress_bar.move(1100, 800)
    window.progress_bar.setFixedHeight(50)
    window.progress_bar.setFixedWidth(680)
    window.progress_bar.setStyleSheet("border-radius: 15px; border: 2px solid black;")
    window.show()
    app.exec()
