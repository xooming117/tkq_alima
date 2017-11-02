FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tbk/chrome
COPY ./requirements.txt /opt/tbk/chrome/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tbk/chrome

ENTRYPOINT ["sh", "start.sh"]
ENTRYPOINT ["python", "main.py"]
#CMD ["sh", "start.sh", "&&", "python", "main.py"]
#CMD ["python", "main.py"]
