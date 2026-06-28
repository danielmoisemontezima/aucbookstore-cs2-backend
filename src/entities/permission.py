from enum import Enum


class Permission(Enum):
    """
    Pure business permissions. Each member represents a business CAPABILITY,
    never a technical detail (no HTTP route, no SQL table name).
    """

    # --- Book management ---
    MANAGE_BOOKS = "MANAGE_BOOKS"
    LEND_BOOK = "LEND_BOOK"
    RETURN_BOOK = "RETURN_BOOK"
    VIEW_CATALOG = "VIEW_CATALOG"

    # --- User / role management ---
    MANAGE_USERS = "MANAGE_USERS"
    ASSIGN_ROLES = "ASSIGN_ROLES"
    DELETE_ACCOUNT = "DELETE_ACCOUNT"

    # --- Online shop (supplies, badges, jerseys) ---
    MANAGE_PRODUCTS = "MANAGE_PRODUCTS"
    SELL_PRODUCT = "SELL_PRODUCT"
    MANAGE_STOCK = "MANAGE_STOCK"
    MANAGE_ORDERS = "MANAGE_ORDERS"
    CANCEL_ORDER = "CANCEL_ORDER"
    VIEW_SALES_REPORTS = "VIEW_SALES_REPORTS"

    # --- Printing services: split into two distinct responsibilities ---
    EXECUTE_PRINT_JOB = "EXECUTE_PRINT_JOB"        # run the job + hand it to the customer
    CONFIGURE_PRINT_PRICING = "CONFIGURE_PRINT_PRICING"  # change prices/parameters