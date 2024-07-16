function openEditModal(emp_id = "") {
    let name = ""
    let position = ""
    if (emp_id) {
        name = document.getElementById("name-" + emp_id).textContent
        position = document.getElementById("position-" + emp_id).textContent
    }
    document.getElementById("input-name" + emp_id).value = name
    document.getElementById("input-position" + emp_id).value = position
    let elem = document.getElementById("modal" + emp_id)
    elem.classList.remove('hidden')
}

function closeEditModal(emp_id = "") {
    let elem = document.getElementById("modal" + emp_id)
    elem.classList.add('hidden')
}

async function saveEmployee(emp_id = "") {
    let new_name = document.getElementById("input-name" + emp_id).value
    let new_position = document.getElementById("input-position" + emp_id).value
    if (emp_id) {
        await updateEmployee(emp_id, new_name, new_position)
    } else {
        await addEmployee(new_name, new_position)
    }
}


async function updateEmployee(emp_id, new_name, new_position) {
    let response = await fetch(
        '/' + emp_id,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({
                'name': new_name,
                'position': new_position
            })
        }
    )
    if (response.ok) {
        closeEditModal(emp_id)
        document.getElementById("name-" + emp_id).textContent = new_name
        document.getElementById("position-" + emp_id).textContent = new_position
    } else {
        alert("Failed to update employee :(")
    }
}

async function addEmployee(new_name, new_position) {
    let response = await fetch(
        '/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: JSON.stringify({
                'name': new_name,
                'position': new_position
            })
        }
    )
    if (response.ok) {
        location.reload();
    } else {
        alert("Failed to add employee :(")
    }
}