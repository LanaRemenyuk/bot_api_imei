import uuid
from app import db

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    """Модель пользователя в БД"""
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(100), nullable=False, unique=True)
    telegram_id = db.Column(db.String(100), nullable=False, unique=True)
    token = db.Column(db.String(255), nullable=True)
    is_whitelisted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def check_imei_access(self):
        """Метод для проверки, имеет ли пользователь доступ к проверке IMEI."""
        return self.is_whitelisted

    def validate_username(self, username):
        """Проверка валидности имени пользователя."""
        if len(username) < 3:
            raise ValueError('Username must be at least 3 characters long.')
        return username

    def validate_telegram_id(self, telegram_id):
        """Проверка валидности Telegram ID."""
        if not telegram_id.isdigit():
            raise ValueError('Telegram ID must contain only digits.')
        return telegram_id

    def validate_token(self, token):
        """Проверка валидности токена."""
        if len(token) < 10:
            raise ValueError('Token must be at least 10 characters long.')
        return token
