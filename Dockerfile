# Use Python 3.9 image
FROM python:3.9

# Define work dir
WORKDIR /root

# Copy necessary files to work dir
COPY requirements.txt .
COPY models ./models
COPY pipeline ./pipeline
COPY webservice.py .

# Install python dependencies
RUN pip install -r requirements.txt

# Expose port to outside world
EXPOSE 8080

# Launch web service
ENTRYPOINT ["python"]
CMD ["webservice.py"]
