from xmlrpc.server import SimpleXMLRPCServer

def EnviarMensagemVazia():
    return None

def EnviarMensagemLong(n):
    return n*n

def EnviarMensagemOitoLong(n):
    return  n*n

def EnviarMensagemString(n):
    return '6889'*n

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(EnviarMensagemVazia, "EnviarMensagemVazia")
server.register_function(EnviarMensagemLong, "EnviarMensagemLong")
server.register_function(EnviarMensagemOitoLong, "EnviarMensagemOitoLong")
server.register_function(EnviarMensagemString, "EnviarMensagemString")
server.serve_forever()