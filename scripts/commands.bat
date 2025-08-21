docker login
docker build -t hostile-tweets:1.0 .
docker run -d -p 8000:8000 hostile-tweets:1.0

docker tag hostile-tweets yosigu/hostile-tweets:1.0
docker push yosigu/hostile-tweets:1.0 