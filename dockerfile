#Use an official Python runtime as a parent image
FROM python:3.12-slim

#Set the working directory inside the container
WORKDIR /app

#Copy requirements first caching layer
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy everything from local project into container
COPY . /app

#Expose port 8080
EXPOSE 8080


#COMMAND to run server
CMD ["python","app.py"]