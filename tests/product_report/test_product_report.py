from inventory_report.inventory.product import Product


def test_relatorio_produto():
    instructions = "Don't know what I want, but I know how to get it"
    mock = Product(
        77,
        "Never Mind The Bollocks",
        "S Pistols",
        "1977-03-07",
        "2333-12-31",
        "407300237-5390682354",
        instructions,
    )

    assert mock.id == 77
    assert mock.nome_do_produto == "Never Mind The Bollocks"
    assert mock.nome_da_empresa == "S Pistols"
    assert mock.data_de_fabricacao == "1977-03-07"
    assert mock.data_de_validade == "2333-12-31"
    assert mock.numero_de_serie == "407300237-5390682354"
    assert mock.instrucoes_de_armazenamento == instructions
