FROM python:slim-bookworm

COPY . /usr/app/

WORKDIR /usr/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]
