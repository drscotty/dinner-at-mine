from dinneratmine.data.crud.base import CRUDBase
from dinneratmine.models.recipe import Recipe
from dinneratmine.schemas.recipe import RecipeCreate, RecipeUpdate


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    ...


recipe = CRUDRecipe(Recipe)