"""Test functions from deap/benchmarks."""
import sys
import unittest

from deap import base
from deap import creator
from deap.benchmarks import binary


class BenchmarkTest(unittest.TestCase):
    """Test object for unittest of deap/benchmarks."""

    def setUp(self):

        @binary.bin2float(0, 1023, 10)
        def evaluate(individual):
            """Simplest evaluation function."""
            return individual

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        self.toolbox.register("evaluate", evaluate)

    def tearDown(self):
        del creator.FitnessMin

    def test_bin2float(self):

        # Correct evaluation of bin2float.
        zero_individual = creator.Individual([0] * 10)
        full_individual = creator.Individual([1] * 10)
        two_individiual = creator.Individual(8 * [0] + [1, 0])
        population = [zero_individual, full_individual, two_individiual]
        fitnesses = map(self.toolbox.evaluate, population)
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit
        assert population[0].fitness.values == (0.0, )
        assert population[1].fitness.values == (1023.0, )
        assert population[2].fitness.values == (2.0, )

        # Incorrect evaluation of bin2float.
        wrong_size_individual = creator.Individual([0, 1, 0, 1, 0, 1, 0, 1, 1])
        wrong_population = [wrong_size_individual]
        # It is up the user to make sure that bin2float gets an individual with
        # an adequate length; no exceptions are raised.
        fitnesses = map(self.toolbox.evaluate, wrong_population)
        for ind, fit in zip(wrong_population, fitnesses):
            # In python 2.7 operator.mul works in a different way than in
            # python3. Thus an error occurs in python2.7 but an assignment is
            # correctly executed in python3.
            if sys.version_info < (3, ):
                with self.assertRaises(AssertionError):
                    ind.fitness.values = fit
            else:
                assert wrong_population[0].fitness.values == ()
    def test_trap_function(self):
        # Test cases for binary.trap function

        # Test case 1: All ones
        individual_all_ones = [1] * 10
        fitness_all_ones = binary.trap(individual_all_ones)
        self.assertEqual(fitness_all_ones, 10)

        # Test case 2: Mixed zeros and ones
        individual_mixed = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
        fitness_mixed = binary.trap(individual_mixed)
        self.assertEqual(fitness_mixed, 4)

        # Test case 3: All zeros
        individual_all_zeros = [0] * 10
        fitness_all_zeros = binary.trap(individual_all_zeros)
        self.assertEqual(fitness_all_zeros, 9)
    
    def test_chuang_f1_function(self):
        # Test cases for binary.chuang_f1 function

        # Test case 1: Example from the description
        individual_case1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        fitness_case1 = binary.chuang_f1(individual_case1)
        self.assertEqual(fitness_case1[0], 30)

        # Test case 2: Another example with different pattern
        individual_case2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        fitness_case2 = binary.chuang_f1(individual_case2)
        self.assertEqual(fitness_case2[0], 30)
    def test_inv_trap_function(self):
        # Test cases for binary.inv_trap function

        # Test case 1: All ones
        individual_all_ones = [1] * 10
        fitness_all_ones = binary.inv_trap(individual_all_ones)
        self.assertEqual(fitness_all_ones, 9)

        # Test case 2: Mixed zeros and ones
        individual_mixed = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
        fitness_mixed = binary.inv_trap(individual_mixed)
        self.assertEqual(fitness_mixed, sum(individual_mixed) - 1)

        # Test case 3: All zeros
        individual_all_zeros = [0] * 10
        fitness_all_zeros = binary.inv_trap(individual_all_zeros)
        self.assertEqual(fitness_all_zeros, len(individual_all_zeros))
    def test_chuang_f3_function(self):
        # Test case 1: All ones
        individual_case1 = [1] * 41
        fitness_case1 = binary.chuang_f3(individual_case1)
        self.assertEqual(fitness_case1[0], 31)

        # Test case 2: All zeros
        individual_case2 = [0] * 41
        fitness_case2 = binary.chuang_f3(individual_case2)
        self.assertEqual(fitness_case2[0], 40)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BenchmarkTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
