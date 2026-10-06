import logging

logger = logging.getLogger(__name__)


def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # 找出 required_columns 里但不在 df 列中的
    missing = [col for col in required_columns if col not in df.columns]

    if missing:                                              # 有缺的列
        logger.error("Missing required columns: %s", missing)
        raise ValueError(f"Missing required columns: {missing}")

    logger.info("Validation completed")                     # 没缺 → 验证通过
    return df