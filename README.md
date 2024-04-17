## Клонируйте репозиторий
git clone git@github.com:First-team-hack/backend_1.git
## Для запуска проекта:<br />
в корневой папке выполнить в терминале:<br />
  docker build -t backend .<br />
  docker run --name taski_backend_container --rm -p 8000:8000 backend<br />
API доступен на http://127.0.0.1:8000<br />
