from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import bcrypt
import firebase_admin
from firebase_admin import credentials, firestore
import uuid
from fastapi.responses import Response
import re 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not firebase_admin._apps:
    cred = credentials.Certificate("backend/config/firebase.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def check(email: str, token: str):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA0-9-.]+$'
    if not re.match(email_regex, email):
        raise HTTPException(status_code=403, detail="Adresse mail invalide !")

    doc_id = None
    collection_name = 'users'
    users_ref = db.collection(collection_name).where('email', '>=', email).where('email', '<=', email + '\uf8ff')

    for doc in users_ref.stream():    
        doc_id = doc.id
        stored_token = doc.to_dict().get('token')
        break

    if not doc_id or stored_token != token:
        raise HTTPException(status_code=401, detail="Token invalide")

    return True

@app.get("/")
async def home():
    return {"message": "API FastAPI OK avec CORS"}

@app.post("/login")
async def login(loginInfos: dict = Body(...)):
    email = loginInfos["email"]
    password = loginInfos["password"]

    users_ref = db.collection("users")
    docs = users_ref.where("email", "==", email).stream()

    for doc in docs:
        user_data = doc.to_dict()
        hashed_pw = user_data["password"]

        if bcrypt.checkpw(password.encode("utf-8"), hashed_pw.encode("utf-8")):
            token = str(uuid.uuid4())

            user_ref = db.collection('users').document(doc.id)

            user_ref.update({
                'token': token
            })

            return {"message": token}
        else:
            raise HTTPException(status_code=401, detail="Mot de passe incorrect")

    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

def api_start():
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=5000)

if __name__ == "__main__":
    api_start()
