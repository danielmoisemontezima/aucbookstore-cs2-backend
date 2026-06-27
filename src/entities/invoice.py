from dataclasses import dataclass, field
from datetime import date
from typing import List

# =====================================================
# BUSINESS ENTITY : InvoiceItem
# Représente un article présent sur une facture.
# =====================================================

@dataclass
class InvoiceItem:
    description: str
    quantity: int
    unit_price: float

    def total(self):
        return self.quantity * self.unit_price


# =====================================================
# BUSINESS ENTITY : Invoice
# Représente une facture.
# Cette classe est indépendante de la base de données,
# de l'interface utilisateur et des frameworks.
# =====================================================

@dataclass
class Invoice:
    id: int
    invoice_number: str
    customer_id: int
    issue_date: date
    payment_method: str
    status: str = "DRAFT"
    items: List[InvoiceItem] = field(default_factory=list)

    # =================================================
    # BUSINESS RULE 1
    # Une facture doit contenir au moins un article.
    # =================================================
    def validate(self):
        if len(self.items) == 0:
            raise Exception("The invoice must contain at least one item.")

    # =================================================
    # BUSINESS RULE 2
    # Une facture payée ne peut plus être modifiée.
    # =================================================
    def add_item(self, item: InvoiceItem):
        if self.status == "PAID":
            raise Exception("Cannot modify a paid invoice.")
        self.items.append(item)

    # =================================================
    # BUSINESS RULE 3
    # Calcul du montant total de la facture.
    # =================================================
    def total_amount(self):
        return sum(item.total() for item in self.items)

    # =================================================
    # BUSINESS RULE 4
    # Le montant payé doit être égal au montant total.
    # Si le paiement est valide, la facture devient PAID.
    # =================================================
    def pay(self, amount):
        if amount != self.total_amount():
            raise Exception("Incorrect payment amount.")
        self.status = "PAID"

    # =================================================
    # Affichage de la facture
    # =================================================
    def display_invoice(self):
        print("\n========== INVOICE ==========")
        print(f"Invoice ID       : {self.id}")
        print(f"Invoice Number   : {self.invoice_number}")
        print(f"Customer ID      : {self.customer_id}")
        print(f"Issue Date       : {self.issue_date}")
        print(f"Payment Method   : {self.payment_method}")
        print(f"Status           : {self.status}")

        print("\nItems")
        print("-----------------------------------")

        for item in self.items:
            print(f"Description : {item.description}")
            print(f"Quantity    : {item.quantity}")
            print(f"Unit Price  : {item.unit_price}")
            print(f"Total       : {item.total()}")
            print("-----------------------------------")

        print(f"Grand Total : {self.total_amount()}")
        print("===================================")



        #=================================================
        #exemple d'utilisation
        #=================================================
        from datetime import date

# Création des articles
book = InvoiceItem(
    description="Python Programming Book",
    quantity=2,
    unit_price=25
)

notebook = InvoiceItem(
    description="Notebook",
    quantity=3,
    unit_price=5
)

# Création de la facture
invoice = Invoice(
    id=1,
    invoice_number="INV-001",
    customer_id=1001,
    issue_date=date.today(),
    payment_method="Cash"
)

# Ajout des articles
invoice.add_item(book)
invoice.add_item(notebook)

# Vérification des règles métier
invoice.validate()

# Paiement
invoice.pay(amount=invoice.total_amount())

# Affichage
invoice.display_invoice()
