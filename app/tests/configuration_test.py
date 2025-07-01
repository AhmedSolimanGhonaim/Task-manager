#
#!!!!!!!!!!!!! under development tests for configuration



# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
# from app.db.session import get_session

# from sqlmodel import create_engine ,SQLModel

# DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(DATABASE_URL, echo=True)

# @pytest.fixture(scope="function")
# def db_session():
    
#     SQLModel.metadata.create_all(engine)
#     db = TestingSessionLocal()
#     try :
#         yield db
#     finally:
#         db.close()
#         SQLModel.metadata.drop_all(engine)
   

