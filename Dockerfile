FROM python:3.11.2

ENV APP_HOME /__main__

WORKDIR $APP_HOME

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "__main__.py"]
