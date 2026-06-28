from flask import Flask, request, jsonify

from use_cases.assign_role_use_case import AssignRoleUseCase, AccessDeniedError
from use_cases.register_sale_use_case import RegisterSaleUseCase
from use_cases.cancel_order_use_case import CancelOrderUseCase
from use_cases.execute_print_job_use_case import ExecutePrintJobUseCase
from use_cases.configure_print_pricing_use_case import ConfigurePrintPricingUseCase
from adapters.sqlite_user_repository import SQLiteUserRepository, map_role_from_name

app = Flask(name)

# Dependency injection — wired together at the outermost layer only.
user_repo = SQLiteUserRepository("bookstore.db")
assign_role_use_case = AssignRoleUseCase(user_repo)


@app.route("/admin/assign-role", methods=["POST"])
def assign_role_handler():
    current_user = request.current_user  # set by an auth middleware (not shown)
    data = request.json

    try:
        new_role = map_role_from_name(data["new_role_name"])
        assign_role_use_case.execute(current_user, data["target_user_id"], new_role)
        return jsonify({"message": "Role assigned successfully."}), 200
    except AccessDeniedError as e:
        return jsonify({"error": str(e)}), 403


@app.route("/shop/print-jobs/<int:job_id>/execute", methods=["POST"])
def execute_print_job_handler(job_id):
    current_user = request.current_user
    try:
        execute_print_job_use_case.execute(current_user, job_id)
        return jsonify({"message": "Print job started."}), 200
    except AccessDeniedError as e:
        return jsonify({"error": str(e)}), 403


@app.route("/admin/print-pricing", methods=["PUT"])
def configure_print_pricing_handler():
    current_user = request.current_user
    data = request.json
    try:
        configure_print_pricing_use_case.execute(
            current_user, data["print_type"], data["new_price"]
        )
        return jsonify({"message": "Pricing updated."}), 200
    except AccessDeniedError as e:
        return jsonify({"error": str(e)}), 403
    except ValueError as e:
        return jsonify({"error": str(e)}), 400