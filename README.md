# bokeh

### Build backend:

```
Require : Ubuntu 22.04
cd backend_cpp/libwebsockets
cmake .
make
sudo make install
```

###

```
Server code:
cd backend_cpp/cppWebSockets
g++ -w -DLOG_TO_STDOUT=1 -omyserver server.c -lwebsockets
After build success,Run server with command:
./myserver
```

### Build frontend

```
Modify :frontend_bokeh\myapp\templates\index.html
var socket = new WebSocket( "ws://192.168.200.131:8000", "example-protocol" );
to:
var socket = new WebSocket( "ws://Your_server_ip:8000", "example-protocol" );
Run frontend:
pip install bokeh==3.0.0.dev2
After install success,Go to frontend_bokeh,And run command:
bokeh serve --show myapp
```


