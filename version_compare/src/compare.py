from .version import Version
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('compare')


def compare(version_1: str, version_2: str):
    """Compares two version strings and returns an ordered tuple if they're different or a single element
    tuple if they are equal

    Args:
        version_1: Version string
        version_2: Version string

    Returns:
        tuple
    """
    try:
        v1 = Version(version_1)
        v2 = Version(version_2)

        result = (version_1,)
        if version_1 == version_2:
            return result

        if v1.release < v2.release:
            result = (version_1, version_2)
        elif v1.release > v2.release:
            result = (version_2, version_1)
        elif v1.pre_rls and not v2.pre_rls:
            result = (version_1, version_2)
        elif v2.pre_rls and not v1.pre_rls:
            result = (version_2, version_1)
        elif v1.pre_rls[0] < v2.pre_rls[0]:
            result = (version_1, version_2)
        elif v1.pre_rls[0] > v2.pre_rls[0]:
            result = (version_2, version_1)
        elif v1.pre_rls[1] < v2.pre_rls[1]:
            result = (version_1, version_2)
        elif v1.pre_rls[1] > v2.pre_rls[1]:
            result = (version_2, version_1)

        return result

    except ValueError:
        logger.error(f'Value error, please check your input: {version_1} {version_2}')
