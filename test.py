import bcrypt
from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI, Body, UploadFile
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

# Exemple de mot de passe
password = "test"

# Générer un salt pour le hashage
salt = bcrypt.gensalt()


hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

cred = credentials.Certificate('backend/config/firebase.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('users').add({
    'email': 'test@test.com',
    'password': hashed_password
})
