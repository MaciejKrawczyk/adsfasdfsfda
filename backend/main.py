from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from fastapi.responses import RedirectResponse


app = FastAPI()


class Data(BaseModel):
    test: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def home_get():
    return {"hello": "world"}


@app.post('/postText/')
def home_post(data: Data):
    print(data)
    return 'luzzzz'


@app.post('/upload/')
async def upload_file(file: List[UploadFile] = File(...)):

    # print(file.filename)
    for x in file:
        file_content = await x.read()
        # print(file_content)
        with open(f'Storage\\{x.filename}', 'wb') as f:
            # shutil.copyfileobj(file.file, buffer)
            f.write(file_content)

    return {"file_name": file}
    # return RedirectResponse('http://localhost:3000/')