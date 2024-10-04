from flask import Flask, render_template, Response, request
from data import employees

app = Flask(__name__, static_folder="static", template_folder="static/templates")
app.register_error_handler(404, lambda error: ('bad request!', 404))


@app.route("/")
def get_list():
    return render_template('list.html', employees=employees.values())


@app.route("/<int:employee_id>")
def get(employee_id):
    employee = employees[employee_id]
    return render_template(
        'detail.html', id=employee_id, name=employee['name'], position=employee['position']
    )


@app.route("/<int:employee_id>", methods=["DELETE"])
def delete(employee_id):
    del employees[employee_id]
    return Response(status=204)


@app.route("/<int:employee_id>", methods=["PUT"])
def put(employee_id):
    employee = employees[employee_id]
    employee["name"] = request.json["name"]
    employee["position"] = request.json["position"]
    return Response(status=204)


@app.route("/", methods=["POST"])
def post():
    employee_data = request.json
    employee_data["id"] = max(employees.keys(), default=0) + 1
    employees[employee_data["id"]] = employee_data
    return employee_data
