# WebSocket_middleware
Automatically forward HTTP POST requests into a WebSocket.

POST version of Rayhan0x01's script: https://rayhan0x01.github.io/ctf/2021/04/02/blind-sqli-over-websocket-automation.html

## Download
### GNU/Linux
```bash
wget https://raw.githubusercontent.com/Sad-theFaceless/WebSocket_middleware/main/middleware.py && chmod +x middleware.py
```

## Usage
Start the middleware server:
```bash
./middleware.py $DOMAIN $PORT "$URL_PATH"
```
Then send HTTP POST data to `http://127.0.0.1:8081/`

## Example
```bash
./middleware.py ws.example.com 5678 "/"
```
### cURL
```bash
curl -X POST 'http://127.0.0.1:8081/' -d '{"id":"1"}'
```
### sqlmap
```bash
sqlmap --method=POST --skip=User-agent,Referer,Host -u "http://127.0.0.1:8081/" --data '{"id":"1"}'
```
