from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Cooperative(Base):
    tablename = "cooperatives"
    id = Column(Integer, primary_key=True, index=True)  
    region = Column(String)  
    authorized_capital = Column(Float)  
    
    memberships = relationship("Membership", back_populates="cooperative")

class Owner(Base):   
   tablename = "owners"
  
  id = Column(Integer, primary_key=True, index=True)  
    full_name = Column(String, index=True)  
    passport_data = Column(String)  
    
    memberships = relationship("Membership", back_populates="owner")

class Membership(Base):   
   tablename = "memberships"
  
  id = Column(Integer, primary_key=True, index=True)  
    cooperative_id = Column(Integer, ForeignKey("cooperatives.id"))  
    share_size = Column(Float)  
    
    cooperative = relationship("Cooperative", back_populates="memberships") 
    owner = relationship("Owner", back_populates="memberships")
