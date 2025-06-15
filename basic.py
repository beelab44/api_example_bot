# handlers/basic.py
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.weather_api import get_weather, get_random_duck

router = Router()

class WeatherStates(StatesGroup):
    city = State()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        f"Вітаємо у боті погоди, {message.from_user.first_name}!\n"
        "Бажаєте отримати інформацію про погоду?\nНадішліть слово погода"
    )

@router.message(F.text == "Погода")
async def weather_command(message: Message, state: FSMContext):
    await message.answer("Надішліть назву міста, і я надішлю вам погоду в цьому місті")
    await state.set_state(WeatherStates.city)

@router.message(WeatherStates.city)
async def process_city(message: Message, state: FSMContext):
    city = message.text
    weather_message = get_weather(city)
    full_text = f"{weather_message}"
    await message.answer(full_text)
    await state.clear()


@router.message(Command("duck"))
async def start_command(message: Message):
    duck_url = get_random_duck()
    await message.answer_photo(
        duck_url,
        caption="Ось ваша випадкова улюблена качка"
    )