import logging
import traceback
import unittest
import module_12_4_task

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            mr_walker = module_12_4_task.Runner('mr_Walker', -5)
            for _ in range(10):
                mr_walker.walk()
            self.assertEqual(mr_walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверная скорость для Runner {e}, {traceback.print_exc()}")

    def test_run(self):
        try:
            mr_runner = module_12_4_task.Runner(5, 'mr_Runner')
            for _ in range(10):
                mr_runner.run()
            self.assertEqual(mr_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверный тип данных для объекта Runner {e}, {traceback.print_exc()}")


if __name__ == '__main__':
    unittest.main()
