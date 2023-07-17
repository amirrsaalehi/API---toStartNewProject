from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any, List, Optional
from api import deps
from sqlalchemy.orm import Session
from core import security
import schemas, crud
from datetime import datetime, timedelta
from core.config import settings
import json

router = APIRouter()

@router.post("/sum")# , response_model=schemas.Calc1)
async def sum( input1: schemas.Calc1,   request: Request
) -> Any:
    """
    calculator.
    """
    if input1.op=="+":
        res = input1.num1 + input1.num2
    elif input1.op=="*":
        res = input1.num1 * input1.num2
    elif input1.op=="-":
        res = input1.num1 - input1.num2
    elif input1.op=="/":
        res = input1.num1 / input1.num2   
    elif input1.op=="^":
        res = input1.num1 ** input1.num2
    else:
        return "عملگر درست را وارد نمایید"      
    # x= schemas.calc.Calc1
    # x.num1=1
    # x.num2=2
    # x.op="dd"  
    # print(x)       
    return {"result " : res , "status_code":200  }#json.load(**x)#{"op":"aa" ,"num2":200  }