import module_12_1_task
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        mr_walker = module_12_1_task.Runner('mr_Walker')
        for _ in range(10):
            mr_walker.walk()
        self.assertEqual(mr_walker.distance, 50)

    def test_run(self):
        mr_runner = module_12_1_task.Runner('mr_Runner')
        for _ in range(10):
            mr_runner.run()
        self.assertEqual(mr_runner.distance, 100)

    def test_challenge(self):
        mr_black = module_12_1_task.Runner('mr.Black')
        mr_white = module_12_1_task.Runner('mr.White')
        for _ in range(10):
            mr_black.walk()
            mr_white.run()
        self.assertNotEqual(mr_white.distance, mr_black.distance)


if __name__ == '__main__':
    unittest.main()
