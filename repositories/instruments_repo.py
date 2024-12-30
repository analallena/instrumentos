from repositories import file_reader


class Instrument:
    def __init__(self, name, available, minimum):
        self.name = name
        self.available = available
        self.minimum = minimum


class InstrumentsRepository:
    def __init__(self):
        pass

    def get(self):
        instrument_lines = file_reader.read_file('instruments-raffle', 'general-data/instruments.csv')

        instruments = list()

        for instrument_line in instrument_lines:
            instrument = instrument_line.split(',')
            instrument_name = instrument[0].strip()
            instrument_number = instrument[1].strip()
            instrument_minimum = instrument[2].strip()

            instruments.append(Instrument(instrument_name, instrument_number, instrument_minimum))

        return instruments

