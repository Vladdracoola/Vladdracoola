import module_12_2_task
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_tournament_1(self):
        tournament_check = module_12_2_task.Tournament(90, self.usain, self.nick)
        test_1 = tournament_check.start()
        self.assertTrue(test_1[max(test_1.keys())] == self.nick)

    def test_tournament_2(self):
        tournament_check = module_12_2_task.Tournament(90, self.andrey, self.nick)
        test_2 = tournament_check.start()
        self.assertTrue(test_2[max(test_2.keys())] == self.nick)

    def test_tournament_3(self):
        tournament_check = module_12_2_task.Tournament(90, self.usain, self.andrey, self.nick)
        test_3 = tournament_check.start()
        self.assertTrue(test_3[max(test_3.keys())] == self.nick)



if __name__ == '__main__':
    unittest.main()
