from datetime import datetime, timedelta
from jose import JWTError, jwt


SECRET_KEY = "d92ddwero09sdk02knds93n5njn55"
ALGORITHAM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 30

def create_token(data:dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        
    else:
        expires_delta = datetime.utcnow() + expires_delta(ACCESS_TOKEN_EXPIRE_MIN)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHAM)
        return encoded_jwt