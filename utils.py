
image_types = ['jpeg', 'png', 'gif']
video_types = ['mp4', 'webm', 'av1']
file_types = ['pdf', 'doc']


def verify_user_number(user_number):
    if user_number == '' or not user_number.isdigit() or (len(user_number) != 9 or len(user_number) != 11):
        return False
    return True


def verify_username(username):
    if username == '' or len(username) < 4 or username.isdigit():
        return False
    return True


def verify_format(file_format):
    if any(x == file_format.lower() for x in image_types) or any(x == file_format.lower() for x in video_types) \
            or any(x == file_format.lower() for x in file_types):
        return file_format
    return None
