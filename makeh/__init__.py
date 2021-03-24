__version__ = '0.2.0'

import pathlib
import re
import textwrap
import typing

import jinja2
import typer

re_target = re.compile('\n# (?P<description>.+)\n(?P<name>[^\\s:]+):.*')
re_variable = re.compile('\n# (?P<description>.+)\n(?P<name>[^\\s=]+)=(?P<default>.*)')


class Target(typing.TypedDict):
    name: str
    description: str


class Variable(typing.TypedDict):
    name: str
    description: str
    default: typing.Optional[str]


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
        self.targets: typing.Dict[str, str] = {}
        self.arguments: typing.Dict[str, str] = {}

    def __str__(self) -> str:
        targets: typing.List[Target] = []
        variables: typing.List[Variable] = []
        for comment, target in re_target.findall(self.text):
            if target.startswith('_'):
                continue
            targets.append(Target(
                name=target.strip(),
                description=comment.strip()
            ))

        for description, name, default in re_variable.findall(self.text):
            variables.append(Variable(description=description,
                                      name=name,
                                      default=default or None
                                      ))

        return self.template.render(
            targets=targets,
            variables=variables
        ).strip()


def run():
    typer.run(main)


def main(makefile: str = typer.Argument('Makefile')):
    from makeh import Makefile
    path = pathlib.Path(makefile)
    if not path.exists():
        typer.echo(f'{path.absolute()} not found!')
        raise typer.Exit(1)

    typer.echo(str(Makefile(path.read_text())))
