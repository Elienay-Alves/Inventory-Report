from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Fried Chicken",
        "Two Sons Company",
        "1990-12-31",
        "123456789",
        "Maintain in your stomach",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Fried Chicken"
    assert product.nome_da_empresa == "Two Sons Company"
    assert product.data_de_fabricacao == "1990-12-31"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "Maintain in your stomach"
