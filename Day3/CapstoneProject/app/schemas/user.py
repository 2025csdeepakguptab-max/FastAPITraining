#Define the Pydantic models that the FastAPI uses to validate incoming request bodies
#shapes the outgoing response

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole

class UserCreate(BaseModel):
    name:str = Field(...,min_length=2,max_length=100,description="Full name of the user")
    email: EmailStr = Field(...,description="Email address of the user")
    password: str = Field(...,min_length=8,description="Password of the user")
    role: UserRole = Field(default=UserRole.EMPLOYEE,description="one of: employee, support_engineer,team_lead, admin")
    
class UserResponse(BaseModel):
    #shape the user as returned by the API
    _id: str
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    