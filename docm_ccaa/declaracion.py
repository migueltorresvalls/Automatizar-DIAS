# Clase que agrupa todos los valores de una declaracion

class Declaracion:
    def __init__(self, fecha, sumario, expediente, resolucion, proyecto, tecnologia, hibridacion, size_fv, size_eo, size_bess, capacidad, nombre_set, tension, distribuidora, spv, sociedad, municipio_evacuacion, municipio, codigo_municipio, comunidad_autonoma, provincia, resultado, motivacion, ruta, poligono_parcela, coordenadas, ref_catastral):
        self.fecha = fecha
        self.sumario = sumario 
        self.expediente = expediente
        self.resolucion = resolucion
        self.proyecto = proyecto
        self.tecnologia = tecnologia
        self.hibridacion = hibridacion
        self.size_fv = size_fv
        self.size_eo = size_eo
        self.size_bess = size_bess
        self.capacidad = capacidad
        self.nombre_set = nombre_set
        self.tension = tension
        try: self.set_tension = nombre_set + str(int(tension))
        except: self.set_tension = nombre_set
        self.distribuidora = distribuidora
        self.spv = spv
        self.sociedad = sociedad
        self.municipio_evacuacion = municipio_evacuacion
        self.municipio = municipio
        self.codigo_municipio = codigo_municipio
        self.comunidad_autonoma = comunidad_autonoma
        self.provincia = provincia
        self.resultado = resultado
        self.motivacion = motivacion
        self.ruta = ruta
        self.poligono_parcela = poligono_parcela
        self.coordenadas = coordenadas
        self.ref_catastral = ref_catastral
    
    # Crea una lista con los valores de la fila que luego se añadiran al excel
    def to_excel(self):
        fila = [self.fecha, self.sumario, self.expediente, self.resolucion, self.proyecto, self.tecnologia, self.hibridacion, self.size_fv, self.size_eo, self.size_bess, self.capacidad, self.nombre_set, self.tension, self.set_tension, self.distribuidora, self.spv, self.sociedad, self.municipio_evacuacion, self.municipio, self.codigo_municipio, self.comunidad_autonoma, self.provincia, self.resultado, self.motivacion, self.ruta, self.poligono_parcela, self.coordenadas, self.ref_catastral]

        return fila

    # Sobreescribir método == de python. No tocar
    def __eq__(self, resp): 
        if self.ruta == resp.ruta: 
            return True
        return False

    # Sobreescribe el metodo print de python. 
    def __str__(self):
        return (
            f"fecha={self.fecha}\n"
            f"sumario={self.sumario}\n"
            f"expediente={self.expediente}\n"
            f"resolucion={self.resolucion}\n"
            f"proyecto={self.proyecto}\n"
            f"tecnologia={self.tecnologia}\n"
            f"hibridacion={self.hibridacion}\n"
            f"tamaño_fv={self.size_fv}\n"
            f"tamaño_eo={self.size_eo}\n"
            f"tamaño_bess={self.size_bess}\n"
            f"capacidad={self.capacidad}\n"
            f"SET={self.nombre_set}\n"
            f"tension={self.tension}\n"
            f"SET+tension={self.set_tension}\n"
            f"distribuidora={self.distribuidora}\n"
            f"spv={self.spv}\n"
            f"sociedad={self.sociedad}\n"
            f"municipio_evacuacion={self.municipio_evacuacion}\n"
            f"municipio={self.municipio}\n"
            f"codigo_municipio={self.codigo_municipio}\n"
            f"comunidad_autonoma={self.comunidad_autonoma}\n"
            f"provincia={self.provincia}\n"
            f"resultado={self.resultado}\n"
            f"motivos={self.motivacion}\n"
            f"ruta={self.ruta}\n"
            f"poligono_parcela={self.poligono_parcela}\n"
            f"coordenadas={self.coordenadas}\n"
            f"ref_catastral={self.ref_catastral}"
        )

