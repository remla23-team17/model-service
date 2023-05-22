# Dockerfile for model-service
FROM python:3.9

LABEL "maintainer"="remla23-team17"

USER root

ENV EXPOSE_PORT=80

EXPOSE $EXPOSE_PORT

WORKDIR /root

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY models ./models
COPY pipeline ./pipeline
COPY webservice.py .

# Launch web service
ENTRYPOINT ["python"]
CMD ["webservice.py"]
