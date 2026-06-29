"""
#############################################################################
ENTITY LAYER - ORDER
#############################################################################
# Code by VAVAL GAEL & St Prix Casimy

BUSINESS ENTITY

Order is the entity that represents a customer's order in the Bookstore system.

Its responsibilities:
    - Store information about a customer's order.
    - Track the order lifecycle (status).
    - Enforce the business rules that define how an order can evolve.

IMPORTANT:
    This entity must NOT know anything about:
        ✘ Database
        ✘ API
        ✘ Framework (Flask, Django, FastAPI)
        ✘ HTTP / JSON
        ✘ Repository

It only contains:
        ✔️ Business data
        ✔️ Business rules

#############################################################################

BUSINESS RULES

Rules governing an Order:

1. An Order always starts as PENDING.
2. A PENDING Order can become CONFIRMED.
3. A CONFIRMED Order can become SHIPPED.
4. A SHIPPED Order can become COMPLETED.
5. A COMPLETED Order cannot be modified or cancelled.
6. A CANCELLED Order cannot be reactivated.
7. The total amount cannot be negative.

#############################################################################
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import uuid


# =========================================================
# Function to get the current UTC time
# =========================================================
def now():
    return datetime.now(timezone.utc)


# =========================================================
# ENUM: Order Status
# Represents every possible state of an order
# =========================================================
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


# =========================================================
# BUSINESS ENTITY: ORDER
# =========================================================
@dataclass
class Order:

    # Unique identifier for each order
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    # Customer ID who placed the order
    customer_id: str = ""

    # Total amount of the order
    total_amount: float = 0.0

    # Current order status
    status: OrderStatus = OrderStatus.PENDING

    # Date when the order was created
    created_at: datetime = field(default_factory=now)

    # Date of the last update
    updated_at: datetime = field(default_factory=now)

    # =====================================================
    # VALIDATION ON INITIALIZATION
    # =====================================================
    def __post_init__(self):

        # Business Rule:
        # The total amount cannot be negative
        if self.total_amount < 0:
            raise ValueError(
                "The total amount cannot be negative."
            )

    # =====================================================
    # BUSINESS METHOD: CONFIRM ORDER
    # =====================================================
    def confirm(self):

        """
        Rule:
            Only a PENDING Order
            can become CONFIRMED.
        """

        if self.status != OrderStatus.PENDING:
            raise ValueError(
                "Only a pending order can be confirmed."
            )

        self.status = OrderStatus.CONFIRMED
        self.updated_at = now()

    # =====================================================
    # BUSINESS METHOD: SHIP ORDER
    # =====================================================
    def ship(self):

        """
        Rule:
            Only a CONFIRMED Order
            can be shipped.
        """

        if self.status != OrderStatus.CONFIRMED:
            raise ValueError(
                "The order must be CONFIRMED before it can be shipped."
            )

        self.status = OrderStatus.SHIPPED
        self.updated_at = now()

    # =====================================================
    # BUSINESS METHOD: COMPLETE ORDER
    # =====================================================
    def complete(self):

        """
        Rule:
            Only a SHIPPED Order
            can become COMPLETED.
        """

        if self.status != OrderStatus.SHIPPED:
            raise ValueError(
                "The order must be SHIPPED before it can be completed."
            )

        self.status = OrderStatus.COMPLETED
        self.updated_at = now()

    # =====================================================
    # BUSINESS METHOD: CANCEL ORDER
    # =====================================================
    def cancel(self):

        """
        Rules:
            - A COMPLETED Order cannot be cancelled.
            - An already CANCELLED Order cannot be cancelled again.
        """

        if self.status == OrderStatus.COMPLETED:
            raise ValueError(
                "A completed order cannot be cancelled."
            )

        if self.status == OrderStatus.CANCELLED:
            raise ValueError(
                "The order has already been cancelled."
            )

        self.status = OrderStatus.CANCELLED
        self.updated_at = now()

    # =====================================================
    # QUERY METHODS (only check the current state)
    # =====================================================
    def is_pending(self) -> bool:
        return self.status == OrderStatus.PENDING

    def is_confirmed(self) -> bool:
        return self.status == OrderStatus.CONFIRMED

    def is_shipped(self) -> bool:
        return self.status == OrderStatus.SHIPPED

    def is_completed(self) -> bool:
        return self.status == OrderStatus.COMPLETED

    def is_cancelled(self) -> bool:
        return self.status == OrderStatus.CANCELLED