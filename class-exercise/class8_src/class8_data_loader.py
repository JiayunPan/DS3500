import logging
import pandas as pd

logger = logging.getLogger(__name__)


def load_netflix(filepath):
    """Load the Netflix CSV file."""
    df = pd.read_csv(filepath)              # 用 pandas 读
    logger.info("Data loaded")              # 记一条 INFO
    return df                               # 返回 DataFrame