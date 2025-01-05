from time import sleep

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname=nickname
        self.password=password
        self.age=age


class  video:
    def __int__(self, title: str, duration: int, time_now: int, adult_mode: bool=False):
        self.title=title
        self.duration=duration
        self.time_now=0
        self.adult_mode=adult_mode


class UrTube:
    def __init__(self):
        self.users=[]
        self.videos=[]
        self.current_user=None

    def log_in (self, nickname, password):
        for i in self.users:
            if nickname in i and password in i:
                self.current_user=nickname


    def register (self, nickname, password, age):




    # def log_out ()
    #
    # def add(self):
    #
    # def get_videos ()
    #
    # def watch_video()


# if __name__ == '__main__':
#
# ur = UrTube()

# v1 = Video('Лучший язык программирования 2024 года', 200)
#
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


#
# # Добавление видео
#
# ur.add(v1, v2)


#
# # Проверка поиска
#
# print(ur.get_videos('лучший'))
#
# print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

# ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

# ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

# ur.watch_video('Для чего девушкам парень программист?')



# # Проверка входа в другой аккаунт
#
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
#
# print(ur.current_user)


#
# # Попытка воспроизведения несуществующего видео
#
# ur.watch_video('Лучший язык программирования 2024 года!')