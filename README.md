# Travel Planner API

## Install for Local Development

Ensure the following are installed:

- Git (git --version)  
- Docker (docker --version)  

Steps to set up the project:

1. Clone the repository  
2. Configure the .env file  
3. Build the Docker image  
4. Start the project  
5. Load data from the external API  
6. Access development tools  

---

## Clone Repository

Run the following commands:

git clone https://github.com/vladyslav-mishchenko/travel-planner.git  
cd travel-planner

---

## Configure .env

Set up the environment variables:

mv .env.example .env

- Generate a Django SECRET_KEY  
- Add superuser credentials: username, email, password  

---

## Build Docker Image

1. Make sure the scripts are executable:

chmod +x scripts/build.sh  
chmod +x scripts/up.sh  
chmod +x scripts/down.sh  

2. Build and run the project:

cd scripts  
./build.sh    # build Docker image  
./up.sh       # start project  
./down.sh     # stop project  

---

## Start Project

1. For the first start, uncomment the line in entrypoint.sh to create a superuser:

python manage.py createsuperuser --noinput  

2. After creating the superuser, comment the line again and rebuild the Docker image  

---

## Load Data from External API

Run the custom Django command inside the Docker container:

1. List running containers:

docker container ls  

2. Enter the container:

docker exec -it container-id bash  

3. Run the data loading command:

python manage.py load_places  

---

## Development

Access the Swagger documentation after logging in to the admin dashboard:

http://localhost:8000/api/docs/swagger/
