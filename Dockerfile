FROM python:3.10-slim-buster

ARG USERNAME=app
WORKDIR /app
COPY . /app/

RUN apt update \
    && apt install -y wget \
    && adduser --disabled-password --no-create-home --gecos ${USERNAME} ${USERNAME} \
    && pip install -r requirements.txt

# Disable buffered Python & pycache
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=1

USER ${USERNAME}

CMD ["python", "app.py"]