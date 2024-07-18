from fastapi import FastAPI
from pydantic import BaseModel
import typing
import requests


app = FastAPI()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxMjk1OTAyLCJpYXQiOjE3MjEyOTU2MDIsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImY3NmQxMjZlLTNmMTEtNDBjYi1hMDFmLTEyNzNmYzQ3NGE3NCIsInN1YiI6IjIxZDUxLnNhbXdpbkBzamVjLmFjLmluIn0sImNvbXBhbnlOYW1lIjoiZ29NYXJ0IiwiY2xpZW50SUQiOiJmNzZkMTI2ZS0zZjExLTQwY2ItYTAxZi0xMjczZmM0NzRhNzQiLCJjbGllbnRTZWNyZXQiOiJtandaTVdxUW9rZFZBTnpzIiwib3duZXJOYW1lIjoic2Ftd2luIiwib3duZXJFbWFpbCI6IjIxZDUxLnNhbXdpbkBzamVjLmFjLmluIiwicm9sbE5vIjoiNFNPMjFDUzE0MCJ9.I27OJzxp0zSUNXDNs4RPzSiXctOLKeg8FrPDsTY6DXk"


@app.get("/")
def say_hi():
    return {"hello": "world"}

@app.get("/numbers/{number_id}")
def get_item(number_id: str):
        response = requests.get(
        "http://20.244.56.144/test/primes",
        headers={"Authorization": f"Bearer {token}"}
        )
        
        return {"number_id": f"{response.json()}"}
