from sqlmodel import Session , select
from typing import Optional
from app.models.taskmodel import Task
from app.schemas.taskschema import TaskCreate  , TaskUpdate

from datetime import datetime
def create_task(session:Session,task_data:TaskCreate) -> Task:
    task = Task.from_orm(task_data)
    session.add(task)
    session.commit()
    session.refresh()
    return task


def get_task (session:Session,task_id:int)-> Task:
    return session.get(Task,task_id)

def get_all_tasks(session: Session,skip:int=0,limit:int=10)-> list[Task]:
    return session.query(Task).offset(skip).limit(limit).all()

    
def update_task(session: Session, task_id: int, updates: TaskUpdate) -> Optional[Task]:
    task = session.get(Task, task_id)
    if not task:
        return None

    task_data = updates.dict(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task



def delete_task(session: Session,task_id:int)->bool:
    task = Session.get(Task,task_id)
    if not task :
        return False
    session.delete(task)
    session.commit()
    return True


def get_by_status(session: Session,status: str)-> list[Task]:
    return session.query(select(Task).where(Task.status==status).all())

def get_by_priority(session:Session,priority: str):
    return session.query(select(Task).where(Task.priority==priority)).all()
