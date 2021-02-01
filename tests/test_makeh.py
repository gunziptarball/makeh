import textwrap

import hamcrest as ham
import pytest

from makeh import __version__, Makefile


def test_version():
    assert __version__ == '0.1.0'


class TestMakefile:
    @pytest.fixture
    def simple_makefile(self) -> Makefile:
        return Makefile(textwrap.dedent("""\
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
            
            TARGETS
              <greet>             Greet person""")))
