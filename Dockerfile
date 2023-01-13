FROM python:3.10
VOLUME /helper
COPY . /helper
WORKDIR .
RUN pip install helper/.
RUN pip install -r helper/requirments.txt
CMD ["bash"]
