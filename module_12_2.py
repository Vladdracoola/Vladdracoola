import module_12_2_task
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def add_results(cls, race_id, results):
        cls.all_results[race_id] = results

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
        self.__class__.add_results('Забег_1', test_1)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament_check = module_12_2_task.Tournament(90, self.andrey, self.nick)
        test_2 = tournament_check.start()
        self.assertTrue(test_2[max(test_2.keys())] == self.nick)
        self.__class__.add_results('Забег_2', test_2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament_check = module_12_2_task.Tournament(90, self.usain, self.andrey, self.nick)
        test_3 = tournament_check.start()
        self.assertTrue(test_3[max(test_3.keys())] == self.nick)
        self.__class__.add_results('Забег_3', test_3)


if __name__ == '__main__':
    unittest.main()
