print("BOT BOOTED", flush=True)
import asyncio
from core.engine import telegram_loop,world_loop

async def main():
    try:
        print("MAIN START")
        await asyncio.gather(
            telegram_loop(),
            world_loop()
        )
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(main())