from pydantic import BaseModel
from typing import Optional

class CooperativeBase(BaseModel):   
    name: str 
    location_area: Optional[str] = None    
    employee_count: Optional[int] = None  
    authorized_capital: Optional[float] = None  
    profile: Optional[str] = None  

class CooperativeCreate(CooperativeBase):  
   pass

class Cooperative(CooperativeBase):  
  id: int  


    class Config:
        orm_mode = True

