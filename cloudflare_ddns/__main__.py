import logging
from typing import Tuple

import click
from cloudflare_ddns.app import ApplicationJob
from cloudflare_ddns.constants import DEFAULT_DELAY

log = logging.getLogger("ddns")


@click.command()
@click.option('--delay', '-d', default=DEFAULT_DELAY, show_default=True)
@click.option('--token', '-k', prompt="Enter your Cloudflare Token", hide_input=True, show_envvar=True)
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.argument("domain", nargs=-1)
def start(delay: str, token: str, verbose: int, domain: Tuple[str]) -> None:
    """Main application entrypoint."""
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG if verbose else logging.INFO
    )

    ApplicationJob(delay, token, domain).launch()


# Main entrypoint
if __name__ == "__main__":
    start(auto_envvar_prefix="CF_DDNS")
