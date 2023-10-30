import os 
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
  "imagens": [".png", ",jpg"],
  "planilhas": ["xlsx"],
  "pdfs": [".pdf"],
  "cvs": [".csv"]
}