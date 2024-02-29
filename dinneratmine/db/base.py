# Import all the models, so that Base has them before being
# imported by Alembic
from dinneratmine.db.base_class import Base 
from dinneratmine.models.user import User 
from dinneratmine.models.recipe import Recipe 