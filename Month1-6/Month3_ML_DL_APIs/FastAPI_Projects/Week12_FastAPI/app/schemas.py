from pydantic import BaseModel ,Field ,validator  
from typing import Union

class IrisInput(BaseModel):
    sepal_length : Union[float, int] = Field(...,gt = 0, lt = 10 ,description = "Sepal Length in cm")
    sepal_width : Union[float, int] = Field(...,gt = 0, lt = 10 ,description = "Sepal Width in cm")
    petal_length : Union[float, int] = Field(...,gt = 0, lt = 10 ,description = "Petal Length in cm")
    petal_width : Union[float, int] = Field(...,gt = 0, lt = 10 ,description = "Sepal Width in cm")

    @validator("*")
    def check_float(cls,v):
        if not isinstance(v,(float,int)):
            raise ValueError("Value must be numerical")
        return v