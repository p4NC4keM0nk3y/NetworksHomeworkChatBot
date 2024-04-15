# Chat Message Server
This application is a server used by those who wish to communicate directly to other hosts using their IP address and Port Number. 

## Installation

Clone this [repo](doc:https://github.com/p4NC4keM0nk3y/NetworksHomeworkChatBot.git)

Install socket through terminal

```bash
pip install socket
```

## Usage

```python
# initializes server
python server2.py

# Intitializes client
python client2.py

```
## Instructions
When creating server2, the IP address and port number will be prompted, with the default being 192.168.0.1 and 8080
When running client2, the username and port number will be prompted to establish a connection.
### Connection is established
Once a connection is established, the user and server can communicate back and forth until the client types end. The process will then be killed. 


## License
[MIT](https://choosealicense.com/licenses/mit/)
