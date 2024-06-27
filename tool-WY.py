from deap.benchmarks import binary

def test_chuang_f1():
    result = binary.chuang_f1([1, 1, 0])
    binary.print_coverage_chuang_f1()
    
    result = binary.chuang_f1([0, 0, 1])
    binary.print_coverage_chuang_f1()
print("Test for chuang_f1 function!")
test_chuang_f1()

def test_chuang_f3():
    result = binary.chuang_f3([0, 0, 0])
    binary.print_coverage_chuang_f3()

    result = binary.chuang_f3([1, 1, 1])
    binary.print_coverage_chuang_f3()

print()
print("Test for chuang_f3 function!")
test_chuang_f3()