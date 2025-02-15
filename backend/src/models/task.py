from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime
from .time_stamped_model import TimeStampedModel


class Task(TimeStampedModel):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bucket_id = Column(Integer, ForeignKey("bucket.id"), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    completed = Column(Boolean, nullable=False, default=False)

    start_at = Column(DateTime, nullable=True)
    end_at = Column(DateTime, nullable=True)

    