from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials


basic_schema = HTTPBasic()


def pass_basic_credentials(
        credentials: Annotated[HTTPBasicCredentials, Depends(basic_schema)]):
    if credentials.username != 'admin' or credentials.password != '1':
        return False
    return True
