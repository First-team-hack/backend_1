# backend_1
Для запуска проекта:
в корневой папке выполнить в терминале:
  docker build -t backend .
  docker run --name taski_backend_container --rm -p 8000:8000 backend
API доступен на http://127.0.0.1:8000
