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
@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task_data: TaskCreate, session: Session = Depends(get_session)):

    return cruds.create_task(session, task_data)


@router.get("/", response_model=list[TaskResponse])
def get_list_of_tasks(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return cruds.get_all_tasks(session, skip=skip, limit=limit)


@router.get('/{task_id}', response_model=TaskResponse)
def get_task_by_id(task_id: int, session: Session = Depends(get_session)):
    task = cruds.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Not Found ")

    return task


@router.put('/{task_id}',response_model=TaskResponse)
def modify_task(task_id: int,updates=TaskUpdate,session: Session=Depends(get_session)):
    
    updated_task = cruds.update_task(session,task_id,updates)
    if not updated_task :
        raise HTTPException(status_code=404,detail="Not Found")
    return updated_task


@router.delete("/{task_id}",response_model=TaskResponse)
def delete_task(task_id: int,session: Session=Depends(get_session)):
   target = get_task_by_id(task_id,session)
   name_of_target = target.title
   success = cruds.delete_task(session,task_id)
    
   if not success:
        raise HTTPException(status_code=404,detail="task not found")
   return name_of_target
    


# filteration routes

@router.get('/priority/{priority}',response_model=list[TaskResponse])
def filter_by_priority(priority: TaskPriority,session: Session=Depends(get_session)):
    return cruds.get_by_priority(session,priority)

@router.get('/status/{status}',response_model=list[TaskResponse])
def filter_by_priority(status: TaskStatus,session: Session=Depends(get_session)):
    return cruds.get_by_priority(session,status)