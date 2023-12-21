FROM ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
RUN chmod +x try.py
CMD ["python3", "try.py"]
