import uuid
from datetime import datetime


class Service:
    """
    Business Entity : Service
    ─────────────────────────
    A service is an offering provided by the AUC bookstore ON TOP of selling books.
    Examples : , Print , Bindings , CLaim ID Card etc....

    Key business rules :
      - A service must always have a price >= 0 (free is allowed, negative never).
      - An inactive service CANNOT be ordered by a customer.
      - Duration represents the number of days the service takes (e.g. 2 = 2-day of work for Ex).
      - A "seasonal" service is temporarily available (e.g. CLaim ID only fro new studennt and first Semester ).
    """

    # Les seuls statuts autorisés dans le système
    VALID_STATUSES = {"available", "Unavailable", "seasonal"}

    def __init__(
        self,
        service_name: str,
        description: str,
        price: float,
        duration: int,
        status: str = "active",
    ):
        # ── Unique identifier — never modified after creation ──
        self.service_id: str = str(uuid.uuid4())

        self.service_name: str = service_name
        self.description: str = description

        # Price in USD — must be >= 0 (a free service is valid, a negative price is not)
        self.price: float = price

        # Duration in days — e.g. 2 = service fulfilled within 2 business days
        self.duration: int = duration

        # Default status at creation is "active"
        self.status: str = status

        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()   # refreshed on every modification

    # ── UPDATERS ──────────────────────────────────────────────────────────────
    
    
    
    def update_price(self, new_price: float) -> None:
        # Rule : a negative price makes no sense in our system
        if new_price < 0:
            raise ValueError("A service price cannot be negative.")
        self.price = new_price
        self.updated_at = datetime.now()

    def update_duration(self, new_duration: int) -> None:
        # Rule : duration must be at least 1 day
        if new_duration <= 0:
            raise ValueError("Duration must be at least 1 day.")
        self.duration = new_duration
        self.updated_at = datetime.now()

 
    # ── BUSINESS RULES ────────────────────────────────────────────────────────

    def is_available(self) -> bool:
        """
        Checks whether the service can be ordered by a customer.
        Rule : only "active" and "seasonal" are considered available.
        An "inactive" service must never appear in the customer's cart.
        """
        return self.status in {"active", "seasonal"}

    def apply_discount(self, percent: float) -> float:
        """
        Computes the discounted price WITHOUT modifying the original price.
        Used for one-time promotions (e.g. -20% on express delivery).

        Rule : percent must be between 0 and 100.
        Returns the new price rounded to 2 decimal places.
        """
        if not (0 <= percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")
        return round(self.price * (1 - percent / 100), 2)

    # ── REPRESENTATION ────────────────────────────────────────────────────────

    def __str__(self) -> str:
        return (
            f"[{self.status.upper()}] {self.service_name} "
            f"— ${self.price:.2f} | {self.duration} day(s)"
        )


# ── DEMO ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    svc = Service(
        service_name="Printing",
        description="Printing 2 History Book within 2 business days.",
        price=9.99,
        duration=2,
    )

    print(svc)
    print("Available?", svc.is_available())     # True — status is "available"

    svc.update_price(7.99)
    print("After price update:", svc)

    print("Price with -20%:", svc.apply_discount(20))  # does not change svc.price

    svc.is_available()
    print("Available", svc.is_available())
