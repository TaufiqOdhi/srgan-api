import random
import numpy as np
import os
import threading
from test_srgan import client, base_dir, worker_list
from dwo_cp import get_solution_matrix

srgan_endpoint_list = ['/no_prune', '/random_unstructured', '/l1_norm', '/l2_norm']
filename_list = ['1', '2', '3', '4', '5', '6']
prune_amount_list = [30, 50, 70]
phi = 1.61803398875


def _worker_function(srgan_endpoint, filename, prune_amount, node_worker):
    res = client.post(
        srgan_endpoint,
        data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker),
        files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
    )
    assert res.status_code == 200


# menggantikan vm dengan tipe model
def test_dwo_cp_1():
    list_s = get_solution_matrix(n=5, m=4, c=3, num_agent=5)

    list_eva_pm = []
    for s in list_s:
        list_eva_pm.append(len(np.unique(s[1])))

    # find optimal solution
    opt_eva = np.min(list_eva_pm)
    index_opt_eva = list_eva_pm.index(opt_eva)
    s_opt = list_s[index_opt_eva]

    random_s = s_opt
    # random_s = random.choice(list_s)
    print(random_s)

    threads = []
    for index in range(len(random_s[0])):
        filename = random.choice(filename_list)
        prune_amount = random.choice(prune_amount_list)
        srgan_endpoint = srgan_endpoint_list[int(random_s[0][index]-1)]
        node_worker, curr_docker_context = worker_list[int(random_s[1][index])-1]
        os.system(f'docker context use {curr_docker_context}')

        print(srgan_endpoint)
        thread = threading.Thread(target=_worker_function, args=(
            srgan_endpoint,
            filename,
            prune_amount,
            node_worker  
        ))
        threads.append(thread)
        thread.start()

        # res = client.post(
        #     srgan_enpoint,
        #     data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker),
        #     files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
        # )
        # assert res.status_code == 200

    for thread in threads:
        thread.join()
