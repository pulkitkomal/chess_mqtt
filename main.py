from services.mqtt_service import MQTT

mqtt_obj = MQTT(service_type='CHESS_ENGINE')
mqtt_obj.run()