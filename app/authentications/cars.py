from typing import Annotated

from bcrypt import gensalt, hashpw
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="cars/token")

hash_and_salt = {}

def hash_password(password: str):
    salt = gensalt()
    hashed_password = hashpw(password.encode(), salt)
    hash_and_salt['hashed_password'] = hashed_password
    print(hash_and_salt['hashed_password'].decode())
    return hashed_password


def get_token(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if credentials.username != 'admin' or credentials.password != 'qwerty':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    return hash_password(credentials.password)


def pass_token(token: Annotated[str, Depends(oauth2_scheme)]):
    if token != hash_and_salt['hashed_password'].decode(): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication token") 

