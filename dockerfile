# 用Python官方镜像
FROM python:3.10-slim

# 工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制你的代码
COPY services.py .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "services:app", "--host", "0.0.0.0", "--port", "8000"]