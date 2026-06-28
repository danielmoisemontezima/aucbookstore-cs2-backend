class AccessDeniedError(Exception):
    pass


class AssignRoleUseCase:
    """
    Only the SuperAdmin can designate a Volunteer (or revoke that role).
    This is how the SuperAdmin "hires" a student as a temporary helper.
    """

    def init(self, user_repository):
        self.user_repository = user_repository  # abstraction, not a concrete DB

    def execute(self, current_user, target_user_id: int, new_role):
        if not current_user.can_assign_role():
            raise AccessDeniedError("Only the SuperAdmin can assign a role.")

        target_user = self.user_repository.find_by_id(target_user_id)
        target_user.role = new_role
        self.user_repository.save(target_user)