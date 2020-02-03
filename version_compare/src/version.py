import re


_PATTERN = r"(?:(?P<release>[0-9]+(\.[0-9]+)*)(?P<pre_rls>[-\.]?(?P<pre_flag>(rc|alpha|beta|pre))[-\.]?(?P<pre_n>[0-9]+)?)?)"


class Version:

    _version_parts = re.compile(_PATTERN)

    def __init__(self, version):
        _comp = self._version_parts.search(version)

        if not _comp:
            raise ValueError(f'Invalid version string: {version}')

        self.release = _comp.group('release')
        self.pre_rls = ()
        if _comp.group('pre_flag'):
            self.pre_rls = (_comp.group('pre_flag'), int(_comp.group('pre_n')) if _comp.group('pre_n') else 0)
