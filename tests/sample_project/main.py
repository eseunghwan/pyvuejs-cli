# -*- coding: utf-8 -*-
import os
from pyvuejs import Vue

Vue.init(os.path.dirname(os.path.abspath(__file__))).start_standalone()
