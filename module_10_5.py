import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start = datetime.datetime.now()
# for file in filenames:
# read_info(file)
# end = datetime.datetime.now()
# print(end - start)
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)

# 0:00:02.866205 - Многопроцессорный метод
# 0:00:06.925203 - Линейный метод
