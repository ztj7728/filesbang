# filesbang
bang your files for analysis via API interface
# system environment in Development(theoretically supports arm release version)
Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-205-generic x86_64)
# pre-environment java
```
sudo apt install openjdk-11-jdk
```

# pre-environment python
```
pip install python-multipart fastapi tika uvicorn
```

# run
```
uvicorn app:app --reload
```

# run in background
```
nohup uvicorn app:app > output.log 2>&1 &
```

# use
```
curl -X 'POST' \
  'http://127.0.0.1:8000/parse-file/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/your_file_path/example.pdf'
```

# feedback
```
{
  "status": "success",
  "file_name": "example.pdf",
  "content": "This is the extracted text content of the uploaded document."
}
```
