FROM python:3.12-slim
LABEL authors="max"
WORKDIR /fastapi
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --disable-pip-version-check  \
    --progress-bar=off -r requirements.txt
COPY ./app /fastapi/app
EXPOSE 8000
ENV URL=sqlite:///database.db
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0"]