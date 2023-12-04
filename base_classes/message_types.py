from datetime import datetime
import random


durations = ['2:21', '1:42', '0:54', '2:02', '4:54', '3:14', '0:22', '0:37', '0:19']
sizes = ['1920x1080', '1280x720', '1080x1080']


class DefaultMessage(object):

    def __init__(self, **kwargs):
        self.message = kwargs.get('message') or None
        self.date = datetime.now()


class FileMessage(DefaultMessage, object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.memory_use = f"{random.choice(range(1, 100))} MB"
        self.file_format = kwargs.get('file_format')


class VideoMessage(FileMessage, object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.duration = random.choice(durations)


class PhotoMessage(FileMessage, object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_size = random.choice(sizes)
