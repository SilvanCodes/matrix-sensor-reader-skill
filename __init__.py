from mycroft import MycroftSkill, intent_file_handler


class MatrixSensorReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.sensor.matrix.intent')
    def handle_reader_sensor_matrix(self, message):
        self.speak_dialog('reader.sensor.matrix')


def create_skill():
    return MatrixSensorReader()

