<template>
    <div id="app">
        <p>{{ text }}</p>
        <button v-on:click="change_text">change text</button>
        <br>
        <label-box label="I'm component!"></label-box>
    </div>
</template>

<style>
div#app {
    width: 100%;
    height:100%;
}
</style>
