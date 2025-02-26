import sys
import io
import os
import pandas as pd
from datetime import date
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve, Qt, QThread, Signal
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from ui_main import Ui_MainWindow

# Classe para redirecionar a saída padrão para um widget de texto na interface gráfica
class OutputRedirector:
    def __init__(self, text_edit_widget):
        self.text_edit_widget = text_edit_widget

    def write(self, text):
        self.text_edit_widget.appendPlainText(text)
        QCoreApplication.processEvents()  # Garante que a interface seja atualizada

    def flush(self):
        pass


# Thread para executar código sem bloquear a interface
class CodeExecutionThread(QThread):
    finished_signal = Signal(dict)  # Emite o ambiente após execução
    error_signal = Signal(str)

    def __init__(self, code, exec_env):
        super().__init__()
        self.code = code
        self.exec_env = exec_env

    def run(self):
        try:
            exec(self.code, self.exec_env)  # Executa o código no ambiente customizado
        except Exception as e:
            self.error_signal.emit(str(e))
        else:
            self.finished_signal.emit(self.exec_env)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sitema Bamboo V-2")
        self.setWindowIcon(QIcon(u""))
        # Informações iniciais
        self.label_data.setText(date.today().strftime("%d/%m/%y"))
        self.label_data.setAlignment(Qt.AlignRight)
        self.label_5.setText(f" Welcome {os.environ.get('USERNAME')}")
        
        # Toggle Button
        self.pushButton.clicked.connect(self.leftMenu_animacao)
        # Páginas do sistema
        self.pushButton_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.pushButton_manipula.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_manipula))
       
        # Selecionar arquivo para tabela
        self.pushButton_arquivo.clicked.connect(self.trocar_dataset)
        self.plainTextEdit_sep.setPlaceholderText(',')
        # Atualizar tabela
        self.pushButton_atualizar.clicked.connect(self.atualizar_dataset)
        
        # Terminal de saída (apenas leitura)
        self.plainTextEdit_output.setReadOnly(True)
        # Botão run para código digitado
        self.pushButton_run.clicked.connect(self.execute_code)

        # Redireciona stdout e stderr para o widget de saída
        sys.stdout = OutputRedirector(self.plainTextEdit_output)
        sys.stderr = OutputRedirector(self.plainTextEdit_output)

        # Ambiente de execução customizado para o exec()
        self.exec_env = {}  # dicionário que manterá variáveis do ambiente

    def execute_code(self):
        code = self.plainTextEdit_input.toPlainText()
        print(f'[].{code}',end='')
        # Injeta o DataFrame (se já carregado) e a própria instância, se necessário
        if hasattr(self, "df"):
            self.exec_env["df"] = self.df
        self.exec_env["self"] = self  # se quiser acessar métodos/atributos da instância
        # Cria e inicia a thread de execução
        self.thread = CodeExecutionThread(code, self.exec_env)
        self.thread.finished_signal.connect(self.on_execution_finished)
        self.thread.error_signal.connect(lambda err: print(f"Erro: {err}"))
        self.thread.start()


    def on_execution_finished(self, env):
        print("Código executado com sucesso!",end='')
        # Se o usuário alterou 'df' no código, atualize a tabela
        if "df" in env:
            self.df = env["df"]
            if self.checkBox_atualizar.isChecked():
                self.atualizar_dataset()


    def info_dataset(self):
        original_stdout = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer
        self.df.info()
        sys.stdout = original_stdout
        info_text = buffer.getvalue()
    
        # Exibir a informação no widget de texto
        self.plainTextEdit_info.setPlainText(info_text)
    
        # Criar e aplicar uma fonte monoespaçada
        font = QFont("Courier New")  # "Consolas" ou "Monospace" podem ser alternativas
        font.setStyleHint(QFont.Monospace)  # Garante que o sistema tente carregar uma fonte monoespaçada
        self.plainTextEdit_info.setFont(font)


    def atualizar_dataset(self):
        self.tableWidget.setRowCount(self.df.shape[0])
        self.tableWidget.setColumnCount(self.df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                item = QTableWidgetItem(str(self.df.iat[row, col]))
                self.tableWidget.setItem(row, col, item)
        self.info_dataset()


    def trocar_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecione um arquivo", "", "Todos os Arquivos (*);;Imagens (*.png *.jpg);;Texto (*.txt)"
        )
        if file_path:
            separador = self.plainTextEdit_sep.toPlainText()
            self.df = pd.read_csv(file_path, sep= separador if separador != '' else ',')
            self.exec_env["df"] = self.df  # Atualiza o ambiente com o DataFrame
            self.atualizar_dataset()


    def leftMenu_animacao(self):
        width = self.frame_menu.width()
        newWidth = 200 if width == 0 else 0
        self.animation = QPropertyAnimation(self.frame_menu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
