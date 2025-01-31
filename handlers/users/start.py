from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    user = db.select_user(telegram_id=telegram_id)
    if not user:
        db.add_user(full_name=full_name, telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"🤖 ✨\n\nAssalomu alaykum hurmatli \n{full_name} \n'Calkulyator' botga hush kelibsiz.\n\n-yordam uchun '/help'  tugmasini tanlang.\n-botni ishga tushirish uchun '/calc'  tugmasini tanlang.\n\nQolgan menularni ko'rish uchun menu tugmasini tanlang.\n\n\nBu bot 'sifatedu' o'quv markazi tomonidan yaratilgan.")
    else:
        await message.answer(text=f"🤖 ✨\n\nAssalomu alaykum hurmatli \n{full_name} \n'Calkulyator' botga hush kelibsiz.\n\n-yordam uchun '/help'  tugmasini tanlang.\n-botni ishga tushirish uchun '/calc'  tugmasini tanlang.\n\nQolgan menularni ko'rish uchun menu tugmasini tanlang.\n\n\nBu bot 'sifatedu' o'quv markazi tomonidan yaratilgan.")
