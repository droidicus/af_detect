import asyncio

import click
import twitchio

import twitch_secrets


async def async_main(username) -> None:
    async with twitchio.Client(
        client_id=twitch_secrets.CLIENT_ID, client_secret=twitch_secrets.CLIENT_SECRET
    ) as client:
        await client.login()
        user = await client.fetch_users(logins=[username])
        for u in user:
            print(f"User: {u.name} - ID: {u.id}")


@click.command(help="The Twitch username to query for the client ID.")
@click.argument("username", type=str)
def main(username) -> None:
    asyncio.run(async_main(username))


if __name__ == "__main__":
    main()
