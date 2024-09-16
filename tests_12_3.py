import module_12_1_task, module_12_2_task
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        mr_walker = module_12_1_task.Runner('mr_Walker')
        for _ in range(10):
            mr_walker.walk()
        self.assertEqual(mr_walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        mr_runner = module_12_1_task.Runner('mr_Runner')
        for _ in range(10):
            mr_runner.run()
        self.assertEqual(mr_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        mr_black = module_12_1_task.Runner('mr.Black')
        mr_white = module_12_1_task.Runner('mr.White')
        for _ in range(10):
            mr_black.walk()
            mr_white.run()
        self.assertNotEqual(mr_white.distance, mr_black.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = module_12_2_task.Runner("Усэйн", 10)
        self.andrey = module_12_2_task.Runner("Андрей", 9)
        self.nick = module_12_2_task.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"{place}. {runner}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament_check = module_12_2_task.Tournament(90, self.usain, self.nick)
        test_1 = tournament_check.start()
        self.assertTrue(test_1[max(test_1.keys())] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament_check = module_12_2_task.Tournament(90, self.andrey, self.nick)
        test_2 = tournament_check.start()
        self.assertTrue(test_2[max(test_2.keys())] == self.nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament_check = module_12_2_task.Tournament(90, self.usain, self.andrey, self.nick)
        test_3 = tournament_check.start()
        self.assertTrue(test_3[max(test_3.keys())] == self.nick)


if __name__ == '__main__':
    unittest.main()
