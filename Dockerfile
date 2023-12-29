FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY . .
RUN pip install -r ./requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/src"

CMD ["python", "./main.py"]