# filesbang
bang your files for analysis via API interface
# system environment(theoretically supports arm release version)
Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-205-generic x86_64)
# pre-environment java
sudo apt install openjdk-11-jdk
# pre-environment python
pip install python-multipart fastapi tika uvicorn
# run
uvicorn app:app --reload
# run in background
nohup uvicorn app:app > output.log 2>&1 &
