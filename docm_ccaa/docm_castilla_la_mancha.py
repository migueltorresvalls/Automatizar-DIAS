# Utilizando chromedriver instalado con brew. Ruta completa: /opt/homebrew/bin/chromedriver
# (Esto cambiará para cada dispositivo)
from selenium.webdriver.chrome.options import Options

from gemini import Gemini
from pdf import Pdf
from declaracion import Declaracion
from excel import Excel
from respuesta import Respuesta
from driver import Driver

from tqdm import tqdm

import time

if __name__ == "__main__":
    # Cargo declaraciones antiguas
    excel = Excel("docm_ccaa/documentos.xlsx", "docm_ccaa/Responsables municipios.xlsx")
    declaraciones = excel.leer_declaraciones()
    declaraciones_nuevas = []

    # Cargo modelo de IA
    gemini = Gemini()

    # Cargo driver de chrome
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    driver = Driver(options)

    # Lanzo driver
    pagina_comienzo = 15
    fila_comienzo = 14
    fila_fin = 21
    pdfs = driver.buscar_castilla_mancha(pagina_comienzo, fila_comienzo, fila_fin)

    # Compruebo si se trata de una resolucion nueva
    for i in pdfs: 
        resp = gemini.lanzar_consulta(i.leer())

        # Parseo respuesta de la IA en un objeto declaracion
        respuesta = Respuesta(i.fecha, i.sumario, i.ruta, resp)
        declaracion = respuesta.parsear()
        
        # Si se trata de una respuesta que no se ha guardado previamente, la añado a la lista. 
        if declaracion not in declaraciones and declaracion.tecnologia != "N/A":
            print(f"\n===Nueva resolución encontrada===\n{declaracion}")
            declaraciones_nuevas.append(declaracion)


    # Escribo respuestas en excel
    excel.escribir_declaraciones(declaraciones_nuevas)

    # Si queremos que mantenga abierto el navegador descomentar siguiente linea
    # time.sleep(1000)
    driver.close()