FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
ADD . /sre-app

WORKDIR /sre-app

RUN pip3 install -r requirements.txt

ENV PORT=8000

EXPOSE 8000

CMD [ "python3", "api.py"]