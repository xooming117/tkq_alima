FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tkq/chrome
COPY ./requirements.txt /opt/tkq/chrome/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tkq/chrome

#ENTRYPOINT ["sh", "start.sh"]


#ENTRYPOINT ["python", "main.py"]
#ENTRYPOINT ["python", "main.py"]
#CMD ["sh", "start.sh", "&&", "python", "main.py"]
#CMD ["python", "main.py"]
