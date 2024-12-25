from sqlmodel import SQLModel, Field
from typing import Optional


# 기본 모델
# 공통으로 사용될 필드를 정의하는 부모 클래스
class TodoBase(SQLModel):
    title: str
    # Optinal -> 값이 null일 수도 있다
    description: Optional[str] = None
    completed: bool = False


# todo table model 정의
# SQLModel의 테이블 매핑을 위해 table=True로 설정하고, id를 primary key로 설정
class Todo(TodoBase, table=True):
    # id가 primary key인데 Optional이 붙은 이유:
    # -> Python에서 객체를 처음 생성할 때는 id 값이 없음
    # -> id는 데이터베이스에 삽입될 때 자동으로 생성됨
    # -> Optional[int]를 통해 Python 코드에서 id가 None인 상태를 허용
    id: Optional[int] = Field(default=None, primary_key=True)


# 데이터 생성 시 사용하는 모델
# 요청으로 들어오는 데이터에 대해 유효성을 검사하는 데 사용됩니다.
class TodoCreate(TodoBase):
    pass  # TodoBase의 필드만 사용 (id는 필요 없음)


# 데이터 조회 시 사용하는 모델
# 클라이언트에게 데이터를 반환할 때 사용되며, id 필드를 포함합니다.
class TodoRead(TodoBase):
    # 조회 응답에 포함될 고유 ID
    id: int