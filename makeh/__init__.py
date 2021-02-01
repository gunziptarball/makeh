__version__ = '0.1.0'

import pathlib
import re
import typing

import typer

re_target = re.compile('\n# (?P<comment>.+)\n(?P<name>[^\\s:]+):.*')
re_argument = re.compile('^# (?P<comment>.+)\n(?P<name>[^\\s=]+)=(?P<default>.*)$')


class Target(typing.TypedDict):
    name: str
    description: str


class Argument(typing.TypedDict):
    name: str
    description: str
    default: typing.Optional[str]


class Makefile:
    def __init__(self, text: str):
        self.text = text
        self.targets: typing.Dict[str, str] = {}
        self.arguments: typing.Dict[str, str] = {}

    def __str__(self) -> str:
        target_section = []
        for comment, target in re_target.findall(self.text):
            if target.startswith('_'):
                continue
            target = target.strip() + '>'
            target_section.append(f'  <{target:19}{comment.strip()}')
        return '\n'.join(['USAGE', '  make [options] [target] ...', '', 'TARGETS'] + target_section)


def run():
    typer.run(main)


def main(makefile: str = typer.Argument('Makefile')):
    from makeh import Makefile
    path = pathlib.Path(makefile)
    if not path.exists():
        typer.echo(f'{path.absolute()} not found!')
        raise typer.Exit(1)

    typer.echo(str(Makefile(path.read_text())))
