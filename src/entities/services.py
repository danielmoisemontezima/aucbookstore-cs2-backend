import uuid
from datetime import datetime
from enum import Enum


class ServiceStatus(Enum):
    """
    Represents the lifecycle states of a bookstore service.

    Rules :
      - ACTIVE   → available for ordering at any time.
      - INACTIVE → pulled from the catalog; customers cannot select it.
      - SEASONAL → temporarily available (e.g. gift wrapping during the holidays).
    """
    AVAILABLE   = "available"
    UNAVAILABLE = "unavailable"
    SEASONAL    = "seasonal"


class Service:
    """
    Business Entity : Service
    ─────────────────────────
    A service is an offering provided by the bookstore ON TOP of selling books.
    Examples : express delivery, gift wrapping, monthly subscription, author signing event.

    Key business rules :
      - A service must always have a price >= 0 (free is allowed, negative never).
      - An INACTIVE service CANNOT be ordered by a customer.
      - Duration represents the number of days the service takes (e.g. 2 = 2-day delivery).
      - A SEASONAL service is temporarily available but still orderable.
    """

    def __init__(
        self,
        service_name: str,
        description: str,
        price: float,
        duration: int,
        status: ServiceStatus = ServiceStatus.AVAILABLE,
    ):
        # Unique identifier — never modified after creation
        self.service_id: str = str(uuid.uuid4())

        self.service_name: str = service_name
        self.description: str = description

        # Price in USD — must be >= 0 (a free service is valid, a negative price is not)
        self.price: float = price

        # Duration in days — e.g. 2 = service fulfilled within 2 business days
        self.duration: int = duration

        # Strongly typed status — only ServiceStatus enum values are accepted
        self.status: ServiceStatus = status

        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()  # refreshed on every modification

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

    # ── STATUS MANAGEMENT ─────────────────────────────────────────────────────
    # Status controls whether a customer can order this service or not.
   

    def available(self) -> None:
        # Makes the service available for ordering
        self.status = ServiceStatus.AVAILABLE
        self.updated_at = datetime.now()

    def unavailable(self) -> None:
        # Removes the service from the catalog — customers can no longer select it
        self.status = ServiceStatus.UNAVAILABLE
        self.updated_at = datetime.now()

    def mark_as_seasonal(self) -> None:
        # Temporarily available (e.g. gift wrapping in December)
        # Still orderable, but flagged as time-limited
        self.status = ServiceStatus.SEASONAL
        self.updated_at = datetime.now()

    # ── OTHER BUSINESS RULES ────────────────────────────────────────────────────────

    def is_available(self) -> bool:
        """
        Checks whether the service can be ordered by a customer.
        Rule : only ACTIVE and SEASONAL are considered available.
        An INACTIVE service must never appear in the customer's cart.
        """
        return self.status in {ServiceStatus.AVAILABLE, ServiceStatus.SEASONAL}

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

   


# ── DEMO ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    svc = Service(
        service_name="Print",
        description="Printing 2 History book within 2 business days.",
        price=9.99,
        duration=2,
    )

    print(svc)
    print("Available?", svc.is_available())      # True — status is AVAILABLE

    svc.update_price(7.99)
    print("After price update:", svc)

    print("Price with -0%:", svc.apply_discount(0))  # does not change svc.price

    svc.unavailable()
    print("Available after deactivation?", svc.is_available())  # False

    # Enum comparison is now safe 
    print("Is Unavailable?", svc.status == ServiceStatus.AVAILABLE)  # True