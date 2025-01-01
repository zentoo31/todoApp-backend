from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from config.config import DATABASE_URL
from models import Base

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
    
    def reset_database(self):
        try:
            print("Dropping all tables...")
            Base.metadata.drop_all(self.engine)
            print("All tables dropped successfully.")
            
            print("Creating all tables...")
            Base.metadata.create_all(self.engine)
            print("All tables created successfully.")
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    manager = DatabaseManager()
    manager.reset_database()