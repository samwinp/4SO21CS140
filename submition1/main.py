from fastapi import FastAPI
from pydantic import BaseModel
import typing
import requests


app = FastAPI()

windowPrevState = []
windowCurrentState = []
numbers = []
avg = 0


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxMjk2NDcwLCJpYXQiOjE3MjEyOTYxNzAsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImY3NmQxMjZlLTNmMTEtNDBjYi1hMDFmLTEyNzNmYzQ3NGE3NCIsInN1YiI6IjIxZDUxLnNhbXdpbkBzamVjLmFjLmluIn0sImNvbXBhbnlOYW1lIjoiZ29NYXJ0IiwiY2xpZW50SUQiOiJmNzZkMTI2ZS0zZjExLTQwY2ItYTAxZi0xMjczZmM0NzRhNzQiLCJjbGllbnRTZWNyZXQiOiJtandaTVdxUW9rZFZBTnpzIiwib3duZXJOYW1lIjoic2Ftd2luIiwib3duZXJFbWFpbCI6IjIxZDUxLnNhbXdpbkBzamVjLmFjLmluIiwicm9sbE5vIjoiNFNPMjFDUzE0MCJ9.aPkHZ8AmBZvSxqza7EctUi8HQH7as3pnBoSkRNh-YJA"
@app.get("/")
def say_hi():
    return {"hello": "world"}

@app.get("/numbers/{number_id}")
def get_item(number_id: str):

        
    if number_id == "e":
            response = requests.get(
            "http://20.244.56.144/test/even",
            headers={"Authorization": f"Bearer {token}"}
            )
            return  {"number_id" : f"{response.json()}"}
    
    if number_id == "p":
        response = requests.get(
        "http://20.244.56.144/test/primes",
        headers={"Authorization": f"Bearer {token}"}
        )
        return  {"number_id" : f"{response.json()}"}
    
    if number_id == "f":
        response = requests.get(
        "http://20.244.56.144/test/fibo",
        headers={"Authorization": f"Bearer {token}"}
        )
        return  {"number_id" : f"{response.json()}"}
    
    if number_id == "r":
         response = requests.get(
             "http://20.244.56.144/test/rand",
             headers={"Authorization": f"Bearer {token}"}
         )

    return {"number_id": f"{response.json()}"}
