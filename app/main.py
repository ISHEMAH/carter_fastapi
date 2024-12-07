from fastapi import FastAPI, HTTPException
from app import crud, database
from app.schemas import CateringOrder, StaffSchedule, EventPlan

app = FastAPI()

# Connect to the database
@app.on_event("startup")
async def startup():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

# Orders
@app.get("/orders/", response_model=list[CateringOrder])
async def get_orders():
    return await crud.get_all_orders()

@app.post("/orders/{order_id}/status/")
async def update_order_status(order_id: int, new_status: str):
    await crud.update_order_status(order_id, new_status)
    return {"status": "success"}

# Schedules
@app.get("/schedules/", response_model=list[StaffSchedule])
async def get_schedules():
    return await crud.get_all_schedules()

@app.post("/schedules/{schedule_id}/status/")
async def update_schedule_status(schedule_id: int, new_status: str):
    await crud.update_schedule_status(schedule_id, new_status)
    return {"status": "success"}

# Events
@app.get("/events/", response_model=list[EventPlan])
async def get_events():
    return await crud.get_all_events()

@app.post("/events/{event_id}/status/")
async def update_event_status(event_id: int, new_status: str):
    await crud.update_event_status(event_id, new_status)
    return {"status": "success"}
