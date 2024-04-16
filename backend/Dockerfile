FROM python:latest
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "manage.py", "runserver", "0:8000"]