from use_cases.assign_role_use_case import AccessDeniedError


class CancelOrderUseCase:
    """
    Reserved for the SuperAdmin only — the Volunteer does not hold
    CANCEL_ORDER. Cancelling/refunding an order is a financial decision.
    """

    def init(self, order_repository):
        self.order_repository = order_repository

    def execute(self, current_user, order_id: int):
        if not current_user.can_cancel_order():
            raise AccessDeniedError("Only the SuperAdmin can cancel an order.")

        order = self.order_repository.find_by_id(order_id)
        order.status = "CANCELLED"
        self.order_repository.save(order)