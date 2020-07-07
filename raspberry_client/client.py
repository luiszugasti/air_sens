from importlib import import_module
import os
import time

if os.environ.get('SENSOR'):
    Sensor = import_module('sensor_' + os.environ['SENSOR']).Sensor
else:
    import sensor


def main():
    # open defined client
    start_time = time.time()
    while True:
        reading = sensor.get_test_values()
        sensor.pub("test", payload=reading)
        time.sleep(10.0 - ((time.time() - start_time) % 10.0))


if __name__ == "__main__":
    main()
