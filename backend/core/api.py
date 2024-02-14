from fastapi import APIRouter, Depends, File, UploadFile

from backend.authorization.auth import User, get_current_user

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), order: int = 0, publish_time: str = None):
    return {"filename": file.filename, "order": order, "publish_time": publish_time}


@router.get('/protected')
async def get_protected_data(current_user: User = Depends(get_current_user)):
    return {'message': 'Hi', 'user': current_user.username}
