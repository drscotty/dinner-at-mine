from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates

from typing import Optional, Any
from pathlib import Path

from schemas.recipe import RecipeSearchResults, Recipe, RecipeCreate
from data.recipe_data import RECIPES


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

#UpBRkTu@RGc4BdP

app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """
    
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "recipes": RECIPES},
    )


@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )

    return result[0]


# 2 new addition, query parameter
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults) 
def search_recipes(
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
    max_results: Optional[int] = 10  
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]} 

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES) 
    return {"results": list(results)[:max_results]}


@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:  # 2
    """
    Create a new recipe (in memory only)
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.model_dump())  # 3

    return recipe_entry


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
    