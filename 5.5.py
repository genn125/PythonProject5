# 5.5 Дополнительное практическое задание по модулю: "Классы и объекты."
# Задача "Свой YouTube":
import time

class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname=nickname
        self.password=hash(password)
        self.age=age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title=str(title)                                        # Заголовок (Название видео (фильма)
        self.duration=int(duration)                                  # Продолжительность
        self.time_now=time_now                                      # секунда остановки (изначально 0)
        self.adult_mode=adult_mode                                  # ограничение по возрасту

class UrTube:
# 1
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
# 3
    def register(self, nickname: str, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'6 --- Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)
# 2
    def log_in (self,nickname: str, password):
        for i in self.users:
            if nickname in i and hash(password) in i:
                self.current_user=i
# 4
    def log_out (self):
        self.current_user = None # сброс текущего пользователя
# 5
    def add(self, *args: Video):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
# 6
    def get_videos (self, search_word: str):
        videos_list = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():                  # с учетом регистра
                videos_list.append(i.title)
        return videos_list
# 7
    def watch_video(self, title: str):
        if self.current_user is None:
            print('3 --- Войдите в аккаунт чтобы смотреть видео')
            return

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end='    ')
                        time.sleep(0.1)                                # задержки выполнения на N секунду
                    video.time_now = 0
                    print('Конец видео ')
                else:
                    print('4 --- Вам нет 18 лет, пожалуйста покиньте страницу')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10, adult_mode=True)
v2 = Video('Для чего девушкам парень программист?', 2, adult_mode=True)

# Добавление видео
ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

# поиск видео без регистрации
ur.watch_video('Для чего девушкам парень программист?')
# поиск видео при регистрации по ограничению возраста
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
# Правильная регистрация и воспроизведение видео
ur.register('urban_pythonist', 'iScX4', 25)
ur.watch_video('Лучший язык программирования 2024 года')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print('7 ---', ur.current_user)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования ЛЮБОГО  года!')