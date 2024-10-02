import paho.mqtt.client as mqtt
import json
from services.openai_service import OPENAI
from services.chess_engine import CHESSENGINE

class MQTT:
    def __init__(self, service_type=None):
        self.client = mqtt.Client()
        self.openai = OPENAI()
        self.chessengine = CHESSENGINE()
        self.service_type = service_type

    def on_message_openai(self, client, userdata, message):
        response = self.openai.call_openai(prompt=message.payload.decode())
        client.publish("chess/next_move_response", json.dumps({'data': response}))
    
    def on_message_chessengine(self, client, userdata, message):
        jsonify_data = self.chessengine.get_black_pieces(chessboard_str=message.payload.decode())
        response = self.chessengine.next_best_move(black_pieces=jsonify_data)
        client.publish("chess/next_move_response", json.dumps({'data': response}))

    def run(self):
        if self.service_type == 'OPENAI':
            self.client.on_message = self.on_message_openai
        elif self.service_type == 'CHESS_ENGINE':
            self.client.on_message = self.on_message_chessengine
        else:
            raise Exception("Service not defined")
        # Connect to the MQTT broker
        self.client.connect("localhost", 1883, 60)
        # Subscribe to the topic
        self.client.subscribe("chess/next_move")
        # Start the loop
        self.client.loop_forever()