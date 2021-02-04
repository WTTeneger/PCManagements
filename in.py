#!/usr/bin/env python
"""
Author: WTTeneger (https://github.com/WTTeneger)
"""


from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify
import datetime
import sqlite3
import pymysql
import time
import string
import random

from soundtest import Sound # будем использовать статические функции класса Sound
from keyb import Keyboard

"""
Sound.mute() # убрали звук
Sound.volume_max() # Наоборот, прибавили на максимум
cur = Sound.current_volume() # получили текущие настройки
vol = int(input("Введите громкость звука в единицах (0..100): ")) # получим громкость от пользователя
Sound.volume_set(vol) # установим пользовательскую громкость
Sound.volume_up() # увеличим громкость на 2 единицы (проценты говорить неправильно)
Sound.volume_down() # уменьшим громкость на 2 единицы

"""
application = Flask(__name__)

@application.route('/')
def index():
  return render_template('main.html')


@application.route('/ClockBut/<string:token>', methods=["POST","GET"])
def ClockBut(token):
  """The function of processing the pressed button on the server
  Args:
      token (str): accepts the name of the pressed button
  """
  if(token == 'Left'):
    Keyboard.key(Keyboard.VK_MEDIA_PREV_TRACK)
  elif(token == 'Right'):
    Keyboard.key(Keyboard.VK_MEDIA_NEXT_TRACK)
  elif(token == 'SS'):
    Keyboard.key(Keyboard.VK_MEDIA_PLAY_PAUSE)
  elif('Volumes' in token):
    Vol = int(str(token).replace('Volumes',''))
    Sound.volume_set(Vol, 0)
  
 
  data = {
    'static': 'true',
    'code': token
  }
  return(jsonify(data))


if __name__=="__main__":
    application.run(host='192.168.3.2', port='8000', debug=True, threaded=True)
