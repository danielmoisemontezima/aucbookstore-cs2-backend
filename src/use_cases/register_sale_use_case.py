from use_cases.assign_role_use_case import AccessDeniedError


class RegisterSaleUseCase:
    """
    Accessible to BOTH the SuperAdmin and the Volunteer —
    both roles hold SELL_PRODUCT. This is the everyday "ring up a sale"
    action that keeps the shop running while the SuperAdmin is away.
    """

    def init(self, sale_repository, stock_repository):
        self.sale_repository = sale_repository
        self.stock_repository = stock_repository

    def execute(self, current_user, product_id: int, quantity: int):
        if not current_user.can_sell():
            raise AccessDeniedError("You are not allowed to sell a product.")

        stock = self.stock_repository.find_by_product(product_id)
        stock.remove(quantity)
        self.stock_repository.save(stock)
        # ... create the sale record here (depends on a Sale entity, omitted)