from PyPDF2 import PdfReader
import extrator
from datetime import datetime
from PySide6.QtWidgets import QLabel

hora_atual = datetime.now()
hora_atual = hora_atual.strftime("%H:%M")

# reader = PdfReader("AV2/AV2 O PEQUENO PRINCÍPE.ALUNO LUCIMARA DA SILVA RELATÓRIO DE INTERVENÇÃO - (DISCIPLINA DE EXTENSÃO - DISCENTE).pdf")
# number_of_pages = len(reader.pages)
# text = ""
# for pagina in range(0, number_of_pages):
#   page = reader.pages[pagina]
#   text = text + page.extract_text()

# extrator.extrair_info(text)
# print(text)

logs = []

def app_logs(text, label):
  texto = ""
  if len(logs) == 10:
    logs.pop(0)
  logs.append(text)
  for log in logs:
    texto = f"{texto}\n{log}"
  label.setText(texto)
