from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.schemas.auth import LoginOut
from src.services.auth import AuthService

router = APIRouter(tags=["auth"])

@router.post("/login", response_model=LoginOut)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    service = AuthService()
    user = await service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorret username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = service.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}