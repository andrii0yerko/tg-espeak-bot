from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ESpeakConfig:
    amplitude: int = None  # 0..200
    pitch: int = None  # 0..99
    speed: int = None  # words / min
    word_gap: int = None  # units of 10mS at the default speed

    def __iter__(self):
        args = []
        if self.amplitude is not None:
            args.append("-a")
            args.append(str(self.amplitude))

        if self.pitch is not None:
            args.append("-p")
            args.append(str(self.pitch))

        if self.speed is not None:
            args.append("-s")
            args.append(str(self.speed))

        if self.word_gap is not None:
            args.append("-q")
            args.append(str(self.word_gap))

        for i in args:
            yield i


espeak_conf = ESpeakConfig(speed=150, pitch=50, amplitude=100)
espeak_conf_low = ESpeakConfig(speed=130, pitch=0, amplitude=200)
