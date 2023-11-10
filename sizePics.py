# -*- coding: utf-8 -*-

import os
import click
from PIL import Image


BASE = "./img/work"

@click.group()
def cli():
    pass

@cli.command()
def show():
    """List images in each directory and their sizes"""
    dirs = ["full", "thumbs"]
    for d in dirs:
        click.echo(click.style(f"{d} --", fg='red'))
        for f in os.listdir(f"{BASE}/{d}/"):
            im = Image.open(f"{BASE}/{d}/{f}")
            click.secho(f"  |- {f}:: ", fg='blue', nl=False)
            click.secho(f"{im.size}", fg='green')
        

@cli.command()
@click.option('--pixels', "-p", default=400, help='max h|w of image resized')
def resize(pixels):
    """Re-write images from the "full" directory into the respective "thumbs"
    directory. Default set up for how it currently is.
    """

    size = pixels, pixels 
    for f in os.listdir(f"{BASE}/full/"):
        im = Image.open(f"{BASE}/full/{f}")
        old_size = im.size
        im.thumbnail(size, Image.ADAPTIVE)
        im.save(f"{BASE}/thumbs/{f}", "JPEG")
        click.secho(f"{f}:: {im.size} written from {old_size}", fg='red', bold=True)

        
if __name__ == '__main__':
    cli()
