from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.int("ADMINS")  # Тут у нас будет список из админов
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


# class Config:  # TODO
#     _TOKEN = os.environ.get("TELEGRAM_TOKEN")

#     @property
#     def token(self) -> str:
#         if not Config._TOKEN:
#             raise EnvironmentError("Provide TELEGRAM_TOKEN env variable")
#         return Config._TOKEN