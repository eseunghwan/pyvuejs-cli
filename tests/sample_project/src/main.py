# -*- coding: utf-8 -*-
from pyvuejs import Vue

class app():
    def data(self):
        return {
            "text": "hello, vue3!"
        }

    def methods(self):
        def change_text(vue):
            vue.text = "changed!"

        return {
            "change_text": change_text
        }

Vue.createApp(Vue.importVue("./app.vue"), app).mount("#main")
