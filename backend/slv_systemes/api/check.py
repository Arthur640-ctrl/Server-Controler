import re
import firebase_admin
from firebase_admin import credentials, firestore
from fastapi.responses import Response  # Assurez-vous d'importer Response de FastAPI si vous l'utilisez

# Initialisation de Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("backend/config/firebase.json")
    firebase_admin.initialize_app(cred)

# Client Firestore
db = firestore.client()

def check(email: str, token: str):
    # Validation de l'email avec une expression régulière
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return Response("403 Forbidden: Adresse mail invalide !", status_code=403)

    doc_id = None
    collection_name = 'users'
    # Recherche de l'utilisateur par email dans Firestore
    users_ref = db.collection(collection_name).where('email', '>=', email).where('email', '<=', email + '\uf8ff')

    for doc in users_ref.stream():    
        doc_id = doc.id
        stored_token = doc.to_dict().get('token')
        break

    # Vérification du token
    if not doc_id or stored_token != token:
        return Response("401 Unauthorized: Token invalide", status_code=401)
    
    return True
