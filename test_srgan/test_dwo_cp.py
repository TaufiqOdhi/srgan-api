import random
import os
from test_srgan import client, base_dir
from dwo_cp import get_solution_matrix

srgan_enpoint_list = ['/no_prune', '/random_unstructured', '/l1_norm', '/l2_norm']
filename_list = ['1', '2', '3', '4', '5', '6']
prune_amount_list = [30, 50, 70]
worker_list = [('10.21.87.149', 'default'), ('10.21.87.160', 'ncc-pc-3')]
phi = 1.61803398875


# menggantikan vm dengan tipe model
def test_dwo_cp_1():
    list_s = get_solution_matrix(n=2, m=4, c=2, num_agent=5)
    random_s = random.choice(list_s)
    print(random_s)

    for index in range(len(random_s[0])):
        filename = random.choice(filename_list)
        prune_amount = random.choice(prune_amount_list)
        srgan_enpoint = srgan_enpoint_list[int(random_s[0][index]-1)]
        node_worker, curr_docker_context = worker_list[int(random_s[1][index])-1]
        os.system(f'docker context use {curr_docker_context}')

        print(srgan_enpoint)

        res = client.post(
            srgan_enpoint,
            data=dict(filename=filename, prune_amount=prune_amount, node_worker=node_worker),
            files=dict(image=open(f'{base_dir}/{filename}.png', 'rb'))
        )
        assert res.status_code == 200
