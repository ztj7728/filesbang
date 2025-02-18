from fastapi import FastAPI, File, UploadFile
from tika import parser
from fastapi.responses import JSONResponse
import os

# 创建FastAPI应用
app = FastAPI()

# 文件解析API
@app.post("/parse-file/")
async def parse_file(file: UploadFile = File(...)):
    try:
        # 获取文件内容
        contents = await file.read()
        
        # 将文件保存为临时文件
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(contents)
        
        # 使用Apache Tika解析文件
        parsed = parser.from_file(temp_file_path)
        
        # 删除临时文件
        os.remove(temp_file_path)
        
        # 返回解析结果
        return JSONResponse(content={
            "status": "success",
            "file_name": file.filename,
            "content": parsed.get("content", "No content extracted")
        })
    
    except Exception as e:
        return JSONResponse(content={
            "status": "error",
            "message": str(e)
        }, status_code=400)

# 启动应用的命令 (通过 Uvicorn)
# uvicorn app:app --reload
