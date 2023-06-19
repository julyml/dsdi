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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
import time
import pandas as pd

import grpc
import grpc_analise_pb2
import grpc_analise_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_analise_pb2_grpc.MensageiroStub(channel)
        duration_list = list()
        for x in range(10):
            start_time = time.time()
            response = stub.EnviarMensagemVazia(grpc_analise_pb2.Resposta_Request_Void())
            duration = time.time() - start_time
            print(f"A operação levou {duration} segundos para ser concluída")
            duration_list.append({'experimento':'void', 'duracao':duration})


            start_time = time.time()
            response = stub.EnviarMensagemLong(grpc_analise_pb2.Resposta_Request_Long(message=6889*6889))
            duration = time.time() - start_time
            print(f"A operação levou {duration} segundos para ser concluída")
            duration_list.append({'experimento':'long', 'duracao':duration})

            start_time = time.time()
            response = stub.EnviarMensagemOitoLong(grpc_analise_pb2.Resposta_Request_Long(message=6889*6889))
            duration = time.time() - start_time
            print(f"A operação levou {duration} segundos para ser concluída")
            duration_list.append({'experimento':'oito_long', 'duracao':duration})
            
            start_time = time.time()
            response = stub.EnviarMensagemString(grpc_analise_pb2.Resposta_Request_String(message='6889'*6889))
            duration = time.time() - start_time
            print(f"A operação levou {duration} segundos para ser concluída")
            duration_list.append({'experimento':'string', 'duracao':duration})
        
        pd.DataFrame(duration_list).to_csv('analise_grpc.csv',index=False)


if __name__ == '__main__':
    logging.basicConfig()
    run()
