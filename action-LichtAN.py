#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paho.mqtt.publish as publish
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

SITE = "default"
SOUNDFILE = "./LichtAN.wav"
binaryFile = open(SOUNDFILE, mode='rb')
wav = bytearray(binaryFile.read())

def intent_callback_LichtAN(hermes, intentMessage):
    result_sentence = "OK. Licht ist eingeschaltet."
    current_session_id = intentMessage.session_id
    publish.single("hermes/audioServer/{}/playBytes/whateverId".format(SITE),payload=wav, hostname="localhost", client_id="")
    #hermes.publish_end_session(current_session_id, result_sentence)    


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("studger:LichtAN", intent_callback_LichtAN)
        h.start()
