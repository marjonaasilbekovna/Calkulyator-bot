from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("📌 Kalkulyator bot haqida.\n\nSalom! 🤖✨\nSizning shaxsiy aqlli hisoblash yordamchingiz.\n\n – Kalkulyator bot! Bu bot oddiy sonlardan tortib murakkab matematik ifodalargacha tez va aniq hisoblaydi.\n🔹 Asosiy imkoniyatlar:\n\n✅ Sonlar va amallar bilan oson ishlash;\n✅ Matematika bo‘yicha aniqlik bilan hisob-kitob qilish;\n✅ Interaktiv tugmalar orqali qulay foydalanish;\n✅ D va C tugmalari yordamida matnni o‘chirish va tozalash.\n\n🚀 Hisoblash uchun shunchaki /calc buyrug‘ini kiriting va boshlang!\n\n🎯 Aniq. Tez. Qulay. Endi hisob-kitob qilish bosh og‘riq emas, balki zavqli jarayon!\n\n🔢 Matematika endi yanada oson!")

