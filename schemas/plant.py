from pydantic import BaseModel


class PlantCreate(BaseModel):
    pass


class PlantUpdate(BaseModel):
    pass


class PlantResponse(BaseModel):
    model_config = {"from_attributes": True}
