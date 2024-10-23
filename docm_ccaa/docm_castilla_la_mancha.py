# Utilizando chromedriver instalado con brew. Ruta completa: /opt/homebrew/bin/chromedriver
# (Esto cambiará para cada dispositivo)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from gemini import Gemini
from pdf import Pdf
from declaracion import Declaracion
from excel import Excel
from respuesta import Respuesta

from tqdm import tqdm

import time

class Main:
    def __init__(self):
        self.excel = Excel("docm_ccaa/documentos.xlsx")

        self.declaraciones = self.excel.leer_declaraciones()
        self.declaraciones_nuevas = []

    # Crea driver de selnium
    def genera_driver(self, options=Options()):
        # Descomentar siguiente linea si vamos a usar Chrome
        driver = webdriver.Chrome(options=options)

        # Comentar si vaoms a usar Chrome
        # driver = webdriver.Firefox(options=options)

        return driver
            
    # Lee los pdfs web, realiza la pregunta a la IA, recibe la respuesta parseada y decide si se trata de un documento no o uno ya analizado previamente
    def comprobar_nuevos_documentos(self, filas):
            for i in filas: 
                pdf = i.find_element(by=By.CLASS_NAME, value="enlacePDFIndividual")

                # Accedo a fecha publicación
                columnas = i.find_elements(by=By.XPATH, value="td[a/@title='Ver los datos detallados del documento']")
                fecha = columnas[3].find_element(By.XPATH, ".//a").text
                sumario = columnas[2].find_element(By.XPATH, ".//a").text

                # Abro pdf
                # pdf.find_element(by=By.CLASS_NAME, value="new-window").click()
                ruta_pdf = pdf.find_element(by=By.CLASS_NAME, value="new-window").get_attribute("href")

                # Lanzamos consulta
                pdf = Pdf(ruta_pdf)
                resp = self.gemini.lanzar_consulta(pdf.leer())
                # print(f"===Nueva resolución encontrada===\n{resp}")

                # Creamos declaracion de la respuesta de la IA
                respuesta = Respuesta(fecha, sumario, ruta_pdf, resp)
                declaracion = respuesta.parsear()
                
                # Si se trata de una respuesta que no se ha guardado previamente, la añadimos a la lista. 
                if declaracion not in self.declaraciones and declaracion.tecnologia != "N/A":
                    print(f"\n===Nueva resolución encontrada===\n{declaracion}")
                    self.declaraciones_nuevas.append(declaracion)

    # Lanza la pagina web de Castilla y la Mancha, va a la pagina inicial y va llamando a las diferentes funciones para analizar los documentos. Cuando ha terminado con la pagina actual, avanza a la siguiente hasta llegar a la página máxima
    def lanzar_selenium(self, pagina_actual):
        self.driver.get("https://docm.jccm.es/docm/busquedaAvanzada.do")

        text_box = self.driver.find_element(by=By.CLASS_NAME, value="cuadroTextoSumarioBusqueda")
        text_box.send_keys("declaración de impacto ambiental" + Keys.ENTER)

        self.cambiar_pagina(pagina_actual)

        pagina_maxima = pagina_actual + 1
        while (pagina_actual < pagina_maxima):
            self.driver.implicitly_wait(0.5)
            filas_par = self.driver.find_elements(by=By.CLASS_NAME, value="filaPar")
            filas_impar = self.driver.find_elements(by=By.CLASS_NAME, value="filaImpar")
            
            # Hay 50 documentos (25 filas par, 25 filas impar) por página
            self.comprobar_nuevos_documentos(filas_par[7:14])
            self.comprobar_nuevos_documentos(filas_impar[7:14])

            pagina_actual += 1
            self.cambiar_pagina(pagina_actual)

    def cambiar_pagina(self, pagina_nueva):
        pagina_encontrada = False
        cadena = "//a[@title='Ir a la página " + str(pagina_nueva) + "']"

        while (not pagina_encontrada):
            try: 
                boton_pagina_nueva = self.driver.find_element(by=By.XPATH, value=cadena)
                boton_pagina_nueva.click()
                pagina_encontrada = True
            # Comprobamos si hay siguiente página. Si no vamos al bloque siguiente
            except NoSuchElementException: 
                boton_bloque_siguiente = self.driver.find_element(by=By.XPATH, value="//a[@title='Ir al bloque página siguiente']")
                boton_bloque_siguiente.click()

    def inicio(self):
        # Cargo modelo de IA
        self.gemini = Gemini()

        # Cargo driver
        # Descomentar siguiente linea si vamos a usar Chrome
        options = webdriver.ChromeOptions()

        # Comentar si vamos a usar Chrome
        # options = webdriver.FirefoxOptions()

        # Si queremos que muestre interfaz gráfica del navegador, comentar siguiente linea
        options.add_argument("--headless")
        # options.binary_location = ruta al ejecutable geckodriver instalado

        self.driver = self.genera_driver(options)

        # Lanzo selenium
        pagina_comienzo = 12
        self.lanzar_selenium(pagina_comienzo)

        # Escribo respuestas en excel
        self.excel.escribir_declaraciones(self.declaraciones_nuevas)

        # Si queremos que mantenga abierto el navegador descomentar siguiente linea
        # time.sleep(1000)
        self.driver.quit()

if __name__ == "__main__":
    Main().inicio()