from app.models import catering_orders, staff_schedules, event_plans
from app.database import database
from sqlalchemy.sql import func

# Catering Orders
async def get_all_orders():
    query = catering_orders.select()
    return await database.fetch_all(query)

async def update_order_status(order_id: int, new_status: str):
    query = catering_orders.update().where(catering_orders.c.id == order_id).values(order_status=new_status)
    await database.execute(query)

# Staff Schedules
async def get_all_schedules():
    query = staff_schedules.select()
    return await database.fetch_all(query)

async def update_schedule_status(schedule_id: int, new_status: str):
    query = staff_schedules.update().where(staff_schedules.c.id == schedule_id).values(status=new_status)
    await database.execute(query)

# Event Plans
async def get_all_events():
    query = event_plans.select()
    return await database.fetch_all(query)

async def update_event_status(event_id: int, new_status: str):
    query = event_plans.update().where(event_plans.c.id == event_id).values(event_status=new_status)
    await database.execute(query)
