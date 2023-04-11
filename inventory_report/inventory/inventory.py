import csv
import json
import os
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Arquivo {path} não encontrado.")

    with open(path) as file:
        if path.endswith(".csv"):
            data = csv.DictReader(file)
            return [row for row in data]
        elif path.endswith(".json"):
            data = file.read()
            return json.loads(data)
        elif path.endswith(".xml"):
            data = file.read()
            return [row for row in xmltodict.parse(data)["dataset"]["record"]]
        else:
            raise ValueError(f"Tipo de inválido: {path}")


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str) -> str:
        data = read_file(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
        else:
            raise ValueError(f"Tipo de relatório inválido: {report_type}")
