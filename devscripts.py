from app import db, create_app

# if the old database still is needed move it before doing this!
db.drop_all(app=create_app())
print("Old Database has been deleted.", flush=True)    
db.create_all(app=create_app())
print("Database created.", flush=True)    

'''def db_setup():
    db.create_all(app=create_app())
    print("test2", flush=True)
    return
'''