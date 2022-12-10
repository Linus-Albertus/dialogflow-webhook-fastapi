FROM python:3.11

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the scripts to the folder
COPY ./app /code/app

# start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]