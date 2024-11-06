from declaracion import Declaracion
from excel import Excel

# Parsea la respuesta recibida de la IA, creando un array de objetos del tipo Declaracion

from fuzzywuzzy import fuzz

class Respuesta: 
    def __init__(self, fecha, sumario, ruta_pdf, respuesta):
        # fecha publicación, tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion

        self.fecha = fecha
        self.sumario = sumario
        self.ruta_pdf = ruta_pdf
        self.respuesta = respuesta

        # Valores por defecto
        self.expediente = "N/A"
        self.resolucion = "N/A"
        self.proyecto = "N/A"
        self.tecnologia = "N/A"
        self.hibridacion = "N/A"
        self.size_fv = 0
        self.size_eo = 0
        self.size_bess = 0
        self.capacidad = 0
        self.nombre_set = "N/A"
        self.tension = 0
        self.distribuidora = "N/A"
        self.spv = "N/A"
        self.sociedad = "N/A"   
        self.municipio_evacuacion = "N/A"
        self.municipio = "N/A"
        self.comunidad_autonoma = "N/A"
        self.provincia = "N/A"
        self.resultado = "N/A"
        self.motivos = ""
        self.poligono_parcela = "N/A"
        self.coordenadas = "N/A"
        self.ref_catastral = "N/A"

    def parsear(self):
        atributos = self.respuesta.split("\n")
        for i in range(len(atributos)):
            campos = atributos[i].split(":")
            clave = campos[0].lower().strip()
            if len(campos) > 1:
                if campos[1].strip() != "N/A" and campos[1].strip() != "":
                    # La fecha que aparece en el documento es la de publicación, no la de resolución
                    if clave == "expediente": 
                        self.expediente = campos[1].strip()
                    elif clave == "resolucion": 
                        self.resolucion = campos[1]
                    elif clave == "proyecto":
                        self.proyecto = campos[1]
                    elif clave == "tecnologia": 
                        self.tecnologia = campos[1].strip()
                    elif clave == "hibridacion": 
                        self.hibridacion = campos[1]
                    elif clave == "tamaño_fv": 
                        self.size_fv = float(campos[1].replace(",",".").strip())
                    elif clave == "tamaño_eo": 
                        self.size_eo = float(campos[1].replace(",",".").strip())
                    elif clave == "tamaño_bess": 
                        self.size_bess = float(campos[1].replace(",",".").strip())
                    elif clave == "capacidad": 
                        self.capacidad = float(campos[1].replace(",",".").strip())
                        if (self.capacidad > self.size_fv) and (self.capacidad > self.size_eo) and (self.capacidad > self.size_bess):
                            self.capacidad = 0
                    elif clave == "set":
                        self.nombre_set = campos[1]
                    elif clave == "tension": 
                        self.tension = float(campos[1].replace(",", ".").strip())
                    elif clave == "distribuidora":
                        self.distribuidora = campos[1].strip()
                    elif clave == "spv": 
                        self.spv = campos[1]
                    elif clave == "municipio_evacuacion":
                        self.municipio_evacuacion = self.formatear_lista(campos[1])
                    elif clave == "municipio_planta":
                        self.municipio = self.formatear_lista(campos[1])
                    elif clave == "comunidad_autonoma":
                        self.comunidad_autonoma = campos[1]
                    elif clave == "provincia":
                        self.provincia = campos[1]
                    elif clave == "resultado": 
                        self.resultado = campos[1].lower().strip()
                    elif clave == "motivos" and self.resultado == "desfavorable": 
                        self.motivos = campos[1]
                    elif clave == "poligono_parcela": 
                        self.poligono_parcela = campos[1]
                    elif clave == "coordenadas": 
                        self.coordenadas = campos[1]
                    elif clave == "ref_catastral":
                        self.ref_catastral = self.formatear_lista(campos[1])
        
        return Declaracion(self.fecha, self.sumario, self.expediente, self.resolucion, self.proyecto, self.tecnologia, self.hibridacion, self.size_fv, self.size_eo, self.size_bess, self.capacidad, self.nombre_set, self.tension, self.distribuidora, self.spv, self.sociedad, self.municipio_evacuacion, self.municipio, self.obtener_codigo_municipio(), self.comunidad_autonoma, self.provincia, self.resultado, self.motivos, self.ruta_pdf, self.poligono_parcela, self.coordenadas, self.ref_catastral)
    
    def formatear_lista(self, lista_no_formateada):
        lista_string = "".join(lista_no_formateada).replace("[", "").replace("]", "").replace("\"", "")
        return [i.strip() for i in lista_string.split(',')]
    
    def obtener_codigo_municipio(self): 
        excel = Excel("docm_ccaa/documentos.xlsx", "docm_ccaa/Responsables municipios.xlsx")

        codigos_municipios = excel.leer_codigos_municipios()
        
        ratio_maximo = 0
        output = []
        for m in self.municipio_evacuacion: 
            for i in codigos_municipios: 
                ratio = fuzz.ratio(i, m)
                if  ratio > ratio_maximo:
                    codigo_municipio = codigos_municipios[i]
                    ratio_maximo = ratio

                    # print(f"Hay ratio de {ratio_maximo} entre {i} y {m} resultando en un codigo {codigo_municipio}")
            if codigo_municipio not in output: 
                output.append(codigo_municipio)
                ratio_maximo = 0

        return output

