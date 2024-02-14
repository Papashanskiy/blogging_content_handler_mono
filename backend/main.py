from fastapi import FastAPI, File, UploadFile
from authorization import auth
from core import api


app = FastAPI()

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(api.router, prefix='/api', tags=['api'])
