from enum import Enum


class FurnitureStatus(Enum):
    AVAILABLE = "available"
    CRITICAL = "Critical"
    OUT_OF_STOCK = "in stock"


class Furniture:
    def __init__(self, id: int, name: str, description: str,
                 category: str, stock_quantity: int,
                 unit_price: float, supplier: str,
                 alert_threshold: int = 5):
``
        # all validation 
        self._validate(name, unit_price, stock_quantity, alert_threshold)

        self.id = id
        self.name: str = name
        self.description = description
        self.category = category
        self.stock_quantity = stock_quantity
        self.unit_price = unit_price
        self.supplier = supplier
        self.alert_threshold = alert_threshold
       

    def _validate(self, name: str, unit_price: float,
                  stock_quantity: int, alert_threshold: int) -> None:
        """all rules for this class"""
        if not name.strip():
            raise ValueError("Name is required.")
        if unit_price <= 0:
            raise ValueError("Unit price must be positive.")
        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        if alert_threshold < 0:
            raise ValueError("Alert threshold cannot be negative.")

    def add_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity to add must be greater than 0.")
        self.stock_quantity += quantity

    def remove_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity to remove must be greater than 0.")
        if quantity > self.stock_quantity:
            raise ValueError("Insufficient stock.")
        self.stock_quantity -= quantity

    def is_stock_critical(self) -> bool:
        return self.stock_quantity <= self.alert_threshold

    @property
    def status(self) -> FurnitureStatus:
        """Statut kalkile otomatikman selon kantite stock la."""
        if self.stock_quantity == 0:
            return FurnitureStatus.OUT_OF_STOCK
        elif self.stock_quantity <= self.alert_threshold:
            return FurnitureStatus.CRITICAL
        else:
            return FurnitureStatus.AVAILABLE

    def __str__(self):
        return (
            f"Furniture(id={self.id}, name='{self.name}', "
            f"stock={self.stock_quantity}, "
            f"price={self.unit_price}, "
            f"status={self.status.value})"
        )


# DEMO
f = Furniture(
    id=12,
    name="Kaye",
    description="Pour prendre des notes",
    category="Papeterie",
    stock_quantity=20,
    unit_price=1.50,
    supplier="Papeterie ABC",
    alert_threshold=5
)
print(f)