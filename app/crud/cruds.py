from sqlmodel import Session , select
from typing import Optional
from app.models.taskmodel import Task
from app.schemas.taskschema import TaskCreate  , TaskUpdate
from fastapi import HTTPException
from datetime import datetime
def create_task(session:Session,task_data:TaskCreate) -> Task:
    task = Task.from_orm(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_task (session:Session,task_id:int)-> Task:
    return session.get(Task,task_id)

def get_all_tasks(session: Session,skip:int=0,limit:int=10)-> list[Task]:
    return session.query(Task).offset(skip).limit(limit).all()

    
def update_task(session: Session, task_id: int, updates: TaskUpdate) -> Optional[Task]:
    task = session.get(Task, task_id)
    if not task:
        return HTTPException(status_code=404, detail="Task not found")

    task_data = updates.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.now()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


# adding more than one item
def create_many_tasks(session: Session, task_list: list[TaskCreate]) -> list[Task]:
    tasks = [Task.from_orm(task_data) for task_data in task_list]
    session.add_all(tasks)
    session.commit()
    for task in tasks:
        session.refresh(task)
    return tasks




def delete_task(session: Session, task_id: int) -> bool:
    task = session.get(Task, task_id)
    if not task:
        return False
    session.delete(task)
    session.commit()
    return True




def get_by_status(session: Session,status: str)-> list[Task]:
    sql_statement = select(Task).where(Task.status == status)
    runner = session.exec(sql_statement).all()
    return runner


def get_by_priority(session: Session, priority: str) -> list[Task]:
    sql_statement = select(Task).where(Task.priority == priority)
    runner = session.exec(sql_statement).all()
    return runner  



