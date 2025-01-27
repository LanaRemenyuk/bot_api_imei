from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from app.config import Config
from app.models.users import User
from app.services.imei_service import IMEIService
from app import db

config = Config()

def setup_bot():
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN, 
             default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer('Приветствую! Отправьте мне IMEI устройства для проверки.')

    @dp.message()
    async def handle_text(message: types.Message):
        from app import create_app
        
        app = create_app()
        with app.app_context():
            user = db.session.execute(
                db.select(User).filter_by(telegram_id=str(message.from_user.id))
            ).scalar_one_or_none()

            if not user:
                return await message.answer('У Вас нет прав для доступа к боту.')

            if not user.check_imei_access():
                return await message.answer('У вас нет доступа к проверке IMEI.')

            imei = message.text.strip()
            imei_data = IMEIService.check_imei_is_valid(imei, user.token)

            response = (f"Ошибка: {imei_data['error']}" if "error" in imei_data 
                        else f"Информация о IMEI:\n{imei_data}")
            
            await message.answer(response)

    return bot, dp

async def run_bot(bot: Bot, dp: Dispatcher):
    await dp.start_polling(bot)