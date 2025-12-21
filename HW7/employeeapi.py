import requests


class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user, password):
        creds = {"username": user, "password": password}
        resp = requests.post(f"{self.url}/auth/login", json=creds)

        assert resp.status_code == 200, (
            f"Error:Awaiting status 200, get {resp.status_code}"
        )

        return resp.json()["user_token"]

    def create_employee(
            self,
            first_name,
            last_name,
            middle_name,
            company_id,
            email,
            phone,
            birthdate,
            is_active
    ):
        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }

        resp = requests.post(
            f"{self.url}/employee/create",
            json=employee_data
        )

        assert resp.status_code == 200, (
            f"Error:Awaiting status 200, get {resp.status_code}"
        )

        return resp.json()

    def get_employee(self, employee_id):
        resp = requests.get(
            f"{self.url}/employee/info/{employee_id}"
        )

        assert resp.status_code == 200, (
            f"Error:Awaiting status 200, get {resp.status_code}"
        )

        return resp.json()

    def update_employee(self, employee_id, user, password, **fields):
        client_token = self.get_token(user, password)

        url_with_token = (
            f"{self.url}/employee/change/"
            f"{employee_id}?client_token={client_token}"
        )

        resp = requests.patch(
            url_with_token,
            json=fields,
        )

        assert resp.status_code == 200, (
            f"Error:Awaiting status 200, get {resp.status_code}"
        )

        return resp.json()