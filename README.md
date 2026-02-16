# Trevel Planner API
## Install for local development

Ensure you have the following installed
git --version
docker --version

1. clone repository
2. setting .env
3. build Docker image
4. start project
5. development

## Clone repository
https://github.com/vladyslav-mishchenko/travel-planner.git

## Setting .env
1. mv .env.example .env
2. generate Django SECRET_KEY
3. add superuser, email, password

## Build Docker image
1. Make sure the scripts are executable
   build.sh up.sh down.sh must be executable
   if not:
   chmod +x build.sh
   chmod +x up.sh
   chmod +x down.sh
2. cd scripts
   ./build.sh - build image
   ./up.sh - start project
   ./down.sh - stop project

## Start project
1. For the first start, uncomment the line to create a superuser 
   python "manage.py" createsuperuser --noinput
2. After creating the superuser, comment the line again and rebuild the Docker image

## Development
1. Access Swagger docs after logging in to the admin dashboard
- login to admin dashboard first
- http://localhost:8000/api/docs/swagger/
