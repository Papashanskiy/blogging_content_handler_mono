from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), order: int = 0, publish_time: str = None):
    # Обработка загрузки файла и сохранение информации о посте
    # в базе данных или другом хранилище
    return {"filename": file.filename, "order": order, "publish_time": publish_time}
