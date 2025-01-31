from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


add = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Qo'shish +"),]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Eslatma qo'shish uchun tanlang"
)