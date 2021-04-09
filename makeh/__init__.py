__version__ = '0.3.0'

import pathlib
import re
import textwrap

import jinja2

re_target = re.compile('\n# (?P<description>.+)\n(?P<name>[^\\s:]+):.*')
re_variable = re.compile('\n# (?P<description>.+)\n(?P<name>[^\\s=]+)=(?P<default>.*)')


class Makefile:
    template = jinja2.Template(textwrap.dedent("""\
    USAGE
      make [options] [target] ...
    {% if variables %}

    VARIABLES
      {% for variable in variables %}
      {{ "{:20}".format(variable.name) }}
      {{- variable.description }}
      {% if variable.default %}
        default: {{ variable.default }}
      {% endif %}
      {% endfor %}
    {% endif %}

    TARGETS
      {% for target in targets %}
      {{ "{:20}".format("<" + target.name + ">") }}{{ target.description }}
      {% endfor %}"""), lstrip_blocks=True, trim_blocks=True)

    def __init__(self, text: str):
        self.text = text
        self.targets = {}
        self.arguments = {}

    def __str__(self) -> str:
        targets = []
        variables = []
        for comment, target in re_target.findall(self.text):
            if target.startswith('_'):
                continue
            targets.append({
                'name': target.strip(),
                'description': comment.strip()
            })

        for description, name, default in re_variable.findall(self.text):
            variables.append({
                'description': description,
                'name': name,
                'default': default or None
            })

        return self.template.render(
            targets=targets,
            variables=variables
        ).strip()


def run():
    import argparse

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('makefile', default='Makefile')
    main(argument_parser.parse_args().makefile)


def main(makefile):
    from makeh import Makefile
    path = pathlib.Path(makefile)
    if not path.exists():
        raise FileNotFoundError('No makefile found')

    print(str(Makefile(path.read_text())))
