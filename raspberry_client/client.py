from importlib import import_module
import os
import time
import arduinosensor
def main():
    # open defined client
    start_time = time.time()
    while True:
        reading = arduinosensor.get_values(os.environ.get('PORT', "/dev/ttyUSB0"))
        arduinosensor.pub("python_client", payload=reading)
        time.sleep(10.0 - ((time.time() - start_time) % 10.0))


if __name__ == "__main__":
    main()
