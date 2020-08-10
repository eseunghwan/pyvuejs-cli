# -*- coding: utf-8 -*-
from pyvuejs import Vue


class component():
    props = [ "label" ]
    template = "<label>{{ label }}</label>"

__export__ = Vue.component("label-box", component)
