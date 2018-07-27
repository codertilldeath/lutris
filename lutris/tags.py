import yaml
import os

from lutris import settings
from lutris.util.system import path_exists
from lutris.util.log import logger


def get_tags_from_file():
    """Read filename and return parsed yaml"""
    tags_filename = os.path.join(settings.CONFIG_DIR, "tags.yml")
    if not path_exists(tags_filename):
        return []
    try:
        content = open(tags_filename, 'r').read()
        yaml_content = yaml.load(content)['tags'] or []
    except (yaml.scanner.ScannerError, yaml.parser.ParserError):
        logger.error("error parsing file %s", tags_filename)
        yaml_content = []
    return yaml_content


__all__ = get_tags_from_file()
