import os.path


class Instrument:
    def __init__(self, name):
        self.name = name
        self.available = True


class InstrumentsRepository:
    cursos_file = '../s3_bucket_data/instruments.csv'

    def __init__(self):
        pass

    def get(self):

        main_path = os.path.dirname(__file__)
        file_path = os.path.join(main_path, self.cursos_file)

        with open(file_path) as f:
            instrument_lines = f.readlines()
            instrument_lines.pop(0)
        instruments = list()

        for instrument_line in instrument_lines:
            instrument = instrument_line.split(',')
            instrument_name = instrument[0].strip()

            for rep in range(0, int(instrument[1].strip())):
                instruments.append(Instrument(instrument_name))

        return instruments

