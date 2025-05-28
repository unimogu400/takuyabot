FROM python:3.13
WORKDIR /bot
COPY requirements.txt /bot
RUN pip install -r requirements.txt
EXPOSE 8880
COPY . /bot
CMD python takuya.py
