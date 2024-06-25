from deap.benchmarks import binary

def test_trap():
    result = binary.trap([1, 1, 1])
    binary.print_coverage_trap()
    
    result = binary.trap([0, 0, 0])
    binary.print_coverage_trap()
print("Test for trap function!")
test_trap()

def test_inv_trap():
    result = binary.inv_trap([1, 1, 1])
    binary.print_coverage_inv_trap()
    
    result = binary.inv_trap([0, 0, 0])
    binary.print_coverage_inv_trap()


print()
print("Test for inv_trap function!")
test_inv_trap()
