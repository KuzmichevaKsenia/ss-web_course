from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import EmployeeModel
from schemas import EmployeeSchema, EmployeeCreateOrUpdateSchema

blp = Blueprint("Employees", __name__)


@blp.route("/employee/<int:employee_id>")
class Employee(MethodView):
    @blp.response(200, EmployeeSchema)
    def get(self, employee_id):
        return EmployeeModel.query.get_or_404(employee_id)

    @blp.response(204)
    def delete(self, employee_id):
        emp = EmployeeModel.query.get_or_404(employee_id)
        db.session.delete(emp)
        db.session.commit()

    @blp.arguments(EmployeeCreateOrUpdateSchema)
    @blp.response(204)
    def put(self, employee_data, employee_id):
        employee = EmployeeModel.query.get_or_404(employee_id)
        employee.name = employee_data["name"]
        employee.position = employee_data["position"]
        db.session.add(employee)
        db.session.commit()


@blp.route("/employees")
class GetEmployees(MethodView):
    @blp.response(200, EmployeeSchema(many=True))
    def get(self):
        return EmployeeModel.query.all()


@blp.route("/employee")
class CreateEmployee(MethodView):
    @blp.arguments(EmployeeCreateOrUpdateSchema)
    @blp.response(201, EmployeeSchema)
    def post(self, employee_data):
        employee = EmployeeModel(**employee_data)
        try:
            db.session.add(employee)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=str(err))

        return employee
