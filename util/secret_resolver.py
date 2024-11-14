import os
import asyncio
import nest_asyncio
from onepassword.client import Client

# Allow nested event loops
nest_asyncio.apply()

# Get the service account token from the environment variable
OP_SERVICE_ACCOUNT_TOKEN = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")

async def get_secret(secret_path: str) -> str:
    """
    Retrieve a secret from 1Password using a secret reference path.
    
    Args:
        secret_path (str): The 1Password secret reference path
    
    Returns:
        str: The resolved secret value
    
    Raises:
        ValueError: If the service account token is missing
    """
    token = OP_SERVICE_ACCOUNT_TOKEN
    if not token:
        raise ValueError("Service account token is missing. Set the OP_SERVICE_ACCOUNT_TOKEN environment variable.")

    client = await Client.authenticate(
        auth=token,
        integration_name="My 1Password Integration",
        integration_version="v1.0.0"
    )

    return await client.secrets.resolve(secret_path)

def resolve_secret(secret_path: str) -> str:
    """
    Synchronous wrapper to get a secret from 1Password.
    
    Args:
        secret_path (str): The 1Password secret reference path
    
    Returns:
        str: The resolved secret value
    """
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(get_secret(secret_path))