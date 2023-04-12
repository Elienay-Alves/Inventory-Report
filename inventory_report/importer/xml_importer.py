import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path) as file:
                content = file.read()
                records = xmltodict.parse(content)["dataset"]["record"]
                return [row for row in records]
        except FileNotFoundError:
            raise ValueError(f"Arquivo não encontrado: {path}")
        except PermissionError:
            raise ValueError(f"Sem permissão para ler arquivo: {path}")
