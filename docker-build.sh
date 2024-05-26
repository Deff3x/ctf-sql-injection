docker stop ctf
docker rm ctf
docker rmi ctf

docker build . -t ctf --no-cache
docker run -p 9374:9374 --rm -it --name ctf ctf