<template>
  <div class="kinfo rounded">
    <div class="d-flex align-items-center">
      <div class="container">
        <div class="row">
          <div class="col">
            <i class="bi bi-arrow-clockwise"></i>
            <p class="kinfo-p">{{ year }}</p>
          </div>
          <div class="col">
            <i class="bi bi-hourglass-split"></i>
            <p class="kinfo-p">{{ timer }}</p>
          </div>
          <div class="col" style="margin-top: -15px;">
            <img id="info-img" src="@/assets/techs/hamdel.png">
          </div>
          <div class="col">
            <p class="kinfo-p kp">{{ group.location }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'Info',
  data () {
    return {
      timer: 0,
      year: 0
    }
  },
  props: {
    group: {}
  },
  methods: {
    getTimer () {
      kapaAPI.get('timer/').then(
        (response) => {
          this.year = response.data.year
          this.timer = response.data.timer.timer
        }).catch(error => {
        console.log(error)
      })
    }
  },
  beforeMount () {
  //   this.getTimer()
  }
}
</script>

<style>
.kinfo {
  margin: 3px;
  margin-top: 20px;

  font-weight: bold;
  color: rgb(57, 6, 62);

  box-shadow: 1px 6px 6px rgba(57, 6, 62, 0.2);
  border: 2px solid rgb(57, 6, 62);
  background-color: rgb(62, 168, 158);
}

i {
  margin: 10px;
}

.kinfo-p {
  padding: 0px;
}

.kp {
  margin-top: 10px;
}

#info-img {
  margin-top: 1vh;
  width: 50px;
  height: auto;
}
</style>
