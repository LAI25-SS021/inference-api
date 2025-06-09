FROM python:3.12.3

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

ENV HOST 0.0.0.0

EXPOSE 8000

CMD ["fastapi", "run", "app.py", "--port", "8000"]