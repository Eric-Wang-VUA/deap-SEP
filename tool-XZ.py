from deap.benchmarks import binary
from deap.tools import emo

def test_selChuangF2():    
    binary.chuang_f2([1, 2, 3])    
    binary.chuang_f2([0, 0, 0])    
    binary.chuang_f2([0, 1, 0])    
    binary.chuang_f2([0, 0, 1])    
    binary.print_chuang_f2_coverage()
test_selChuangF2()

def test_selIsDominate():    
    wvalues1 = [3, 2, 5]    
    wvalues2 = [2, 2, 6]    
    assert emo.isDominated(wvalues1, wvalues2) == False
    wvalues1 = [3, 2, 5]    
    wvalues2 = [3, 3, 6]    
    assert emo.isDominated(wvalues1, wvalues2) == True
    emo.print_isDominated()
test_selIsDominate()