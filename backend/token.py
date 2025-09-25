from datetime import datetime, timedelta
from jose import JWTError, jwt


SECRET_KEY = "d92ddwero09sdk02knds93n5njn55"
ALGORITHAM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 30

def create_token(data:dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta