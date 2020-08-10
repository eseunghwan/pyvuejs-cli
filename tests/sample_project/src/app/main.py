# -*- coding: utf-8 -*-
from pyvuejs import Vue

class app():
    def data(self):
        return {
            "text": "hello, pyvuejs!"
        }

    def methods(self):
        def change_text(self):
            self.text = "I'm changed!"

        return {
            "change_text": change_text
        }

__export__ = Vue.createApp(app).mount("#app")
