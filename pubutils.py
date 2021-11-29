import click
import os
from shlib.shlib import ls, lsd, lsf, rm, to_path, cp, mkdir, touch, mv


@click.group()
def cli():
    """ Writing utilities """
    pass


@cli.command()
@click.option('--format', default='ieee', type=click.Choice(['ieee', 'article'], case_sensitive=False), help='Template format. Currently ieee and article are supported')
@click.argument('root', type=click.Path(exists=True))
@click.argument('name', type=str)
def new_note(root, name, format):
    """ Create new phd note """
    pubutil_path = to_path(__file__).parent
    # Create root dir
    project_path = to_path(root, name)
    mkdir(project_path)

    # Create figures dir
    figpath = to_path(project_path, "figures")
    mkdir(figpath)

    # Create main tex file from template
    if format == 'ieee':
        template_path = to_path(pubutil_path, 'ieee_template.tex')
    elif format == 'article':
        template_path = to_path(pubutil_path, 'article_template.tex')

    with open(to_path(project_path, f'{name}.tex'), 'w') as fo:
        with open(template_path, 'r') as fi:
            lines = fi.readlines()
            fo.writelines(lines)

    # Create meta tex file from template
    template_path = to_path(to_path(__file__).parent, 'meta_template.tex')

    with open(to_path(project_path, f'meta.tex'), 'w') as fo:
        with open(template_path, 'r') as fi:
            lines = fi.readlines()
            fo.writelines(lines)

    # Create empty bib file
    touch(to_path(project_path, f'bibliography.bib'))
