import logging
from pathlib import Path

# logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
#                     level=logging.INFO) # level=logging.DEBUG


log_folder = Path.home().joinpath("logs")
Path(log_folder).mkdir(parents=True, exist_ok=True)
log_file = log_folder.joinpath("crypto_cat_tgbot.log")

if not log_file.exists():
    open(log_file, "w").close()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(log_file, mode="w+"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

# coin notify 
log = logging.getLogger('broadcast')