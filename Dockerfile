FROM python:3.10-slim

# setting work directory to not use root as specified in the streamlit docs
WORKDIR /app

# install git to allow for cloning of remote repo
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# copy the files into the docker container
COPY . .

# install python dependencies
RUN pip3 install -r requirements.txt

# open port 8501 to listen for streamlit
EXPOSE 8501

# set a healthcheck to tell docker how to test a container that its still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# entrypoint allows you to configure a container to run as an executable
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=localhost"]


