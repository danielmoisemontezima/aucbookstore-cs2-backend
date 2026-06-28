from enum import Enum


class SupplyStatus(Enum):
    AVAILABLE = "Available"
    CRITICAL = "Critical"
    OUT_OF_STOCK = "Out of stock"


class Supply:
    def __init__(self, id: int, name: str, description: str,
                 category: str, stock_quantity: int,
                 unit_price: float, supplier: str,
                 alert_threshold: int = 5):

        # All validation rules grouped in a single method
        self._validate(name, unit_price, stock_quantity, alert_threshold)

        self.id = id
        self.name: str = name
        self.description = description
        self.category = category
        self.stock_quantity = stock_quantity
        self.unit_price = unit_price
        self.supplier = supplier
        self.alert_threshold = alert_threshold
        # No self.status = ... here, because 'status' is a @property
        # computed automatically below, based on stock_quantity and alert_threshold.

    def _validate(self, name: str, unit_price: float,
                  stock_quantity: int, alert_threshold: int) -> None:
        """All validation rules for a Supply."""
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
    def status(self) -> SupplyStatus:
        """Status computed automatically based on stock quantity."""
        if self.stock_quantity == 0:
            return SupplyStatus.OUT_OF_STOCK
        elif self.stock_quantity <= self.alert_threshold:
            return SupplyStatus.CRITICAL
        else:
            return SupplyStatus.AVAILABLE

    def __str__(self):
        return (
            f"Supply(id={self.id}, name='{self.name}', "
            f"stock={self.stock_quantity}, "
            f"price={self.unit_price}, "
            f"status={self.status.value})"
        )


# Creating a Supply object
s = Supply(
    id=12,
    name="Notebook",
    description="For taking notes",
    category="Stationery",
    stock_quantity=20,
    unit_price=1.50,
    supplier="ABC Stationery",
    alert_threshold=5
)
print(s)
