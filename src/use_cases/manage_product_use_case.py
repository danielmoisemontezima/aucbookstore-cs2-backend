from use_cases.assign_role_use_case import AccessDeniedError


class ManageProductUseCase:
    """
    Reserved for the SuperAdmin only. Adding/editing/removing a product
    from the catalog is a business-ownership decision, not something
    a temporary volunteer should be able to do.
    """

    def init(self, product_repository):
        self.product_repository = product_repository

    def add_product(self, current_user, name: str, price: float):
        if not current_user.can_manage_products():
            raise AccessDeniedError("Only the SuperAdmin can manage products.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.product_repository.create(name=name, price=price)

    def remove_product(self, current_user, product_id: int):
        if not current_user.can_manage_products():
            raise AccessDeniedError("Only the SuperAdmin can manage products.")

        self.product_repository.delete(product_id)