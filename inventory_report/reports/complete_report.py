from inventory_report.reports.simple_report import (
    SimpleReport,
    oldest_manufacture,
    closest_expiration,
    comp_with_more_products
)
from collections import Counter


def count_products_by_company(products):
    company_counts = Counter([product["nome_da_empresa"]
                              for product in products])
    return company_counts


def format_products_by_company(company_counts):
    result = ""
    for company, count in company_counts.items():
        result += f"- {company}: {count}\n"
    return result


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        oldest_manufacture_date = oldest_manufacture(products)
        closest_expiration_date = closest_expiration(products)
        most_productive_company = comp_with_more_products(products)
        products_by_company = format_products_by_company(
            count_products_by_company(products)
        )
        return (
            f"Data de fabricação mais antiga: {oldest_manufacture_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {most_productive_company}\n"
            f"Produtos estocados por empresa:\n{products_by_company}"
        )
