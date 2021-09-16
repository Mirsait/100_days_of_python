from datetime import datetime
import requests

PIXELA_TOKEN = "your own token"
PIXELA_USERNAME = "your own username"
pixela_endpoint = "https://pixe.la/v1/users"
pixela_graphs_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
headers = {"X-USER-TOKEN": PIXELA_TOKEN}


def create_user(token: str, username: str):
    """ create new user if it is not exists """
    create_user_data = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=create_user_data)
    print(response.text)


def create_graph(headers: dict, data: dict):
    """ create new graph """
    response = requests.post(url=pixela_graphs_endpoint,
                             headers=headers, json=data)
    response.raise_for_status()
    print(response.text)


def strdate(date: datetime) -> str:
    """ get date in format yyyyMMdd  """
    return date.strftime("%Y%m%d")


def get_pixel_endpoint(graph_id: str) -> str:
    return f"{pixela_graphs_endpoint}/{graph_id}"


def get_pixel_data(date: str, count: float) -> dict:
    data = {"date": date, "quantity": f"{count:.2f}"}
    return data


def create_pixel(pixel_url: str, headers: dict, data: dict):
    """ create new pixel """
    response = requests.post(url=pixel_url, headers=headers, json=data)
    response.raise_for_status()
    print(response.text)


def delete_pixel(graph_id: str, date: datetime, headers: dict):
    """ delete pixel """
    graph = get_pixel_endpoint(graph_id)
    pi_date = strdate(date)
    pi_url = f"{graph}/{pi_date}"
    response = requests.delete(pi_url, headers=headers)
    response.raise_for_status()
    print(response.text)


def add_pixel(graph_id: str, date: datetime, headers: dict, quatity: float):
    """ add quantity to exist pixel """
    graph = get_pixel_endpoint(graph_id=graph_id)
    pi_date = strdate(date)
    pi_url = f"{graph}/{pi_date}"

    get_res = requests.get(url=pi_url, headers=headers)
    pixel = get_res.json()

    old_quantity = float(pixel["quantity"])
    new_quantity = old_quantity + quatity
    new_data = {"quantity": f"{new_quantity:.2f}"}

    upd_res = requests.put(url=pi_url, json=new_data, headers=headers)
    upd_res.raise_for_status()
    print(upd_res.text)


create_user(token=PIXELA_TOKEN, username=PIXELA_USERNAME)

graph_id = "piano-21"
create_graph_data = {
    "id": graph_id,
    "name": "piano-practice",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}
create_graph(headers=headers, data=create_graph_data)

today = strdate(date=datetime.today())
pi_url = get_pixel_endpoint(graph_id=graph_id)
pi_count = 2
pi_data = get_pixel_data(date=today, count=pi_count)
create_pixel(pixel_url=pi_url, headers=headers, data=pi_data)

add_pixel(graph_id=graph_id, date=datetime.today(),
          headers=headers, quatity=2.23)

delete_pixel(graph_id=graph_id, date=datetime.today(), headers=headers)
