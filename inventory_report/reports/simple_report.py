from collections import Counter


class SimpleReport:

    @staticmethod
    def generate(prod_list):
        prod_date = "data_de_fabricacao"
        oldest_product = None
        for product in prod_list:
            if oldest_product is None or (
                oldest_product > product[prod_date]
            ):
                oldest_product = product[prod_date]

        exp_date = "data_de_validade"
        soon_to_expire = None
        for product in prod_list:
            if soon_to_expire is None or (
                soon_to_expire > product[exp_date]
            ):
                soon_to_expire = product[exp_date]

        company_with_more_products = Counter(
            [product["nome_da_empresa"] for product in prod_list]
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {soon_to_expire}\n"
            f"Empresa com mais produtos: {company_with_more_products}\n"
        )
