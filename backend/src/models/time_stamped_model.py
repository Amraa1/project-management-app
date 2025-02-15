from database import Base
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone, timedelta


class TimeStampedModel(Base):
    __abstract__ = True

    created_at = Column(
        DateTime,
        default=datetime.now(timezone(offset=timedelta(hours=8), name="Ulaanbaatar")),
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone(offset=timedelta(hours=8), name="Ulaanbaatar")),
        onupdate=datetime.now(timezone(offset=timedelta(hours=8), name="Ulaanbaatar")),
    )
