from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from dinneratmine.data.base_class import Base


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=False)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    user_id = Column(String(10), ForeignKey("user.id"), nullable=True)
    user = relationship("User", back_populates="recipes")