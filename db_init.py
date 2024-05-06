import typer
import asyncio
from db.base import init_models
from db.models import *
# db resetting
cli = typer.Typer()
@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")
if __name__ == "__main__":
    cli()