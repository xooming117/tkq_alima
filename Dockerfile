FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tkq/alima
COPY ./requirements.txt /opt/tkq/alima/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tkq/alima

#ENTRYPOINT ["sh", "start.sh"]


#ENTRYPOINT ["python", "main.py"]
#ENTRYPOINT ["python", "main.py"]
#CMD ["sh", "start.sh", "&&", "python", "main.py"]
#CMD ["python", "main.py"]
