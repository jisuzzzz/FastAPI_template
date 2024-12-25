from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import *
from app.api.main import api_router


app = FastAPI()
# cors 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 엔드 포인트
app.include_router(api_router)


# table 만드는 함수
@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
