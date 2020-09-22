import pysine2 as pysine
from time import sleep
# 349.228 Hz, 440 Hz, 698.46 Hz

F4 = 349.228
A4 = 440.000
F5 = 698.460
A5 = 880.000
F6 = 1396.91
A6 = 1760.00
F7 = 2793.83

duration = 0.15

error_tone = F5


def connection_success():
    sine1 = pysine.PySine()
    sine1.sine(frequency=F4, duration=duration)
    sine1.sine(frequency=A4, duration=duration)
    sine1.sine(frequency=F5, duration=duration)
    sine1.save("output/success1.wav")
    sleep(2)

    sine2 = pysine.PySine()
    sine2.sine(frequency=F5, duration=duration)
    sine2.sine(frequency=A5, duration=duration)
    sine2.sine(frequency=F6, duration=duration)
    sine2.save("output/success2.wav")

    sleep(2)
    sine3 = pysine.PySine()
    sine3.sine(frequency=F6, duration=duration)
    sine3.sine(frequency=A6, duration=duration)
    sine3.sine(frequency=F7, duration=duration)
    sine3.save('output/success3.wav')


def connection_failed(filename, error_repeats, duration):
    s = pysine.PySine()

    for i in range(0, error_repeats):
        s.sine(frequency=error_tone, duration=duration)
        s.sine(frequency=0, duration=duration)
    s.save(filename)


def sos():
    s = pysine.PySine()
    t_unit = 0.1

    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=3*t_unit)

    s.sine(frequency=error_tone, duration=3*t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=3*t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=3*t_unit)
    s.sine(frequency=0, duration=3*t_unit)

    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=t_unit)
    s.sine(frequency=error_tone, duration=t_unit)
    s.sine(frequency=0, duration=7*t_unit)
    s.save("output/sos.wav")


def main():

    sleep(1)
    connection_success()

    sleep(2)
    connection_failed("output/failure1.wav", 8, 0.1)

    sleep(2)
    connection_failed("output/failure2.wav", 4, 0.25)

    sleep(2)
    sos()


if __name__ == "__main__":
    main()
