# Babylist Technical Exercise

Technical Exercise for Babylist

Prerequisites: Python 3.6+

Installation:

pip -r requirements.txt

Run tests:

pytest

Design:

This object was designed not be thread-safe because it's not logical for multiple "Dealers" to be shuffling or dealing the same deck.