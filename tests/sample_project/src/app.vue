<template>
    <div id="main">
        <p>{{ text }}</p>
        <button v-on:click="change_text">change text</button>
        <label-box text1 = "123412341234"></label-box>
    </div>
</template>

<style>
div#main {
    width: 100%;
    height:100%;
    padding: 10px;
}
</style>
