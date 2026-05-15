"""
Waitress WSGI 服务器入口 (Windows 生产环境)
用 NSSM 注册为 Windows 服务实现开机自启
"""
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from waitress import serve
from config.wsgi import application

HOST = os.getenv("SERVER_HOST", "127.0.0.1")
PORT = int(os.getenv("SERVER_PORT", "8080"))

if __name__ == "__main__":
    print(f"Waitress serving on http://{HOST}:{PORT}")
    serve(application, host=HOST, port=PORT, threads=8)
