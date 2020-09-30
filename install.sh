docker build -t myimage .
#docker run -d --name mycontainer -p 80:80 myimage
docker run -it --name mycontainer -p 80:80 myimage
# web: uvicorn fastapp:app --host 0.0.0.0 --port 80