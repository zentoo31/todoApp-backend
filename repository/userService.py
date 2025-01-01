from sqlalchemy.orm import Session
from config.db import get_db
from models.users import User
import bcrypt 

class UserService:
    
    @staticmethod
    def register(first_names, last_names, username, email, password):
        with next(get_db()) as db:
            existing_user = db.query(User).filter(User.email == email).first()
            if existing_user:
                return {"error": "Email already in use"}

            if len(password) > 20:
                return {"error": "the password must be shorter"}
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt=bcrypt.gensalt())
            
            new_user = User(
                first_names=first_names,
                last_names=last_names,
                username=username,
                email=email,
                password=hashed_password  
            )

            try:
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
            except Exception as e:
                db.rollback()
                return {"error": f"An error occurred: {str(e)}"}

            return {"message": "User registered successfully", "user_id": new_user.id}
        
    @staticmethod
    def login(email, password):
        with next(get_db()) as db:
            existing_user = db.query(User).filter(User.email == email).first()
            if not existing_user:
                return {"error": "The user not exists"}
            
            password_binary = password.encode('utf-8')
            
            result = bcrypt.checkpw(password=password_binary, hashed_password=existing_user.password)
            
            return result