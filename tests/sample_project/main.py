# -*- coding: utf-8 -*-
import os
from pyvuejs import Server

Server(os.path.dirname(os.path.abspath(__file__))).start()
