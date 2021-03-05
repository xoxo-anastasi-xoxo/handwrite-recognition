import os

import click as click

from ml import consumers
import json


@click.group()
def main():
    pass


@main.command()
@click.option(
    "--model",
    default="TestModel",
    help=(
        "Class to use for model interaction. Default is 'TestModel'"
    ),
)
@click.option(
    "--config-file",
    default="config.json",
    help=(
        "Config passed to ML model"
    ),
)
def start(model_classname, config_file):
    if os.path.isfile(config_file):
        config = json.load(open(config_file))
    else:
        config = None
    consumer = consumers.Consumer(model_classname, config)
    consumer.listen_queue()


if __name__ == '__main__':
    main()
