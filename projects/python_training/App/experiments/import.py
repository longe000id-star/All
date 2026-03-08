←
←

# flask: Flask  request jsonify
from flask import Flask, request, jsonify

#flask_cors: CORS
from flask_cors import CORS

# agent.emotion_monitor: EmotionMonitorService LanguagePronunciationGuide
from agent.emotion_monitor import EmotionMonitorService, LanguagePronunciationGuide

# agent.translation:
from agent.translation import *

# threading
import threading

# logging
import logging

# time
import time
