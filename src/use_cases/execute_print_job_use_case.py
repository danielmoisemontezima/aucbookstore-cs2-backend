from use_cases.assign_role_use_case import AccessDeniedError


class ExecutePrintJobUseCase:
    """
    Accessible to BOTH the SuperAdmin and the Volunteer.
    The volunteer can run a print job and hand it to the customer,
    but this use case never touches pricing — see
    ConfigurePrintPricingUseCase for that responsibility.
    """

    def init(self, print_job_repository):
        self.print_job_repository = print_job_repository

    def execute(self, current_user, print_job_id: int):
        if not current_user.can_execute_print_job():
            raise AccessDeniedError("You are not allowed to run a print job.")

        job = self.print_job_repository.find_by_id(print_job_id)
        job.status = "IN_PROGRESS"
        self.print_job_repository.save(job)

    def hand_to_customer(self, current_user, print_job_id: int):
        if not current_user.can_execute_print_job():
            raise AccessDeniedError("You are not allowed to hand over this job.")

        job = self.print_job_repository.find_by_id(print_job_id)
        job.status = "HANDED_TO_CUSTOMER"
        self.print_job_repository.save(job)