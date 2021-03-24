import pathlib
import textwrap

import hamcrest as ham
import pytest
import re
from makeh import __version__, Makefile


def test_version(pytestconfig):
    """Dirty test to ensure __version__ aligned with project meta"""
    pyproject_toml = pathlib.Path(pytestconfig.rootdir / '../pyproject.toml').read_text()
    version, = re.findall(r'\nversion\s*=\s*"(\d+\.\d+\.\d+)"\n', pyproject_toml)
    assert __version__ == version


class TestMakefile:
    @pytest.fixture
    def simple_makefile(self) -> Makefile:
        return Makefile(textwrap.dedent("""\
            # This is a test makefile

            # Name of person to greet
            name=
            
            # Greeting to use
            greeting=hi
            
            # utility target
            _prepare:
                echo "preparing for something amazing!"
            
            # Greet person        
            greet:
                echo "$(greeting), $(name)"
        """))

    def test_renders(self, simple_makefile: Makefile):
        ham.assert_that(str(simple_makefile), ham.equal_to(textwrap.dedent("""\
            USAGE
              make [options] [target] ...
            
            VARIABLES
              name                Name of person to greet
              greeting            Greeting to use
                default: hi

            TARGETS
              <greet>             Greet person""")))
