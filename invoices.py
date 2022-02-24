import starkbank
import keys
from names import random_names
from cpf import random_cpf
from random import randint

def create_invoices():
    for i in range(randint(8, 12)):         
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=randint(1, 5000),
                name=random_names(),
                fine=randint(2, 10),
                tax_id=random_cpf()
            )
        ])

        for invoice in invoices:
            print(invoice)