from .time_stamped_model import TimeStampedModel
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean


class Project(TimeStampedModel):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
