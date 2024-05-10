# BASE IMAGE
FROM python:3.10
# Set environment python path

ENV PYTHONPATH ./

# Set work directory
WORKDIR ./

# Add ml application
COPY /src /src
COPY /app.py /app.py
COPY /main.py /main.py
COPY /schema.ymal /schema.ymal


# Add test requirements
COPY test_requirements.txt /test_requirements.txt
COPY test.py /test.py


# upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r test_requirements.txt


CMD ["pytest", "test.py"]