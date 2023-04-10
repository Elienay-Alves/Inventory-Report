from datetime import datetime
from collections import Counter


def oldest_manufacture(products):
    dates = [product["data_de_fabricacao"] for product in products]
    oldest = min(dates)
    return oldest


def closest_expiration(inventory):
    valid_dates = []
    for product in inventory:
        valid_date = datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
        if valid_date > datetime.now():
            valid_dates.append(product["data_de_validade"])
    closest = min(valid_dates)
    return closest


def comp_with_more_products(company):
    companies = [product["nome_da_empresa"] for product in company]
    most_common = Counter(companies).most_common(1)[0][0]
    return most_common


class SimpleReport:
    @staticmethod
    def generate(products):
        oldest_manufacture_date = oldest_manufacture(products)
        closest_expiration_date = closest_expiration(products)
        most_productive_company = comp_with_more_products(products)
        report = (
            f"Data de fabricação mais antiga: {oldest_manufacture_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {most_productive_company}"
        )
        return report
