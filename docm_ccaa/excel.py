import pandas as pd

from declaracion import Declaracion

# Clase utilizada para leer y escribir los datos al excel

class Excel:
    def __init__(self, ruta_documentos, ruta_municipios):
        self.ruta_documentos = ruta_documentos
        self.data_frame = pd.read_excel(ruta_documentos, keep_default_na=False)
        self.df_municipios = pd.read_excel(ruta_municipios, keep_default_na=False)

    # Funcion que lee filas en el excel
    def leer_declaraciones(self):
        declaraciones = []

        for i in range(len(self.data_frame)):
            fecha = self.data_frame.iloc[(i,0)]
            sumario = self.data_frame.iloc[(i,1)]
            expediente = self.data_frame.iloc[(i,2)]
            resolucion = self.data_frame.iloc[(i,3)]
            proyecto = self.data_frame.iloc[(i,4)]
            tecnologia = self.data_frame.iloc[(i,5)]
            hibridacion = self.data_frame.iloc[(i,6)]
            size_fv = self.data_frame.iloc[(i,7)]
            size_eo = self.data_frame.iloc[(i,8)]
            size_bess = self.data_frame.iloc[(i,9)]
            capacidad = self.data_frame.iloc[(i,10)]
            nombre_set = self.data_frame.iloc[(i,11)]
            tension = self.data_frame.iloc[(i,12)]
            set_tension = self.data_frame.iloc[(i,13)]
            distribuidora = self.data_frame.iloc[(i,14)]
            spv = self.data_frame.iloc[(i,15)]
            sociedad = self.data_frame.iloc[(i,16)]
            municipio_evacuacion = self.data_frame.iloc[(i,17)]
            municipio = self.data_frame.iloc[(i,18)]
            codigo_municipio = self.data_frame.iloc[(i,19)]
            comunidad_autonoma = self.data_frame.iloc[(i,20)]
            provincia = self.data_frame.iloc[(i,21)]
            resultado = self.data_frame.iloc[(i,22)]
            motivacion = self.data_frame.iloc[(i,23)]
            ruta = self.data_frame.iloc[(i,24)]
            poligono_parcela = self.data_frame.iloc[(i,25)]
            coordenadas = self.data_frame.iloc[(i,26)]
            ref_catastral = self.data_frame.iloc[(i,27)]

            declaracion = Declaracion(fecha, sumario, expediente, resolucion, proyecto, tecnologia, hibridacion, size_fv, size_eo, size_bess, capacidad, nombre_set, tension, distribuidora, spv, sociedad, municipio_evacuacion, municipio, codigo_municipio, comunidad_autonoma, provincia, resultado, motivacion, ruta, poligono_parcela, coordenadas, ref_catastral)

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

        self.data_frame.to_excel(self.ruta_documentos, index=False)

    def leer_codigos_municipios(self):
        codigos = {}

        for i in range(3,len(self.df_municipios)):
            nombre = self.df_municipios.iloc[(i,4)]
            codigo = self.df_municipios.iloc[(i,5)]

            codigos[nombre] = codigo

        return codigos