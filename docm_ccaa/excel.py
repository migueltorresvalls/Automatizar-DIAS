import pandas as pd

from declaracion import Declaracion

# Clase utilizada para leer y escribir los datos al excel

class Excel:
    def __init__(self, ruta):
        self.ruta = ruta
        self.data_frame = pd.read_excel(ruta, keep_default_na=False)

    # Funcion que lee filas en el excel
    def leer_declaraciones(self):
        declaraciones = []

        for i in range(len(self.data_frame)):
            fecha = self.data_frame.iloc[(i,0)]
            sumario = self.data_frame.iloc[(i,1)]
            resolucion = self.data_frame.iloc[(i,2)]
            proyecto = self.data_frame.iloc[(i,3)]
            tecnologia = self.data_frame.iloc[(i,4)]
            hibridacion = self.data_frame.iloc[(i,5)]
            size = self.data_frame.iloc[(i,6)]
            capacidad = self.data_frame.iloc[(i,7)]
            nombre_set = self.data_frame.iloc[(i,8)]
            tension = self.data_frame.iloc[(i,9)]
            set_tension = self.data_frame.iloc[(i,10)]
            distribuidora = self.data_frame.iloc[(i,11)]
            spv = self.data_frame.iloc[(i,12)]
            sociedad = self.data_frame.iloc[(i,13)]
            municipio = self.data_frame.iloc[(i,14)]
            poligono_parcela = self.data_frame.iloc[(i,15)]
            coordenadas = self.data_frame.iloc[(i,16)]
            ref_catastral = self.data_frame.iloc[(i,17)]
            comunidad_autonoma = self.data_frame.iloc[(i,18)]
            provincia = self.data_frame.iloc[(i,19)]
            resultado = self.data_frame.iloc[(i,20)]
            motivacion = self.data_frame.iloc[(i,21)]
            ruta = self.data_frame.iloc[(i,22)]

            declaracion = Declaracion(fecha, sumario, resolucion, proyecto, tecnologia, hibridacion, size, capacidad, nombre_set, tension, distribuidora, spv, sociedad, municipio, poligono_parcela, coordenadas, ref_catastral, comunidad_autonoma, provincia, resultado, motivacion, ruta)

            declaraciones.append(declaracion)

        return declaraciones

    # Escribe filas en el excel
    def escribir_declaraciones(self, declaraciones):
        # fecha publicación, tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion

        # Creamos columnas. Solo si el excel se empieza de cero y está vacío previamente
        # data_frame = pd.DataFrame(columns=['Fecha', 'Resolucion', 'Proyecto', 'Tecnologia', 'Hibridacion', 'Tamaño', 'Capacidad acceso', 'SPV', 'Sociedad', 'Ubicacion'])
        offset = len(self.data_frame)
        for i in range(len(declaraciones)): 
            # Añadimos una fila para cada declaración
            self.data_frame.loc[i+offset] = declaraciones[i].to_excel()

        self.data_frame.to_excel(self.ruta, index=False)