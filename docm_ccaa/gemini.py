import google.generativeai as genai 
import os

# Clase que se utiliza para realizar consultas a la IA

class Gemini:
    def __init__(self):
        # Hay que crearse una cuenta en Gemini Google y crearse una clave (https://ai.google.dev/gemini-api/docs/api-key?hl=es-419). A continuación, se añade la clave como variable de entorno bajo el nombre GEMINI_API_KEY.
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def lanzar_consulta(self, pdf):
        consulta = """
        Quiero que extraigas la siguiente información del pdf: tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SET, tension, distribuidora, SPV, municipio, poligono_parcela, coordenadas, ref_catastral, comunidad_autonoma, provincia, resultado, motivacion

        Quiero que tu respuesta tenga la siguiente estructura csv.
        resolucion:
        proyecto:
        tecnologia:
        hibridacion:
        tamaño:
        capacidad:
        SET:
        tension:
        distribuidora: 
        SPV:
        municipio:
        poligono_parcela: 
        coordenadas: 
        ref_catastral:
        comunidad_autonoma: 
        provincia:
        resultado:
        motivos:

        A continuación, te explico el significado de cada campo.

        El campo fecha lo quiero en formato dd/mm/aa

        El campo resolución puede tomar los siguientes valores: Solicitud de Autorización Administrativa Previa (AAP), Autorización Administrativa de Construcción (AAC), Evaluación de Impacto Ambiental (a la cual nos referimos como Declaración de Impacto Ambiental o DIA) o una Corrección (CORR). Quiero que me contestes con DIA, AAP, AAC, CORR. En el caso de que sean varias, sepáralas con una /. Por ejemplo: AAC/APP. Si se trata de una corrección (CORR), no va a poder ser de otro tipo, por lo que únicamente pon CORR. Si no lo encuentras, pon N/A.

        Para el campo hibridación, determina si se mezclan tecnologías diferentes en el proyecto. Por ejemplo, si se quiere añadir una planta fotovoltaica a una instalación eólica, si que hay hibridación. En caso de haber hibridación, contesta con un SI. Si no hay, con un NO.

        El campo tecnología puede tomar los siguientes valores: fotovoltaica (FV), eólica (EO) o baterías (BESS). Solo contestame con uno de esos valores, no quiero ningun otro. Si no encuentras o si no fuera ninguno de esos 3, pon N/A.

        El campo tamaño es la potencia instalada en el proyecto en MWp. Si no encuentras el tamaño, pon un 0. 

        El campo capacidad es la potencia en el punto de conexión. Si no lo encuentras, pon un 0.

        Para el campo SET, quiero que me respondas con el nombre de la subestación (también llamada centro de transformación, subestación transformadora, ST o SET) final de la red de transporte o red de distribucion a la que se conecta el proyecto. No quiero que me des la tensión a la que se conecta (por ejemplo, si la subestacion fuera Mingorrubio 20/132 kV, quiero que me respondas solo con Mingorrubio). Tampoco quiero que me digas si se ha ampliado o no (por ejemplo, si el nombre fuera Ampliacion subestación Torviscal, solo me interesa Torviscal). Si no encuentras el nombre, pon N/A.
        
        Para el campo tensión solo quiero que me respondas con un número: la tensión final a la que se conecta a la red de distribución o de transporte en kV. Si no lo encuentras, que sea un 0. Si por ejemplo, la subestación fuera Mingorrubio 20/132 kV quiero que me respondas con 132kV, es decir, la tensión a la que la subestación eleva la tensión. Si hubiera varias subestaciones o centros de transformacion, quiero que me respondas con el último. Si no encuentras nada, pon N/A.

        Para el campo distribuidora, quiero que me digas si la subestación a la que se conecta el proyecto peretenece a la red de Iberdorla (i-DE), Unión Fenosa (UFD), Endesa (EDE) o a la Red Eléctrica Española (REE). Contéstame únicamete con i-DE, UDF, EDE o REE. Si no lo encuentras, respondeme con N/A.
        
        El campo spv es la Special-purpose entity que firma el proyecto. Si no lo encuentras, pon N/A.

        El campo municipio se refiere al término municipal. Si no lo encuentras, pon N/A.

        Para el campo poligono_parcela, quiero saber el número del polígono y la parcela del proyecto. Respondeme con una lista de tuplas, donde cada tupla tiene dos elementos (el primero el polígono y el segundo la parcela). Añade tantas tuplas a la lista como poligonos y parcelas encuentres. Si un proyecto tiene poligono pero no parcela, pon un "N/A" en la parcela. Si no lo encuentras ningun poligono o parcela, pon N/A.

        Para el campo coordenadas, quiero que me digas las coordenadas UTM del proyecto. Respondeme en una lista de tuplas, donde cada tupla tiene dos elementos (el primero la coordenada X y el segundo la coordenada Y). Añade tantas tuplas a la lista como coordenadas encuentres. Si no lo encuentras, pon N/A.

        Para el campo ref_catastral, quiero saber la referencia catastral de las parcelas. Quiero que me respondas con una lista, donde cada elemento es la referencia catastral de una parcela. Si no lo encuentras, pon "N/A.

        Para el campo comunidad autónoma, quiero que me digas la comunidad autónoma en la que se encuentra el proyecto. Si no lo encuentras, pon N/A.

        Para el campo provincia provincia, quiero que me digas la provincia donde se encuentra el proyecto. Si no lo encuentras, pon N/A. 

        Para el campo resultado hay 4 posibles valores. Favorable (resolución favorable), Desfavorable (resolución desfavorable), Correccion (si la resolucion es una corrección) y Anuncio (si la resolucion es un anuncio). Si no lo encuentras, pon N/A.

        Para el campo motivos y solo si el resultado ha sido desfavorable, quiero saber cuales han sido los motivos. Si el resultado ha sido favorable, dejalo en blanco, no quieres que pongas nada. 
        
        Puedes encontrar la información sobre el pdf a continuación: 

        """
        respuesta = self.model.generate_content(consulta + pdf)
        return respuesta.text