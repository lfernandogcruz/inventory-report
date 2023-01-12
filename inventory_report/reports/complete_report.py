from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:

    @staticmethod
    def generate(prod_list):
        simple_report = SimpleReport.generate(prod_list)

        companies_counter = Counter(
            [product["nome_da_empresa"] for product in prod_list]
        ).items()

        result = f"{simple_report}\n"
        result += "Produtos estocados por empresa:\n"
        for company, count in companies_counter:
            result += f"- {company}: {count}\n"

        return result
