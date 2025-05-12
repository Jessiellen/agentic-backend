from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "sua-chave-secreta"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    expires = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode({**data, "exp": expires}, SECRET_KEY, algorithm=ALGORITHM)