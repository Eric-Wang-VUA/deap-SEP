#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

from functools import wraps


def bin2float(min_, max_, nbits):
    """Convert a binary array into an array of float where each
    float is composed of *nbits* and is between *min_* and *max_*
    and return the result of the decorated function.

    """
    def wrap(function):
        @wraps(function)
        def wrapped_function(individual, *args, **kargs):
            # User must take care to make nelem an integer.
            nelem = len(individual) // nbits
            decoded = [0] * nelem
            for i in range(nelem):
                gene = int("".join(map(str,
                                       individual[i * nbits:i * nbits + nbits])),
                           2)
                div = 2**nbits - 1
                temp = gene / div
                decoded[i] = min_ + (temp * (max_ - min_))
            return function(decoded, *args, **kargs)
        return wrapped_function
    return wrap

branch_coverage_trap = {
    "trap_branch_1": False,  
    "trap_branch_2": False
}

def trap(individual):
    u = sum(individual)
    k = len(individual)
    if u == k:
        branch_coverage_trap["trap_branch_1"] = True
        return k
    else:
        branch_coverage_trap["trap_branch_2"] = True
        return k - 1 - u

def print_coverage_trap():
    for branch, hit in branch_coverage_trap.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

branch_coverage_inv_trap = {
    "inv_trap_branch_1": False,  
    "inv_trap_branch_2": False
}

def inv_trap(individual):
    u = sum(individual)
    k = len(individual)
    if u == 0:
        branch_coverage_inv_trap["inv_trap_branch_1"] = True
        return k
    else:
        branch_coverage_inv_trap["inv_trap_branch_2"] = True
        return u - 1

def print_coverage_inv_trap():
    for branch, hit in branch_coverage_inv_trap.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

branch_coverage_chuang_f1 = {
    "chuang_f1_branch_1": False,  
    "chuang_f1_branch_2": False
}

def chuang_f1(individual):
    """Binary deceptive function from : Multivariate Multi-Model Approach for
    Globally Multimodal Problems by Chung-Yao Chuang and Wen-Lian Hsu.

    The function takes individual of 40+1 dimensions and has two global optima
    in [1,1,...,1] and [0,0,...,0].
    """
    total = 0
    if individual[-1] == 0:
        branch_coverage_chuang_f1["chuang_f1_branch_1"] = True
        for i in range(0, len(individual) - 1, 4):
            total += inv_trap(individual[i:i + 4])
    else:
        branch_coverage_chuang_f1["chuang_f1_branch_2"] = True
        for i in range(0, len(individual) - 1, 4):
            total += trap(individual[i:i + 4])
    return total,

def print_coverage_chuang_f1():
    for branch, hit in branch_coverage_chuang_f1.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

chuang_f2_branch = [False, False, False, False]

def chuang_f2(individual):
    """Binary deceptive function from : Multivariate Multi-Model Approach for
    Globally Multimodal Problems by Chung-Yao Chuang and Wen-Lian Hsu.

    The function takes individual of 40+1 dimensions and has four global optima
    in [1,1,...,0,0], [0,0,...,1,1], [1,1,...,1] and [0,0,...,0].
    """
    total = 0
    if individual[-2] == 0 and individual[-1] == 0:
        chuang_f2_branch[0] = True 
        for i in range(0, len(individual) - 2, 8):
            total += inv_trap(individual[i:i + 4]) + inv_trap(individual[i + 4:i + 8])
    elif individual[-2] == 0 and individual[-1] == 1:
        chuang_f2_branch[1] = True 
        for i in range(0, len(individual) - 2, 8):
            total += inv_trap(individual[i:i + 4]) + trap(individual[i + 4:i + 8])
    elif individual[-2] == 1 and individual[-1] == 0:
        chuang_f2_branch[2] = True 
        for i in range(0, len(individual) - 2, 8):
            total += trap(individual[i:i + 4]) + inv_trap(individual[i + 4:i + 8])
    else:
        chuang_f2_branch[3] = True 
        for i in range(0, len(individual) - 2, 8):
            total += trap(individual[i:i + 4]) + trap(individual[i + 4:i + 8])
    return total,

def print_chuang_f2_coverage():    
    count = 0    
    for i in chuang_f2_branch:        
        if i:            
            count += 1    
    coverage = 100 * (count / 4)    
    print("coverage of the function chuang_f2 ", coverage, "%")

branch_coverage_chuang_f3 = {
    "chuang_f3_branch_1": False,  
    "chuang_f3_branch_2": False
}

def chuang_f3(individual):
    """Binary deceptive function from : Multivariate Multi-Model Approach for
    Globally Multimodal Problems by Chung-Yao Chuang and Wen-Lian Hsu.

    The function takes individual of 40+1 dimensions and has two global optima
    in [1,1,...,1] and [0,0,...,0].
    """
    total = 0
    if individual[-1] == 0:
        branch_coverage_chuang_f3["chuang_f3_branch_1"] = True
        for i in range(0, len(individual) - 1, 4):
            total += inv_trap(individual[i:i + 4])
    else:
        branch_coverage_chuang_f3["chuang_f3_branch_2"] = True
        for i in range(2, len(individual) - 3, 4):
            total += inv_trap(individual[i:i + 4])
        total += trap(individual[-2:] + individual[:2])
    return total,

def print_coverage_chuang_f3():
    for branch, hit in branch_coverage_chuang_f3.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

# Royal Road Functions
def royal_road1(individual, order):
    """Royal Road Function R1 as presented by Melanie Mitchell in :
    "An introduction to Genetic Algorithms".
    """
    nelem = len(individual) // order
    max_value = int(2**order - 1)
    total = 0
    for i in range(nelem):
        value = int("".join(map(str, individual[i * order:i * order + order])), 2)
        total += int(order) * int(value / max_value)
    return total,


def royal_road2(individual, order):
    """Royal Road Function R2 as presented by Melanie Mitchell in :
    "An introduction to Genetic Algorithms".
    """
    total = 0
    norder = order
    while norder < order**2:
        total += royal_road1(individual, norder)[0]
        norder *= 2
    return total,
