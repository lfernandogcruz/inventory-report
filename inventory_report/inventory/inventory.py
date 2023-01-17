import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            info = [row for row in reader]

            if report_type == "simples":
                generated_report = SimpleReport.generate(info)
            elif report_type == "completo":
                generated_report = CompleteReport.generate(info)
            else:
                raise ValueError("Tipo de relatório inválido!")
            return generated_report
