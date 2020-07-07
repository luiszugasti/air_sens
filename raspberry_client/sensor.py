import time
from random import randrange

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import re


# will have to be overwritten with the *actual* query implementation with arduino.
def get_test_payload():
    mq2 = randrange(200, 600)
    mq4 = randrange(200, 600)
    mq5 = randrange(200, 600)
    mq135 = randrange(200, 600)
    # dummy procedure which sends the default payload.
    default_payload = "?" + \
                      "mq2={}".format(mq2) + \
                      "&mq4={}".format(mq4) + \
                      "&mq5={}".format(mq5) + \
                      "&mq135={}".format(mq135)
    return default_payload


def parse_payload(payload: str) -> dict:
    # builds a dict with key: value pairs for all the keys in the get type request.
    exp = re.compile('[?]\w*|[=]\d*|[&]\w*')
    hits = exp.findall(payload)
    try:
        ret = {hits[0].replace("?", ""): int(hits[1].replace("=", ""))}
        for i in range(2, len(hits) - 1, 2):
            ret[hits[i].replace("&", "")] = int(hits[i+1].replace("=", ""))
    except ValueError:
        # usually can take place if we try to parse a non-integer as an integer.
        # if we send an empty payload, then entries won't be logged.
        # However, this means we don't take an input. Logging?
        return {'mq2': " ",
                'mq4': " ",
                'mq5': " ",
                'mq135': " "}
    return ret


def get_test_values():
    # table, then payload entries
    pay = get_test_payload()
    hit = parse_payload(pay)
    val_string = "airtestt,site=kitchen mq2={},mq4={},mq5={},mq135={}"\
        .format(hit['mq2'], hit['mq4'], hit['mq5'], hit['mq135'])
    return val_string


# topic is a reference to a database. The payload contains what table we wish to use.
def pub(client_id, topic="sensors", payload="temp,site=room1 value=123456", qos=0, retain=False,
        hostname="192.168.0.18",
        port=1883, keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp"):
    publish.single(topic, payload, qos, retain, hostname,
                   port, client_id, keepalive, will, auth, tls, protocol, transport)
    print("Sent following payload: \n{}".format(payload))
