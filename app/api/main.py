from fastapi import APIRouter
from app.api.routes import todo

# 엔드포인트 앞에 /api로 시작하게 설정
# 모든 하위 라우트에 공통적으로 "/api"를 접두사로 추가
api_router = APIRouter(prefix="/api")

# /api/todos와 같은 경로로 라우트를 포함
api_router.include_router(todo.router)