import xmlrpc.client
import time
import pandas as pd

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    duration_list = list()
    for x in range(10):
        start_time = time.time()
        proxy.EnviarMensagemVazia()
        duration = time.time() - start_time
        print(f"A operação levou {duration} segundos para ser concluída")
        duration_list.append({'experimento':'void', 'duracao':duration})

        start_time = time.time()
        proxy.EnviarMensagemLong(6889)
        duration = time.time() - start_time
        print(f"A operação levou {duration} segundos para ser concluída")
        duration_list.append({'experimento':'long', 'duracao':duration})

        start_time = time.time()
        proxy.EnviarMensagemOitoLong(600)
        duration = time.time() - start_time
        print(f"A operação levou {duration} segundos para ser concluída")
        duration_list.append({'experimento':'oito_long', 'duracao':duration})

        start_time = time.time()
        proxy.EnviarMensagemString(6889)
        duration = time.time() - start_time
        print(f"A operação levou {duration} segundos para ser concluída")
        duration_list.append({'experimento':'string', 'duracao':duration})
    
    pd.DataFrame(duration_list).to_csv('analise_xml_rpc.csv')
    
    
    