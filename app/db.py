from sqlmodel import create_engine, Session, SQLModel
from app.config import DATABASE_URL

# SQLModel 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)  # echo=True는 SQL 쿼리를 로그로 출력


# 테이블 생성
def create_tables():
    SQLModel.metadata.create_all(engine)


# 데이터베이스 세션 생성
def get_session():
    with Session(engine) as session:
        yield session
