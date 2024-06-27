from deap.tools import emo

def test_selNSGA2():
    individual = []
    assert(emo.selNSGA2(individual, 0) == [])
    assert(emo.selNSGA2(individual, 5) == [])
    assert(emo.selNSGA2(individual, 0, "log") == [])
    assert(emo.selNSGA2(individual, 0, "else") == 0)

test_selNSGA2()
emo.print_selNSGA2Coverage()

def test_randomselect():
    array = [5, 6, 8, 9, 19, 21]
    assert(emo._randomizedSelect(array, 0, 0, 1) == 5)
    assert(emo._randomizedSelect(array, 0, 5, 1) == 6)

test_randomselect()
emo.print_randomizedSelectCoverage()