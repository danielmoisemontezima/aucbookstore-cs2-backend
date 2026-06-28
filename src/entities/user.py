from entities.role import Role
from entities.permission import Permission


class User:
    """
    Core Entity representing anyone with an account in the system.
    The role assigned to a user is what determines whether they act as
    a SuperAdmin or a Volunteer — there is no separate class per role.

    This class has ZERO external dependencies: no Flask, no SQLite,
    no HTTP. It must be usable in a plain Python script with no server.
    """

    def init(self, user_id: int, name: str, role: Role, is_active: bool = True):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.is_active = is_active  # lets the SuperAdmin "deactivate" a volunteer

    def has_permission(self, permission: Permission) -> bool:
        # An inactive account never has any permission, regardless of role.
        if not self.is_active:
            return False
        return self.role.has(permission)

    # --- Role management ---
    def can_assign_role(self) -> bool:
        return self.has_permission(Permission.ASSIGN_ROLES)

    def can_manage_users(self) -> bool:
        return self.has_permission(Permission.MANAGE_USERS)

    # --- Shop ---
    def can_sell(self) -> bool:
        return self.has_permission(Permission.SELL_PRODUCT)

    def can_manage_products(self) -> bool:
        return self.has_permission(Permission.MANAGE_PRODUCTS)

    def can_manage_stock(self) -> bool:
        return self.has_permission(Permission.MANAGE_STOCK)

    def can_cancel_order(self) -> bool:
        return self.has_permission(Permission.CANCEL_ORDER)

    def can_view_sales_reports(self) -> bool:
        return self.has_permission(Permission.VIEW_SALES_REPORTS)

    # --- Printing ---
    def can_execute_print_job(self) -> bool:
        return self.has_permission(Permission.EXECUTE_PRINT_JOB)

    def can_configure_print_pricing(self) -> bool:
        return self.has_permission(Permission.CONFIGURE_PRINT_PRICING)