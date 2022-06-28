import csv
import os

MAX_RECORDS = 10


class Records:

    filename = "records.csv"
    dir_path = os.path.dirname(
        os.path.realpath(__file__)
    )
    # __file__ = corresponde con el path del archivo actual (record.py)

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
        if not os.path.exists(self.file_path):
            self.reset()

    def insertar_record(self, nombre: str, puntos: int):
        """
        Agrega un registro en el listado de records
        con el nombre del jugador y los puntos conseguidos.
        La lista de records se debe quedar ordenada, es decir,
        se inserta en la posición que le corresponde ordenando
        de mayor a menor.
        """
        self.game_records.append([nombre, puntos])
        self.game_records.sort(key=lambda item: item[1], reverse=True)

    def puntuacion_menor(self):
        """
        Devuelve un entero con el valor de puntos de la última
        posición del listado de records.
        """
        return self.game_records[-1]

    def guardar(self):
        """
        Guarda el archivo de records.
        """
        with open(self.file_path, mode="w") as records_file:
            records_writer = csv.writer(records_file)
            records_writer.writerow(["Jugador", "Puntos"])
            for record in self.game_records[:MAX_RECORDS]:
                records_writer.writerow(record)

    def cargar(self):
        """
        Carga el archivo de records, si existe.
        """
        with open(self.file_path, mode="r") as records_file:
            records_reader = csv.reader(records_file)
            contador_lineas = 0
            self.game_records = []
            for linea in records_reader:
                contador_lineas += 1
                if contador_lineas == 1:
                    continue
                self.game_records.append([linea[0], linea[1]])

    def reset(self):
        """
        Resetea el archivo de records.
        """
        print("Creando archivo de records vacío")
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['---', 0])
        self.guardar()