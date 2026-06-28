from entities.permission import Permission


class Role:
    """
    A role is a SET of permissions. This is the ONLY place where the
    "power" of each role is defined for the whole system.
    """

    def init(self, name: str, permissions: set[Permission]):
        self.name = name
        self.permissions = permissions

    def has(self, permission: Permission) -> bool:
        return permission in self.permissions


# === SUPER ADMIN ===
# Full authority: owner of the bookstore AND the main seller of the shop.
SUPER_ADMIN_ROLE = Role("SUPER_ADMIN", {
    Permission.MANAGE_BOOKS,
    Permission.LEND_BOOK,
    Permission.RETURN_BOOK,
    Permission.VIEW_CATALOG,
    Permission.MANAGE_USERS,
    Permission.ASSIGN_ROLES,
    Permission.DELETE_ACCOUNT,
    Permission.MANAGE_PRODUCTS,
    Permission.SELL_PRODUCT,
    Permission.MANAGE_STOCK,
    Permission.MANAGE_ORDERS,
    Permission.CANCEL_ORDER,
    Permission.VIEW_SALES_REPORTS,
    Permission.EXECUTE_PRINT_JOB,
    Permission.CONFIGURE_PRINT_PRICING,
})

# === VOLUNTEER ===
# Limited access: a student who temporarily fills in when the SuperAdmin
# is absent. Can serve customers, but cannot manage the business itself.
VOLUNTEER_ROLE = Role("VOLUNTEER", {
    Permission.LEND_BOOK,
    Permission.RETURN_BOOK,
    Permission.VIEW_CATALOG,
    Permission.SELL_PRODUCT,
    Permission.MANAGE_ORDERS,
    Permission.EXECUTE_PRINT_JOB,
    # Explicitly NOT granted:
    # MANAGE_BOOKS, MANAGE_PRODUCTS, MANAGE_STOCK, CANCEL_ORDER,
    # VIEW_SALES_REPORTS, ASSIGN_ROLES, MANAGE_USERS, DELETE_ACCOUNT,
    # CONFIGURE_PRINT_PRICING
})