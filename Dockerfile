FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
# CMD ["python","app.py"]
ENTRYPOINT ["./gunicorn_start.sh"]