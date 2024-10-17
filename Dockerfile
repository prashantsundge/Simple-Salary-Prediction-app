# use pythyon runtime as base image
FROM python:3.9-slim

#set working directory in the container 
WORKDIR / GCP_PROJECT 02 SALARY_DOCKER

# copy the requirements.txt and app files to the container 
COPY requirements.txt .
# we will create seperate requirements.txt as previous we directly installed the modules 

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the files 
COPY . .
# Expose the port on which the app will run 
EXPOSE 5000

#set the command to run  the flask app
CMD ["python" , "app.py"]
