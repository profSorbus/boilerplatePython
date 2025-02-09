import logging
import logging.config
from datetime import datetime
from app.core.config_manager import ConfigManager


class LogManager:
    def __init__(self, configManager: ConfigManager):
        timestamp = datetime.now().strftime("%Y%m%d")

        logging.config.fileConfig(
            configManager.getLogConfPath(),
            disable_existing_loggers=False,
            defaults={"logfilename": f"logs/sample_app_{timestamp}.log"},
        )
