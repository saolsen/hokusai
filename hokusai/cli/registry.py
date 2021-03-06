import click

import hokusai

from hokusai.cli.base import base
from hokusai.lib.common import set_verbosity, CONTEXT_SETTINGS

@base.group()
def registry(context_settings=CONTEXT_SETTINGS):
  """Interact with the project registry defined by `./hokusai/config.yml`"""
  pass


@registry.command(context_settings=CONTEXT_SETTINGS)
@click.option('--tag', type=click.STRING, help='The tag to push (default: the value of `git rev-parse HEAD`)')
@click.option('--force', type=click.BOOL, is_flag=True, help='Push even if working directory is not clean')
@click.option('--overwrite', type=click.BOOL, is_flag=True, help='Push even if the tag already exists')
@click.option('-v', '--verbose', type=click.BOOL, is_flag=True, help='Verbose output')
def push(tag, force, overwrite, verbose):
  """Build and push an image to the project's remote repo tagged as the git SHA1 of HEAD"""
  set_verbosity(verbose)
  hokusai.push(tag, force, overwrite)


@registry.command(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', type=click.BOOL, is_flag=True, help='Verbose output')
def images(verbose):
  """Print images and tags in the project's remote repo"""
  set_verbosity(verbose)
  hokusai.images()
