import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Filter
from aiogram.types import Message

TOKEN = "7938184656:AAG2YZzuT09Iaj44qifwovK1zlF_hBe0px4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Xabarni forward qilgan foydalanuvchilarning xabarini o‘chirish
class ForwardFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return bool(message.forward_from or message.forward_from_chat)


@dp.message(ForwardFilter())
async def delete_forwarded_message(message: types.Message):
    await message.delete()
    await message.answer("Forward qilish taqiqlangan!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
