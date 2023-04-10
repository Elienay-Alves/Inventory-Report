from datetime import datetime
from collections import Counter


def oldest_manufacture(products):
    return min([product["data_de_fabricacao"] for product in products])


def closest_expiration(products):
    now = datetime.now()
    expired_dates = [
        datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
        for product in products
        if datetime.strptime(product["data_de_validade"], "%Y-%m-%d") < now
    ]

    return min(expired_dates)


def comp_with_more_products(company):
    companies = [product["nome_da_empresa"] for product in company]
    return Counter(companies).most_common(1)[0][0]


class SimpleReport:
    @staticmethod
    def generate(products):
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture(products)}\n"
            f"Data de validade mais próxima: {closest_expiration(products)}\n"
            f"Empresa com mais produtos: {comp_with_more_products(products)}\n"
        )
