FROM python:3.12
WORKDIR /WORKDIR
COPY ./requirements.txt /WORKDIR/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /WORKDIR/requirements.txt
COPY ./app /WORKDIR/app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]