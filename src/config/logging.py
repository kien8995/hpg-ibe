"""
    logging config
"""
import os

from loguru import logger

project_root = os.path.dirname(os.path.dirname(__file__))


def setup_logging():
    """logging config function
    """
    logger.add(os.path.join(project_root,  'logs', 'file.log'), retention="10 days")
