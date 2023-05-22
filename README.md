# model-service

## Install the python requirements
```bash
python3 -m pip install -r requirements.txt
```

## Run the webservice locally
```bash
python3 webservice.py
```

## Run the webservice with Docker
```bash
docker buildx build . -t model-service
```
```bash
docker run -it -p <PORT>:80 model-service
```

## Test the webservice with Curl
```bash
curl -X POST http://localhost:<PORT>/predict -H "Content-Type: application/json" -d '{"input": "The selection on the menu was great and so were the prices."}' 
```
