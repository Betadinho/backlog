from app import db, create_app, models
from werkzeug.security import generate_password_hash
from os import path

# if the old database still is needed move it before doing this!
if not path.exists("app/db.sqlite"):
    db.create_all(app=create_app())
    print("Database created.", flush=True)
    # session.add(User(email="Admin@admin.com", name="Admin", password=generate_password_hash(password="admin", method='sha256', salt_length=8), role="Admin"))
    #print("Admin account created.", flush=True)
else:
    db.drop_all(app=create_app())
    print("Old Database has been deleted.", flush=True)    
    db.create_all(app=create_app())
    print("Database created.", flush=True)

'''def db_setup():
    db.create_all(app=create_app())
    print("test2", flush=True)
    return
'''