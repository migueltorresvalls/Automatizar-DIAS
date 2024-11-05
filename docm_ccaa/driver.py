from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import time

import numpy as np

from pdf import Pdf

class Driver: 
    def __init__(self, options=Options()):
        self.driver = webdriver.Chrome(options=options)

    # Lee los pdfs web, realiza la pregunta a la IA, recibe la respuesta parseada y decide si se trata de un documento no o uno ya analizado previamente
    def buscar_castilla_mancha(self, pagina_actual, fila_comienzo, fila_fin):
        self.driver.get("https://docm.jccm.es/docm/busquedaAvanzada.do")

        text_box = self.driver.find_element(by=By.CLASS_NAME, value="cuadroTextoSumarioBusqueda")
        text_box.send_keys("declaración de impacto ambiental" + Keys.ENTER)

        self.cambiar_pagina(pagina_actual)

        self.driver.implicitly_wait(0.5)
        filas_par = self.driver.find_elements(by=By.CLASS_NAME, value="filaPar")
        filas_impar = self.driver.find_elements(by=By.CLASS_NAME, value="filaImpar")
        
        # Hay 50 documentos (25 filas par, 25 filas impar) por página
        filas = np.concatenate((filas_par[fila_comienzo:fila_fin], filas_impar[fila_comienzo:fila_fin]))

        pdfs = []
        for i in filas: 
            pdf = i.find_element(by=By.CLASS_NAME, value="enlacePDFIndividual")

            # Accedo a fecha publicación
            columnas = i.find_elements(by=By.XPATH, value="td[a/@title='Ver los datos detallados del documento']")
            fecha = columnas[3].find_element(By.XPATH, ".//a").text
            sumario = columnas[2].find_element(By.XPATH, ".//a").text

            # Abro pdf
            # pdf.find_element(by=By.CLASS_NAME, value="new-window").click()
            ruta_pdf = pdf.find_element(by=By.CLASS_NAME, value="new-window").get_attribute("href")
            pdf = Pdf(ruta_pdf, fecha, sumario)
            
            pdfs.append(pdf)

        return pdfs        

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

    def close(self):
        self.driver.close()
