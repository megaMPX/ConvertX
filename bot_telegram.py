from aiogram.utils import executor
from create_bot import dp 

async def on_startup(_):
	print('Бот запущен епт')


from handlers import func

func.funct(dp)


executor.start_polling(dp,skip_updates=True, on_startup=on_startup)