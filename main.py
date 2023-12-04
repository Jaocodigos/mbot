from utils import verify_format
from base_classes.message_channels import verify_platform


def start_chatbot():
    print("Welcome to MBot v1.0!")
    print("To use, insert the message on this way: MESSAGE-TYPE - MESSAGE(If it's a text-message) OR FORMAT(If it's a midia) - "
          "PLATFORM(WhatsApp, Telegram, Instagram or Facebook) - "
          "USER-NUMBER(for WhatsApp or Telegram) OR USERNAME(for Instagram, Facebook or Telegram).")
    get_message()


def get_message():
    message = input("What message you want to send?: ")
    data = message.split('-')
    if len(data) < 4:
        print("Some field is missing, verify and try again.")
        get_message()
    message_type = data[0].replace(' ', '').replace('"', '')
    message_or_format = data[1]
    platform = data[2].replace(' ', '').replace('"', '')
    user = data[3].replace(' ', '').replace('"', '')
    sender = verify_platform(platform)()
    if not sender:
        print("Invalid platform, verify and try again.")
        get_message()
    if message_type == 'text':
        print(sender.send_text_message(user, message_or_format))
        get_message()
    # Supported image types: jpeg, png and GIF
    # Supported video types:  MP4, Webm, and Av1
    # Supported file types: PDF and DOC
    if not verify_format(data[1].replace(' ', '').replace('"', '')):
        print("Invalid file format, verify and try again.")
        get_message()
    if message_type == 'image':
        print(sender.send_image_message(user, message_or_format))
        get_message()
    if message_type == 'video':
        print(sender.send_video_message(user, message_or_format))
        get_message()
    if message_type == 'file':
        print(sender.send_file_message(user, message_or_format))
        get_message()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_chatbot()
