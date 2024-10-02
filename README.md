# MQTT Chess Game Integration

This document provides instructions for setting up and interacting with an MQTT server for a chess game integration. The server allows for sending and receiving messages about the next move in the game.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- MQTT broker (e.g., Mosquitto)

## Running the MQTT Server

To start the MQTT server, navigate to the directory containing the `main.py` file and execute the following command:

```bash
python3 main.py
```

## Subscribing to the MQTT Server

To listen for responses from the MQTT server regarding the chess moves, use the Mosquitto subscription command. Open a new terminal and run:

```bash
mosquitto_sub -h localhost -t chess/next_move_response
```

## Publishing Next Move Request

To send a request to the MQTT server, use the Mosquitto publish command. Below is an example command to publish a request containing the positions of the chess pieces:

```bash
mosquitto_pub -h localhost -t chess/next_move -m "{'white_pieces': {
    'Rook': ['a1', 'h1'],
    'Knight': ['b1', 'g1'],
    'Bishop': ['c1', 'f1'],
    'Queen': 'd1',
    'King': 'e1',
    'Pawn_1': 'a2',
    'Pawn_2': 'b2',
    'Pawn_3': 'c2',
    'Pawn_4': 'd2',
    'Pawn_5': 'e2',
    'Pawn_6': 'f2',
    'Pawn_7': 'g2',
    'Pawn_8': 'h2'
},
'black_pieces': {
    'Rook': ['a8', 'h8'],
    'Knight': ['b8', 'g8'],
    'Bishop': ['c8', 'f8'],
    'Queen': 'd8',
    'King': 'e8',
    'Pawn_1': 'a7',
    'Pawn_2': 'b7',
    'Pawn_3': 'c7',
    'Pawn_4': 'd7',
    'Pawn_5': 'e7',
    'Pawn_6': 'f7',
    'Pawn_7': 'g7',
    'Pawn_8': 'h7'
}}"
```
