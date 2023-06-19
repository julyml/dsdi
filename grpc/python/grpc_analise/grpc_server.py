# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import time


import grpc
import grpc_analise_pb2
import grpc_analise_pb2_grpc



class Mensageiro(grpc_analise_pb2_grpc.MensageiroServicer):

  def EnviarMensagemVazia(self, request, context):
    start_time = time.time()
    duration = time.time() - start_time
    print(f"A operação levou {duration:.2f} segundos para ser concluída")
    return grpc_analise_pb2.Resposta_Request_Void()
  
  def EnviarMensagemLong(self, request, context):
    start_time = time.time()
    duration = time.time() - start_time
    print(f"A operação levou {duration:.2f} segundos para ser concluída")
    return grpc_analise_pb2.Resposta_Request_Long()
  
  def EnviarMensagemOitoLong(self, request, context):
    start_time = time.time()
    duration =  time.time() - start_time
    print(f"A operação levou {duration:.2f} segundos para ser concluída")
    return grpc_analise_pb2.Resposta_Request_Long()
  
  def EnviarMensagemString(self, request, context):
    start_time = time.time()
    duration = time.time() - start_time
    print(f"A operação levou {duration:.2f} segundos para ser concluída")
    return grpc_analise_pb2.Resposta_Request_String()


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_analise_pb2_grpc.add_MensageiroServicer_to_server(Mensageiro(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


# 1. tempo para chamada de uma operação sem argumentos e sem valor de
# retorno (void)
# 2. tempo para chamada de uma operação com um argumento long e valor
# de retorno long
# 3. tempo para chamada de uma operação com oito argumentos long e valor
# de retorno long
# 4. tempo para chamada de uma operação com um argumento String e va-
# lor de retorno String, para strings com diferentes tamanhos (sugere-se
# testes com potências de 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, …)
# 5. tempo para chamada de uma operação com um argumento e um valor de
# retorno de um tipo complexo (ex: uma classe definida por vocês)