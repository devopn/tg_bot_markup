import asyncio
import logging
from config import config

# Aiogram imports
from aiogram import Dispatcher, Bot, types


# Routers



# Set up logging
logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def main():

    # Set up bot
    bot = Bot(token=config.tg_token)
    await bot.set_my_commands(
        commands=[
            types.BotCommand(command="start", description="Перезапуск бота "),
            ]
    )

    dp = Dispatcher()
    dp.include_routers()

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())