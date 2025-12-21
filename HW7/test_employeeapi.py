import pytest
from .employeeapi import EmployeeApi

BASE_URL = "http://5.101.50.27:8000"
TEST_USER = "harrypotter"
TEST_PASSWORD = "expelliarmus"
TEST_EMPLOYEE_ID = 1


@pytest.fixture
def api():
    return EmployeeApi(BASE_URL)


def test_create_employee(api):
    employee_data = {
        "first_name": "Taras",
        "last_name": "Bulba",
        "middle_name": "Georgi",
        "company_id": 1,
        "email": "bulba_test@gmail.com",
        "phone": "1523541",
        "birthdate": "1982-11-19",
        "is_active": True
    }

    result = api.create_employee(**employee_data)

    for key, value in employee_data.items():
        assert result[key] == value, (
            f"Field {key} dont match. Expected {value}, get {result[key]}"
        )


def test_get_employee(api):
    employee = api.get_employee(TEST_EMPLOYEE_ID)

    assert isinstance(employee, dict)
    assert "first_name" in employee
    assert "last_name" in employee


def test_update_employee(api):
    update_data = {
        "last_name": "Petkya",
        "email": "updated_petkya_test@example.com",
        "phone": "1321257",
        "is_active": False
    }

    updated_employee = api.update_employee(
        employee_id=TEST_EMPLOYEE_ID,
        user=TEST_USER,
        password=TEST_PASSWORD,
        **update_data
    )

    for key, value in update_data.items():
        assert updated_employee[key] == value


def test_allowed_fields(api):
    updatable_fields = [
        ("last_name", "Dimitrius"),
        ("email", "test_dimka_allowed@example.com"),
        ("phone", "8398591"),
        ("is_active", True),
        ("company_id", 1),
    ]

    for field, new_value in updatable_fields:
        updated = api.update_employee(
            employee_id=TEST_EMPLOYEE_ID,
            user=TEST_USER,
            password=TEST_PASSWORD,
            **{field: new_value}
        )

        assert updated[field] == new_value


def test_update_multiple_fields(api):
    update_data = {
        "last_name": "Zahrenko",
        "email": "multizah_update@test.com",
        "phone": "9136862",
        "is_active": True
    }

    updated = api.update_employee(
        employee_id=TEST_EMPLOYEE_ID,
        user=TEST_USER,
        password=TEST_PASSWORD,
        **update_data
    )

    for key, value in update_data.items():
        assert updated[key] == value