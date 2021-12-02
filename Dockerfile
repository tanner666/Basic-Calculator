# FROM python:3.9-alpine
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip install --upgrade pip setuptools wheel
# RUN apk add build-base
# RUN adduser -D myuser
# RUN apk add --no-cache gcc musl-dev linux-headers
# USER myuser
# WORKDIR /home/myuser
# ENV PATH="/home/myuser/.local/bin:${PATH}"
# COPY --chown=myuser:myuser . .
# RUN pip install --user -r requirements.txt
FROM python:3.8-buster
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN apt-get update
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY CSV_Files/CSV_InputFiles/* ./
COPY CSV_Files/Results/* ./
COPY CSV_Files/CSV_CompletedFiles ./
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
# CMD ["uwsgi", "app/app.ini"]
