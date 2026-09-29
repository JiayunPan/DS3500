import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.debug("DataFrame shape: %s", df.shape)

    print("Shape:", df.shape)
    print("First 5 rows:")
    print(df.head())
    print("Columns:", list(df.columns))
    print("Data types:")
    print(df.dtypes)                    


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = len(df) 
    df = df.drop_duplicates()
    after = len(df)

    logger.debug("Rows before: %s, after: %s", before, after)  
    return df                           


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before = len(df)
    df = df.dropna()
    after = len(df)

    logger.debug("Rows before: %s, after: %s", before, after)
    return df