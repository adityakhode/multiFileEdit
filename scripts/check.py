import requests
import firebase_admin
from firebase_admin import firestore, credentials

# Firebase configuration
API_KEY  = "AIzaSyDyL1ZInfooam57Ce8FeiZ2LpgU5Egbr7Y "  # Replace with your Firebase API Key
BASE_URL = "https://identitytoolkit.googleapis.com/v1/accounts:"

cred = credentials.Certificate("scripts/cred.json")
firebase_admin.initialize_app(cred)


class Check():

    def login(email, password):

        url = f"{BASE_URL}signInWithPassword?key={API_KEY}"
        data = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("Successful login")
            return True
        else:
            print(f"Unsuccessful login: {response.json().get('error', {}).get('message')}")
            return False
        
    def signup(email, name, surname, phone, password):
        db = firestore.client()
        url = f"{BASE_URL}signUp?key={API_KEY}"

        data = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            data = {
                        "email"    : email   ,
                        "name"     : name    ,
                        "surname"  : surname ,
                        "phone"    : phone   ,
                        "password" : password
                    }

            doc_ref = db.collection("userDetails").document(email)
            doc_ref.set(data)
            return True
        else:
            return False