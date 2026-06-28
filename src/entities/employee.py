"""
Entity: Employee
Clean Architecture — AUC Bookstore Project
Layer: Domain / Entities

Author: [LAURENT-MIKE]
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class EmployeeStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ON_LEAVE = "on_leave"


class EmployeeRole(Enum):
    CASHIER = "cashier"
    MANAGER = "manager"
    STOCK_CLERK = "stock_clerk"
    ADMIN = "admin"


@dataclass
class Employee:
    """
    Represents an Employee working at the AUC Bookstore.

    This is a pure business entity following Clean Architecture
    principles — independent of any database or framework.
    """

    id: int
    name: str
    email: str
    role: EmployeeRole
    job_title: str = ""
    status: EmployeeStatus = EmployeeStatus.ACTIVE
    hire_date: date = field(default_factory=date.today)

    # ------------------------------------------------------------------
    # BUSINESS RULES
    # Constraints that define what makes an Employee valid.
    # ------------------------------------------------------------------

    def _post_init_(self):
        if not self.name or not self.name.strip():
            raise ValueError("Employee name cannot be empty.")
        if not self.email or "@" not in self.email:
            raise ValueError("Employee email must be a valid email address.")

    # ------------------------------------------------------------------
    # BUSINESS LOGIC
    # Behaviors and actions an Employee can perform.
    # ------------------------------------------------------------------

    def deactivate(self):
        """Marks the employee as inactive."""
        self.status = EmployeeStatus.INACTIVE

    def activate(self):
        """Marks the employee as active."""
        self.status = EmployeeStatus.ACTIVE

    def put_on_leave(self):
        """Marks the employee as on leave."""
        self.status = EmployeeStatus.ON_LEAVE

    def is_active(self) -> bool:
        """Returns True if the employee is currently active."""
        return self.status == EmployeeStatus.ACTIVE

    def change_role(self, new_role: EmployeeRole):
        """Changes the employee's role."""
        self.role = new_role