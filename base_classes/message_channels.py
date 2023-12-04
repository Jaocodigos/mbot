from base_classes.message_types import VideoMessage, FileMessage, DefaultMessage, PhotoMessage
from utils import verify_username, verify_user_number


class Channel(object):

    def send_text_message(self, user_or_phone, message):
        if not verify_user_number(user_or_phone) and not verify_username(user_or_phone):
            return self.invalid_user
        if message == '':
            return 'Invalid message, send something.'
        sender = DefaultMessage(message=message)
        return f"({self.platform} - {user_or_phone}) Message: {sender.message}, date: {sender.date}"

    def send_image_message(self, user_or_phone, image_format):
        if not verify_user_number(user_or_phone) and not verify_username(user_or_phone):
            return self.invalid_user
        sender = PhotoMessage(file_format=image_format)
        return f"({self.platform} - {user_or_phone}) Image Size: {sender.image_size}, Format: {sender.file_format}," \
               f"Memory required: {sender.memory_use}"

    def send_video_message(self, user_or_phone, video_format):
        if not verify_user_number(user_or_phone) and not verify_username(user_or_phone):
            return self.invalid_user
        sender = VideoMessage(file_format=video_format)
        return f"({self.platform} - {user_or_phone}) Video Duration: {sender.duration}, Format: {sender.file_format}, " \
               f"Memory required: {sender.memory_use}"

    def send_file_message(self, user_or_phone, file_format):
        if not verify_user_number(user_or_phone) and not verify_username(user_or_phone):
            return self.invalid_user
        sender = FileMessage(file_format=file_format)
        return f"({self.platform} - {user_or_phone}) Format: {sender.file_format}, Memory required: {sender.memory_use}"

    @property
    def invalid_user(self):
        return 'Invalid phone number or username, verify and try again.'


class WhatsApp(Channel, object):

    def __init__(self):
        self.platform = 'WhatsApp'


class Telegram(Channel, object):
    def __init__(self):
        self.platform = 'Telegram'


class Instagram(Channel, object):
    def __init__(self):
        self.platform = 'Instagram'


class Facebook(Channel, object):
    def __init__(self):
        self.platform = 'Facebook'


def verify_platform(platform):
    if platform.lower() == 'whatsapp':
        return WhatsApp
    elif platform.lower() == 'instagram':
        return Instagram
    elif platform.lower() == 'facebook':
        return Facebook
    elif platform.lower() == 'telegram':
        return Telegram
    return False
