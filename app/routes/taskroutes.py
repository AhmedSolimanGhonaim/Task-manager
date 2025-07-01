# end points


from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.crud import cruds
from app.models.taskmodel import Task

from app.schemas.taskschema import TaskCreate, TaskUpdate, TaskResponse
from app.models.taskmodel import TaskPriority, TaskStatus

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# http cruds


@router.get("/", response_model=list[TaskResponse])
def get_list_of_tasks(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return cruds.get_all_tasks(session, skip=skip, limit=limit)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task_data: TaskCreate, session: Session = Depends(get_session)):

    return cruds.create_task(session, task_data)


@router.get('/{task_id}', response_model=TaskResponse)
def get_task_by_id(task_id: int, session: Session = Depends(get_session)):
    task = cruds.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Not Found ")

    return task


@router.put('/{task_id}', response_model=TaskResponse)
def modify_task(task_id: int, updates: TaskUpdate, session: Session = Depends(get_session)):

    updated_task = cruds.update_task(session, task_id, updates)
    if not updated_task:
        return None
    return updated_task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    target = get_task_by_id(task_id, session)
    if not target:
        raise HTTPException(status_code=404, detail="Task not found")
    cruds.delete_task(session, task_id)
    return


# filteration routes

@router.get('/priority/{priority}', response_model=list[TaskResponse])
def filter_by_priority(priority: TaskPriority, session: Session = Depends(get_session)):
    return cruds.get_by_priority(session, priority)


@router.get('/status/{status}', response_model=list[TaskResponse])
def filter_by_status(status: TaskStatus, session: Session = Depends(get_session)):
    return cruds.get_by_status(session, status)


@router.post("/group", response_model=list[TaskResponse], status_code=201)
def create_many(task_list: list[TaskCreate], session: Session = Depends(get_session)):
    return cruds.create_many_tasks(session, task_list)
