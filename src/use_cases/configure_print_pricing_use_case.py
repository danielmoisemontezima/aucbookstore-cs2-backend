
from use_cases.assign_role_use_case import AccessDeniedError


class ConfigurePrintPricingUseCase:
    """
    Reserved EXCLUSIVELY for the SuperAdmin. Deliberately separated from
    ExecutePrintJobUseCase (Single Responsibility Principle) — a bug here
    can never affect the print execution flow, and vice versa.
    """

    def init(self, pricing_repository):
        self.pricing_repository = pricing_repository

    def execute(self, current_user, print_type: str, new_price: float):
        if not current_user.can_configure_print_pricing():
            raise AccessDeniedError("Only the SuperAdmin can change print pricing.")
        if new_price < 0:
            raise ValueError("Price cannot be negative.")

        pricing = self.pricing_repository.find_by_type(print_type)
        pricing.price = new_price
        self.pricing_repository.save(pricing)