from abc import ABC, abstractmethod


class IUserRepository(ABC):
    """
    Abstract contract. Defined on the inner layers' side, implemented
    by an outer layer (Dependency Inversion Principle).
    """

    @abstractmethod
    def find_by_id(self, user_id: int):
        pass

    @abstractmethod
    def save(self, user):
        pass


class IProductRepository(ABC):
    @abstractmethod
    def create(self, name: str, price: float):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass


class IStockRepository(ABC):
    @abstractmethod
    def find_by_product(self, product_id: int):
        pass

    @abstractmethod
    def save(self, stock):
        pass