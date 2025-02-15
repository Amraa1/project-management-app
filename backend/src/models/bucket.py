from sqlalchemy import Column, Integer, String, ForeignKey
from .time_stamped_model import TimeStampedModel


class Bucket(TimeStampedModel):
    __tablename__ = "bucket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # rgb color
    # red = Column(Integer, nullable=False)
    # green = Column(Integer, nullable=False)
    # blue = Column(Integer, nullable=False)
