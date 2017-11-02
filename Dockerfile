FROM markadams/chromium-xvfb-py2
WORKDIR /opt/tbk/chrome
COPY ./requirements.txt /opt/tbk/chrome/requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY :1
COPY . /opt/tbk/chrome
CMD ["sh", "start.sh", "&&", "python", "main.py"]
#CMD ["python", "main.py"]
