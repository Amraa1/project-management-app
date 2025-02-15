from .time_stamped_model import TimeStampedModel
from sqlalchemy import Column, Integer, String


class Category(TimeStampedModel):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
