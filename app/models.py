from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import metadata


catering_orders = Table(
    "catering_orders", metadata,
    Column("id", Integer, primary_key=True),
    Column("event_date", Date),
    Column("order_status", String(50)),
)

staff_schedules = Table(
    "staff_schedules", metadata,
    Column("id", Integer, primary_key=True),
    Column("event_date", Date),
    Column("status", String(50)),
    Column("assigned_event_id", Integer, ForeignKey("event_plans.id")),
)

event_plans = Table(
    "event_plans", metadata,
    Column("id", Integer, primary_key=True),
    Column("event_date", Date),
    Column("event_status", String(50)),
)
