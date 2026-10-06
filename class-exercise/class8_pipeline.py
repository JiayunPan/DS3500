import logging
import sys
from pathlib import Path
from class8_src import load_netflix, require_columns

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def main():
    input_path = Path("../data/messy_netflix_titles.csv")

    # TODO 3: 加载 + 验证，用 try/except 接 ValueError
    try:
        df = load_netflix(input_path)
        df = require_columns(df, ["title", "type", "release_year"])
    except ValueError:
        sys.exit(1)

    logger.info("Pipeline completed")


if __name__ == "__main__":
    main()