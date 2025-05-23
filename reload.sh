
docker stop web-socket

docker rm web-socket

docker rmi web-socket-image


git pull


docker build -t web-socket-image .

docker run -d --name web-socket -p 80:8000 web-socket-image
