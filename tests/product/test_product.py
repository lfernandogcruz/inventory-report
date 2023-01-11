from inventory_report.inventory.product import Product


def test_cria_produto():

    storaging = "Local seco e arejado ao abrigo do sol"

    product = Product(
        1,
        "Toddynho",
        "Toddy",
        "07/03/2021",
        "01/05/2024",
        "TDNH-1234",
        "Local seco e arejado ao abrigo do sol",
        )

    assert product.id == 1
    assert product.nome_do_produto == "Toddynho"
    assert product.nome_da_empresa == "Toddy"
    assert product.data_de_fabricacao == "07/03/2021"
    assert product.data_de_validade == "01/05/2024"
    assert product.numero_de_serie == "TDNH-1234"
    assert product.instrucoes_de_armazenamento == storaging
