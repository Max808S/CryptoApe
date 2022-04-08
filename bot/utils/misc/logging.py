import logging
from pathlib import Path


log_folder = Path.home().joinpath("/Users/keyglock/Documents/python/CryptoCurrency/logs")
Path(log_folder).mkdir(parents=True, exist_ok=True)
log_file = log_folder.joinpath("logs_tgbot.log")


if not log_file.exists():
    open(log_file, "w").close()

# FORMAT = f"[%(asctime)s] %(module)s - %(funcName)s [LINE:%(lineno)d] #%(levelname)-5s %(message)s"
FORMAT = f"[%(asctime)s] [LINE:%(lineno)d] #%(levelname)-5s %(message)s"


logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    handlers=[logging.FileHandler(log_file, mode="w+"), logging.StreamHandler()]
)


logger = logging.getLogger(__name__)

# coin notify 
# log = logging.getLogger('broadcast')