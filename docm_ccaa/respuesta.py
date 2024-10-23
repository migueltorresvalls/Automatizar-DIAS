from declaracion import Declaracion

# Parsea la respuesta recibida de la IA, creando un array de objetos del tipo Declaracion

class Respuesta: 
    def __init__(self, fecha, sumario, ruta_pdf, respuesta):
        # fecha publicación, tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion

        self.fecha = fecha
        self.sumario = sumario
        self.ruta_pdf = ruta_pdf
        self.respuesta = respuesta

        # Valores por defecto
        self.resolucion = ""
        self.proyecto = ""
        self.tecnologia = ""
        self.hibridacion = ""
        self.size = 0
        self.capacidad = 0
        self.nombre_set = ""
        self.tension = 0
        self.distribuidora = "N/A"
        self.spv = "N/A"
        self.sociedad = "N/A"   
        self.municipio = "N/A"
        self.poligono_parcela = "N/A"
        self.coordenadas = "N/A"
        self.ref_catastral = "N/A"
        self.comunidad_autonoma = "N/A"
        self.provincia = "N/A"
        self.resultado = "N/A"
        self.motivos = ""

    def parsear(self):
        atributos = self.respuesta.split("\n")
        for i in range(len(atributos)):
            campos = atributos[i].split(":")
            clave = campos[0].lower().strip()
            if len(campos)>1:
                if campos[1].strip() == "" and clave != "motivos":
                    campos[1] = "N/A"

                # La fecha que aparece en el documento es la de publicación, no la de resolución
                if clave == "resolucion": 
                    self.resolucion = campos[1]
                elif clave == "proyecto":
                    self.proyecto = campos[1]
                elif clave == "tecnologia": 
                    self.tecnologia = campos[1].strip()
                elif clave == "hibridacion": 
                    self.hibridacion = campos[1]
                elif clave == "tamaño": 
                    self.size = float(campos[1].replace(",",".").strip())
                elif clave == "capacidad": 
                    self.capacidad = float(campos[1].replace(",",".").strip())
                    if self.capacidad > self.size:
                        self.capacidad = 0
                elif clave == "set":
                    self.nombre_set = campos[1]
                elif clave == "tension": 
                    self.tension = float(campos[1].replace(",",".").strip())
                elif clave == "distribuidora":
                    self.distribuidora = campos[1].strip()
                elif clave == "spv": 
                    self.spv = campos[1]
                elif clave == "municipio":
                    self.municipio = campos[1].lower()
                elif clave == "poligono_parcela": 
                    self.poligono_parcela = campos[1]
                elif clave == "coordenadas": 
                    self.coordenadas = campos[1]
                elif clave == "ref_catastral":
                    self.ref_catastral = campos[1]
                elif clave == "comunidad_autonoma":
                    self.comunidad_autonoma = campos[1].lower()
                elif clave == "provincia":
                    self.provincia = campos[1].lower()
                elif clave == "resultado": 
                    self.resultado = campos[1].lower().strip()
                elif clave == "motivos" and self.resultado == "desfavorable": 
                    self.motivos = campos[1]

        return Declaracion(self.fecha, self.sumario, self.resolucion, self.proyecto, self.tecnologia, self.hibridacion, self.size, self.capacidad, self.nombre_set, self.tension, self.distribuidora, self.spv, self.sociedad, self.municipio, self.poligono_parcela, self.coordenadas, self.ref_catastral, self.comunidad_autonoma, self.provincia, self.resultado, self.motivos, self.ruta_pdf)
