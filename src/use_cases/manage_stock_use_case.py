from use_cases.assign_role_use_case import AccessDeniedError


class ManageStockUseCase:
    """
    Reserved for the SuperAdmin only. A volunteer can SELL (which reduces
    stock as a side effect, see RegisterSaleUseCase) but cannot manually
    adjust inventory counts (e.g. restocking, correcting errors).
    """

    def init(self, stock_repository):
        self.stock_repository = stock_repository

    def execute(self, current_user, product_id: int, new_quantity: int):
        if not current_user.can_manage_stock():
            raise AccessDeniedError("Only the SuperAdmin can adjust stock levels.")

        stock = self.stock_repository.find_by_product(product_id)
        stock.quantity = new_quantity
        self.stock_repository.save(stock)