from fastapi import FastAPI
import os
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fastapi-demo-90c20-626c89869d6f.json"
dataBase = firestore.Client()
app = FastAPI()

@app.get("/address")
def get_address():
    postcode = os.getenv("POSTCODE", "00000")
    
    data = {
        "street": "Oxford Street",
        "city": "London",
        "country": "United Kingdom",
        "postcode": postcode
    }

    # Save to Firestore in a collection called "responses"
    dataBase.collection("responses").add(data)

    return data
