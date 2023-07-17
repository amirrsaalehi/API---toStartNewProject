from pydantic import BaseModel
from typing import Optional
  
class Calc1(BaseModel):
    # def __repr__(self) -> str:
    #     return self.op
    # def __str__(self) -> str:
    #     return self.op
    num1:int
    op:str
    num2:int 
# c=Calc1 