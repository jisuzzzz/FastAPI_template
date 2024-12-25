from fastapi import APIRouter, Path, HTTPException, status, Depends
from sqlmodel import Session, select
from app.models.model import Todo, TodoCreate, TodoRead
from app.db import get_session
from typing import List


# /todos 경로와 관련된 엔드포인트를 관리하는 라우터
router = APIRouter(prefix="/todos", tags=["todos"])


# Create
@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(*, session: Session = Depends(get_session), todo: TodoCreate):
    """
    새로운 todo를 생성하는 api
    - 요청 데이터: TodoCreate 모델 (title, description, completed 포함)
    - 응답 데이터: 생성된 Todo 객체
    - 상태 코드: 201 Created
    """
    # 요청 데이터를 Todo 객체로 변환
    db_todo = Todo.from_orm(todo)
    session.add(db_todo)  # DB에 추가
    session.commit()  # 변경사항 저장
    session.refresh(db_todo)  # DB에서 갱신된 객체 가져오기
    return db_todo


# Read (모든 todo)
@router.get("/", response_model=List[Todo])
def read_todos(*, session: Session = Depends(get_session), skip: int = 0, limit: int = 100):
    """
    모든 todo를 조회하는 api
    - 페이지네이션
    - 쿼리 매개변수:
        - skip: 데이터를 몇 번째 항목부터 건너뛸지 설정 (기본값: 0)
        - limit: 한 번에 반환할 데이터의 최대 개수 설정 (기본값: 100)
    - 응답 데이터: Todo 객체의 리스트
    """
    # DB에서 todo 목록 조회 (페이지네이션 적용)
    todos = session.exec(select(Todo).offset(skip).limit(limit)).all()
    return todos


# Read (특정 todo)
@router.get("/{todo_id}", response_model=Todo)
def read_todo(*, session: Session = Depends(get_session), todo_id: int = Path(..., title="Todo ID")):
    """
    특정 id todo를 조회하는 api
    - 경로 매개변수: todo_id
    - 응답 데이터: Todo 객체
    - 예외 처리: Todo를 찾을 수 없으면 404 반환
    """
    # ID로 할 일 조회
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Can not find todo")
    return todo


# Update
@router.put("/{todo_id}", response_model=Todo)
def update_todo(
        *,
        session: Session = Depends(get_session),
        todo_id: int = Path(..., title="Todo ID"),
        todo: TodoCreate
):
    """
    특정 id todo를 수정하는 엔드포인트.
    - 경로 매개변수: todo_id
    - 요청 데이터: TodoCreate 모델 (수정할 필드)
    - 응답 데이터: Todo 객체
    - 예외 처리: 찾을 수 없으면 404 반환
    """
    # ID로 할 일 조회
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Can not find todo")

    # 요청 데이터로 기존 객체 업데이트
    todo_data = todo.dict(exclude_unset=True)  # 전달되지 않은 필드는 제외
    for key, value in todo_data.items():
        setattr(db_todo, key, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


# Delete
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(*, session: Session = Depends(get_session), todo_id: int = Path(..., title="Todo ID")):
    """
    특정 id todo 삭제하는 api
    - 경로 매개변수: todo_id
    - 상태 코드: 204 No Content
    - 예외 처리: 찾을 수 없으면 404 반환
    """
    # ID로 할 일 조회
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Can not find todo")

    session.delete(todo)  # 데이터 삭제
    session.commit()
    return None