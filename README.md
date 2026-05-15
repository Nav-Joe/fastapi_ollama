# AI Chat Service

基于 FastAPI 的 AI 对话服务，本地大模型（Ollama）私有化部署。

## 技术栈

- Python + FastAPI
- Docker
- Ollama（本地大模型部署）
- Linux

## 功能特性

- REST API 接口（POST /chat）
- 支持 Ollama 本地模型离线运行
- Docker 一键部署
- 自动异常处理与日志记录

## 快速开始
## 1.下载ollama并拉取下载模型（以qwen2.5:3b为例）
ollama pull qwen2.5:3b

## 2.docker化部署：
- docker build -t ai_service .
- docker run -p 8000:8000 -e OLLAMA_HOST=http://host.docker.internal:11434 ai-service
