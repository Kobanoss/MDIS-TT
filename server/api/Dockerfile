# # # # #
# BUILD #
# # # # #
FROM python:3.10.7-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc


RUN pip install --upgrade pip
RUN pip install flake8==5.0.4
COPY . /usr/src/app/
RUN flake8 --extend-ignore E501,E402,F405,F403,F401 .


COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# # # # #
# SETUP #
# # # # #
FROM python:3.10.7-slim-buster


RUN mkdir -p /home/app


RUN addgroup --system app && adduser --system --group app


ENV HOME=/home/app
ENV APP_HOME=/home/app/application
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN apt install gunicorn -y
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/application/entrypoint.sh"]