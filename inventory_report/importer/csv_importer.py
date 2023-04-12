import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path) as file:
                rows = csv.DictReader(file)
                return [row for row in rows]
        except FileNotFoundError:
            raise ValueError(f"Arquivo não encontrado: {path}")
        except PermissionError:
            raise ValueError(f"Sem permissão para ler arquivo: {path}")
