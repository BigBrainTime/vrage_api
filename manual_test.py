from src.vrage_api import vrage_api
import asyncio


async def main():
    vrage = vrage_api.VRageAPI("http://127.0.0.1:8080", "MR5dpr/bbIDfstFErBKZ8A==")
    print(await vrage.get_server_info())
    await vrage.disconnect()

if __name__ == "__main__":
    asyncio.run(main())