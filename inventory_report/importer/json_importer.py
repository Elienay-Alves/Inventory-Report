import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path) as file:
                content = file.read()
                return json.loads(content)
        except FileNotFoundError:
            raise ValueError(f"Arquivo não encontrado: {path}")
        except PermissionError:
            raise ValueError(f"Sem permissão para ler arquivo: {path}")
