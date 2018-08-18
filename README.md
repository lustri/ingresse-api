# Ingresse Backend Devloper test

## Set up

### Install docker and docker compose

- Windows
  
  Install DockerToolbox
  
- Linux
  
  Install docker and docker compose

### Clone app

 - Need to have git installed on your computer
  
  `git clone https://github.com/lustri/ingresse-api.git`

## Run 

   `cd ingresse-api`
   
   `docker-compose build`
   
   `docker-compose up -d`
 
 - You need to restart the app container after postgres set up
     
  `docker restart app`
     
## Run tests
     
 - Need to have all container up
     
  `docker-compose run app python manage.py test`
