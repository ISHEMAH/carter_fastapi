from pydantic import BaseModel
from datetime import date

class CateringOrder(BaseModel):
    id: int
    event_date: date
    order_status: str

    class Config:
        orm_mode = True

class StaffSchedule(BaseModel):
    id: int
    event_date: date
    status: str
    assigned_event_id: int

    class Config:
        orm_mode = True

class EventPlan(BaseModel):
    id: int
    event_date: date
    event_status: str

    class Config:
        orm_mode = True
