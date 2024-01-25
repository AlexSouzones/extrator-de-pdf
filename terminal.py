from PyPDF2 import PdfReader
import extrator
from datetime import datetime
from PySide6.QtWidgets import QLabel

hora_atual = datetime.now()
hora_atual = hora_atual.strftime("%H:%M")
logs = []

def app_logs(text, label):
  texto = ""
  if len(logs) == 10:
    logs.pop(0)
  logs.append(text)
  for log in logs:
    texto = f"{texto}\n{log}"
  label.setText(texto)
