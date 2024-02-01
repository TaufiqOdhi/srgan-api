import random
import math
import numpy as np


def get_solution_matrix(
    n = 3, # number of pm
    m = 5, # number of vm
    c = 10, # number of container
    num_agent = 5 # number of whale agent    
):
    
    list_n = [x+1 for x in range(n)]
    list_m = [x+1 for x in range(m)]
    phi = 1.61803398875

    list_s = []
    list_s_index = []
    for i in range(num_agent):
        list_s_index.append(i)
        list_s.append(np.array([
            [random.randint(1, m) for _ in range(c)],
            [random.randint(1, n) for _ in range(c)]
        ]))

    # Generate solution matrixs (s1, s2, ...., sn)
    for s in list_s:
        vm, pm = s
        for l in range(len(pm)):
            for n_i in range(len(pm)-1):
                if vm[abs(l-n_i)] == vm[l]:
                    pm[l] = pm[abs(l-n_i)]

    # Generate evaluation for each solution matrix, pm
    list_eva_pm = []
    for s in list_s:
        list_eva_pm.append(len(np.unique(s[1])))

    # find optimal solution
    opt_eva = np.max(list_eva_pm)
    index_opt_eva = list_eva_pm.index(opt_eva)
    list_s_index.pop(index_opt_eva)
    s_opt = list_s[index_opt_eva]

    # update other solutions than the optimal solution
    for i in range(len(list_s)):
        # skip the optimal solution
        if i == index_opt_eva:
            continue
        
        prob = random.uniform(0, 1)
        a = random.randint(0, 2)
        rand = random.uniform(0, 1)
        cf_1 = abs(2*a*rand - a)
        cf_2 = 2*rand
        s_rand = list_s[list_s_index[random.randint(0, len(list_s_index)-1)]]
        dir = abs(cf_2*s_rand - list_s[i])
        dir_i = abs(s_opt - list_s[i])
        b = random.uniform(-1, 1)
        z = random.uniform(-1, 1)
        if prob < 0.5 and cf_1 < 1:
            # condition 1
            curr_s = s_opt - cf_1*dir
        elif prob < 0.5 and cf_1 >= 1:
            # condition 2
            curr_s = s_rand - cf_1*dir
        else:
            # condition 3
            curr_s = dir_i * math.e**(b*z) * math.cos(2*phi*z) + s_opt
        
        list_s[i] = curr_s

    for s_1 in list_s:
        vm, pm = s_1
        for m_i in range(len(vm)):
            if vm[m_i] not in list_m:
                vm[m_i] = math.ceil(vm[m_i] % m)
                # vm[m_i] = vm[m_i] % m
        for n_i in range(len(pm)):
            if pm[n_i] not in list_n:
                pm[n_i] = math.ceil(pm[n_i] % n)
                # pm[n_i] = pm[n_i] % n

    for s_1ndex in range(len(list_s)):
        print(s_1ndex)
        print(list_s[s_1ndex])
        print()
    
    return list_s


if __name__ == "__main__":
    get_solution_matrix()
