<template>
  <div class="home">
    <h1 style="margin-top:20px">گروه {{ group.name }}</h1>
    <Info :group="group" />
    <Resource :group="group" />
    <Alerts hidden />
    <Actions />
  </div>
</template>

<script>
// @ is an alias to /src
import Actions from '@/components/Client/Actions.vue'
import Alerts from '@/components/Client/Alerts.vue'
import Info from '@/components/Client/Info.vue'
import Resource from '@/components/Client/Resource.vue'
import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'ClientHome',
  components: {
    Actions,
    Alerts,
    Info,
    Resource
  },
  data () {
    return {
      group: {
      }
    }
  },
  methods: {
    checkUser () {
      const type = localStorage.getItem('utype')
      if (type !== 'client') {
        this.$router.push({
          name: 'Login'
        })
      }
    },
    getUserInfo () {
      const data = {
        gpk: localStorage.getItem('gpk')
      }
      const auth = {
        username: localStorage.getItem('uname'),
        password: localStorage.getItem('upass')
      }
      kapaAPI.post('group/detail/', data, {
        auth: auth
      }).then(
        (response) => {
          this.group = response.data
          console.log(this.group)
        }
      ).catch(error => {
        console.log(error)
      })
    }
  },
  beforeMount () {
    this.checkUser()
    this.getUserInfo()
  }
}
</script>

<style>
h1 {
  font-family: yekan;
  font-weight: bolder !important;
}
</style>
