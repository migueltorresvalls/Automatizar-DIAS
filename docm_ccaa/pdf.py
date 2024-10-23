import requests
from io import BytesIO
from PyPDF2 import PdfReader

# Clase que se utiliza para acceder a los pdfs online y leerlos. 

class Pdf:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def leer(self):
        respuesta = requests.get(self.ruta)
        if respuesta.status_code == 200:
            contenido = BytesIO(respuesta.content)
            lector = PdfReader(contenido)
            pdf = ""
            for pagina in lector.pages:
                pdf += pagina.extract_text()
            return pdf
        else:
            return "Ha habido un error al descargar el pdf"
