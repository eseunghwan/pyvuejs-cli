# -*- coding: utf-8 -*-
from pyvuejs import Vue

Vue.Router({
    "public": {
        "url": "/public"
    },
    "app": {
        "url": "/app",
        "components": [ "label-box" ]
    }
})
