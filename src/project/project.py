from typing import Optional

import click
import ujson as json
from click import Context


@click.group()
@click.pass_context
@click.option("--config", type=str, required=False)
@click.option("--device", type=int, required=False, default=0)
def main(ctx: Context, config: Optional[str], device: int):
    if config is not None:
        with open(config) as infile:
            ctx.obj["config"] = json.load(infile)

    ctx.obj["device"] = device


@main.command()
@click.pass_context
@click.option("--dataset-dir", required=True, type=str)
@click.option("--out-dir", required=False, type=str)
def train(ctx: Context, dataset_dir: str, out_dir: str):
    print("Training")


@main.command()
@click.pass_context
@click.option("--dataset-dir", required=True, type=str)
@click.option("--out-dir", required=False, type=str)
def test(ctx: Context, dataset_dir: str):
    print("Testing")


def start():
    main(obj={})


if __name__ == "__main__":
    start()
