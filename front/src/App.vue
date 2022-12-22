<template>
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <Modals />
  <router-view/>
</template>

<script>
import Modals from '@/components/Modals.vue'

export default {
  components: {
    Modals
  }
}
</script>

<style>
@font-face {
  font-family: 'yekan';
  src: url('./assets/fonts/BYekan.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

body {
  background-color: rgba(231, 255, 253, 0.322) !important;
}

div {
  direction: rtl;
}

#app {
  font-family: yekan, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgb(57, 6, 62);
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: rgb(62, 168, 158);
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
