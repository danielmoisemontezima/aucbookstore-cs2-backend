import sqlite3
from interfaces.repository_interfaces import IUserRepository
from entities.user import User
from entities.role import SUPER_ADMIN_ROLE, VOLUNTEER_ROLE


def map_role_from_name(role_name: str):
    """Technical detail: converts a stored string back into a Role object."""
    return {
        "SUPER_ADMIN": SUPER_ADMIN_ROLE,
        "VOLUNTEER": VOLUNTEER_ROLE,
    }[role_name]


class SQLiteUserRepository(IUserRepository):
    """
    Concrete implementation — SQLite only appears HERE.
    """

    def init(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def find_by_id(self, user_id: int):
        cursor = self.conn.execute(
            "SELECT id, name, role_name, is_active FROM users WHERE id = ?",
            (user_id,),
        )
        row = cursor.fetchone()
        if row is None:
            return None

        role = map_role_from_name(row[2])
        return User(user_id=row[0], name=row[1], role=role, is_active=bool(row[3]))

    def save(self, user: User):
        self.conn.execute(
            "UPDATE users SET role_name = ?, is_active = ? WHERE id = ?",
            (user.role.name, user.is_active, user.user_id),
        )
        self.conn.commit()