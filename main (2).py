import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection(u'plant_data').document('plant_0')

doc_ref.set({u'humidity': 69})
try:
    docs = doc_ref.get()
    print(u'Doc Data:{}'.format(docs.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
