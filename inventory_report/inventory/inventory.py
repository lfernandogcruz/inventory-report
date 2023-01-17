import os
import csv
import json

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path, "r") as file:
            extension = os.path.splitext(path)[1]

            if extension == ".csv":
                reader = csv.DictReader(file)
                info = [row for row in reader]

            if extension == ".json":
                reader = file.read()
                info = json.loads(reader)

        if report_type == "simples":
            generated_report = SimpleReport.generate(info)
        elif report_type == "completo":
            generated_report = CompleteReport.generate(info)
        else:
            raise ValueError("Tipo de relatório inválido.")
        return generated_report

# research on how to extract the file extension from a path made at:
# https://pt.stackoverflow.com/questions/382049/verificar-extens%C3%B5es-de-arquivos-em-python
# and at:
# https://horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
