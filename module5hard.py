import time
import hashlib # Мне сказали, что так надёжнее :D


class User:
    users = []

    def __new__(cls, *args, **kwargs):
        cls.users.append(args)
        return super().__new__(cls)

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __repr__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.time_now = 0
        self.adult_mode = adult_mode
        self.duration = duration


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        self.users = users if users is not None else []
        self.videos = videos if videos is not None else []
        self.current_user = current_user

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search):
        that_video = []
        for vid in self.videos:
            if search.lower() in vid.title.lower():
                that_video.append(vid.title)
        return that_video

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        check_video = None
        for lfv in self.videos:  # Looking for video
            if lfv.title == title:
                check_video = lfv
                break

        if check_video is None:
            return

        if check_video and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста, покиньте страницу")
            return
        for i in range(check_video.duration):
            print(f"{i + 1}")
            time.sleep(1)
        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
