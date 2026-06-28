from datetime import datetime
from enum import Enum
from typing import Dict, List


# =========================
# STATUS ENUM
# =========================
class ItemStatus(Enum):
    ACTIVE = "active"
    REMOVED = "removed"


# =========================
# DOMAIN EXCEPTION
# =========================
class DomainError(Exception):
    """Base domain exception."""
    pass


# =========================
# FAVORIS ENTITY
# =========================
class Favoris:
    """
    Represents a product a user likes (favorite item).
    """

    def _init_(self, user_id: int, product_id: int):
        self._validate(user_id, product_id)

        self.user_id = user_id
        self.product_id = product_id
        self.status = ItemStatus.ACTIVE
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # -------------------------
    # BUSINESS RULES
    # -------------------------

    def remove(self) -> None:
        """
        Soft remove favorite item.
        """
        self.status = ItemStatus.REMOVED
        self.updated_at = datetime.utcnow()

    def is_active(self) -> bool:
        return self.status == ItemStatus.ACTIVE

    # -------------------------
    # VALIDATION
    # -------------------------

    def _validate(self, user_id: int, product_id: int) -> None:
        if user_id <= 0:
            raise DomainError("user_id must be positive")

        if product_id <= 0:
            raise DomainError("product_id must be positive")


# =========================
# PANIER ITEM ENTITY
# =========================
class PanierItem:
    """
    Single item inside cart.
    """

    def _init_(self, product_id: int, quantity: int = 1):
        if product_id <= 0:
            raise DomainError("product_id must be positive")

        if quantity <= 0:
            raise DomainError("quantity must be greater than 0")

        self.product_id = product_id
        self.quantity = quantity


# =========================
# PANIER (CART) ENTITY
# =========================
class Panier:
    """
    Shopping cart entity.
    """

    def _init_(self, user_id: int):
        if user_id <= 0:
            raise DomainError("user_id must be positive")

        self.user_id = user_id
        self.items: List[PanierItem] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    # -------------------------
    # BUSINESS RULES
    # -------------------------

    def add_item(self, product_id: int, quantity: int = 1) -> None:
        """
        Add item or increase quantity if already exists.
        """
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += quantity
                self.updated_at = datetime.utcnow()
                return

        self.items.append(PanierItem(product_id, quantity))
        self.updated_at = datetime.utcnow()

    def remove_item(self, product_id: int) -> None:
        """
        Remove item completely from cart.
        """
        self.items = [i for i in self.items if i.product_id != product_id]
        self.updated_at = datetime.utcnow()

    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    def is_almost_complete(self) -> bool:
        """
        Alert rule: cart is almost complete.
        """
        return self.total_items() >= 5

    def completion_message(self) -> str:
        """
        Notify user progress.
        """
        total = self.total_items()

        if total >= 5:
            return "⚠️ You are almost finished your order!"
        elif total >= 3:
            return "📦 You are close to completing your cart!"
        else:
            return "🛒 Keep shopping!"


# =========================
# APPLICATION SERVICE
# =========================
class ShopService:
    """
    Orchestrates business logic for Favoris and Panier.
    """

    def _init_(self):
        self.favoris_store: Dict[int, Favoris] = {}
        self.panier_store: Dict[int, Panier] = {}

    def add_to_favoris(self, user_id: int, product_id: int) -> Favoris:
        fav = Favoris(user_id, product_id)
        self.favoris_store[product_id] = fav
        return fav

    def add_to_cart(self, user_id: int, product_id: int) -> str:
        if user_id not in self.panier_store:
            self.panier_store[user_id] = Panier(user_id)

        cart = self.panier_store[user_id]
        cart.add_item(product_id)

        return cart.completion_message()