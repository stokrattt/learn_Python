FROM ubuntu:latest

RUN apt-get update
RUN apt-get update && apt-get install -y apt-transport-https

RUN apt-get install -y python-pip build-essential
RUN pip install --upgrade pip
RUN pip install pytest
RUN pip install pytest-xdist
RUN pip install selenium
COPY . /test
WORKDIR /test 
RUN pip install -r requirements.txt
ENTRYPOINT ['python']






# overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["/bin/bash"]
