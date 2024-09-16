import unittest
import tests_12_3



newTS = unittest.TestSuite()

newTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
newTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(newTS)