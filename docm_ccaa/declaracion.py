# Clase que agrupa todos los valores de una declaracion

class Declaracion:
    def __init__(self, fecha, sumario, resolucion, proyecto, tecnologia, hibridacion, size, capacidad, nombre_set, tension, distribuidora, spv, sociedad, municipio, poligono_parcela, coordenadas, ref_catastral, comunidad_autonoma, provincia, resultado, motivacion, ruta):
        self.fecha = fecha
        self.sumario = sumario 
        self.resolucion = resolucion
        self.proyecto = proyecto
        self.tecnologia = tecnologia
        self.hibridacion = hibridacion
        self.size = size
        self.capacidad = capacidad
        self.nombre_set = nombre_set
        self.tension = tension
        try: self.set_tension = nombre_set + str(int(tension))
        except: self.set_tension = nombre_set
        self.distribuidora = distribuidora
        self.spv = spv
        self.sociedad = sociedad
        self.municipio = municipio
        self.poligono_parcela = poligono_parcela
        self.coordenadas = coordenadas
        self.ref_catastral = ref_catastral
        self.comunidad_autonoma = comunidad_autonoma
        self.provincia = provincia
        self.resultado = resultado
        self.motivacion = motivacion
        self.ruta = ruta
    
    # Crea una lista con los valores de la fila que luego se añadiran al excel
    def to_excel(self):
        fila = [self.fecha, self.sumario, self.resolucion, self.proyecto, self.tecnologia, self.hibridacion, self.size, self.capacidad, self.nombre_set, self.tension, self.set_tension, self.distribuidora, self.spv, self.sociedad, self.municipio, self.poligono_parcela, self.coordenadas, self.ref_catastral, self.comunidad_autonoma, self.provincia, self.resultado, self.motivacion, self.ruta]

        return fila

    # Sobreescribir método == de python. No tocar
    def __eq__(self, resp): 
        if self.ruta == resp.ruta: 
            return True
        return False

    # Sobreescribe el metodo print de python. 
    def __str__(self):
        return f"fecha={self.fecha}, sumario={self.sumario}, resolucion={self.resolucion}, proyecto={self.proyecto}, tecnologia={self.tecnologia}, hibridacion={self.hibridacion}, tamaño={self.size}, capacidad={self.capacidad}, SET={self.nombre_set}, tension={self.tension}, SET+tension={self.set_tension}, distribuidora={self.distribuidora}, spv={self.spv}, sociedad={self.sociedad}, municipio={self.municipio}, poligono_parcela={self.poligono_parcela}, coordenadas={self.coordenadas}, ref_catastral={self.ref_catastral}, comunidad_autonoma={self.comunidad_autonoma}, provincia={self.provincia}, resultado={self.resultado}, motivos={self.motivacion}, ruta={self.ruta}"

