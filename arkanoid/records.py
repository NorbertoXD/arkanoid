import csv
import os 

MAX_RECORDS = 10


class Records:

    filename = "records.csv"
    dir_path = os.path.dirname(
        os.path.realpath(__file__)
    )
    #__file__ = /home......records.py

    def __init__(self):
        """
        En el constructor quiero crear los atributos para la ruta y
        comprobar si el archivo existe.
        """
        self.game_records = []
        self.data_path = os.path.join(
            os.path.dirname(self.dir_path), "data")
        self.file_path = os.path.join(self.data_path, self.filename)
        self.check_records_file()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
            print("El directorio data no existe: creado!")
        

    def insertar_record(self, nombre: str, puntos: int):
        """
        Agrega un registro en el listado de records
        con el nombre del jugador y los puntos conseguidos.
        La lista de records se debe quedar ordenada, es decir,
        se inserta en la posicion que le corresponde ordenando
        de mayor a menor.
        """
        pass

        def puntuacion_menor(self):
            """
            Devuelve un entero con el valor de puntos de la ultima
            posicion del listado de records.
            """
            pass

        def guardar(self):
            """
            Guardar el archivo de records.
            """
            with open(self.file_path, mode="w") as records_file:
                records_writer = csv.writer(records_file, delimiter= ",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                


        def cargar(self):
            """
            Cargar el archivo de records, si existe.
            """
            pass

        def reset(self):
            """

            """
            print("Creando )



