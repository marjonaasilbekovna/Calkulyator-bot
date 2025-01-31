from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("💖 Buyruqlar... \n\nBotdan foydalanish uchun -'/start' tugmasini bosing.\nKalkulyatonri ishga tushirish uchun - '/calc' tugmasini bosing. \n'/about' - Bot haqida qisqacha ma'lumot.\n'/xabar'- bot adminiga murojat uchun.\n'/bot_admin' - bot admini.\n\n\n🎗️Qo'shimcha uchun...\n\nKalyutorni ishga tushirganingizda tugmalardagi '1, 2...8, 9' sonlari huddi oddiy kundalik hayotimizda foydalanadigan kalkulyator kabi raqamlar.\n '+' - bu tugma qo'shish amalini bajaradi.\n'-' - bu tugma ayirish amalini bajaradi.\n'*' - bu tugma ko'paytirish amalini bajaradi.\n',' - bu tugma butun qismga ega sonlar uchun kerak; masalan; 2,9 kabi.\n'/' - bu tugma bo'lish amalini bajaradi.\n'=' - bu tugma tengli amali.\n'D' - bu tugma sonlarni uchiradi.\n'C' - bu tugma bajargan amalingizni butkul tozalaydi.\n\nBiz bilan yanada oson.!😉")
