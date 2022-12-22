<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="row">
          <button type="button" class="btn kbtn col"
           data-bs-toggle="modal" data-bs-target="#earnModal"
           v-bind:id="actions.kasb.pk">{{ actions.kasb.title_fa }}</button>
          <button type="button" class="btn kbtn col"
           data-bs-toggle="modal" data-bs-target="#travelModal"
           v-bind:id="actions.safar.pk">{{ actions.safar.title_fa }}</button>
          <button type="button" class="btn kbtn col offset-3"
           data-bs-toggle="modal" data-bs-target="#extractModal"
           v-bind:id="actions.estekhraj.pk">{{ actions.estekhraj.title_fa }}</button>
        </div>
        <div class="row">
          <button type="button" class="btn kbtn col" hidden
           data-bs-toggle="modal" data-bs-target="#discoverModal"
           v-bind:id="actions.kasb.pk">{{ actions.kasb.title_fa }}</button>
          <button type="button" class="btn kbtn col"  hidden
           data-bs-toggle="modal" data-bs-target="#tradeModal"
           v-bind:id="actions.kasb.pk">{{ actions.kasb.title_fa }}</button>
          <button type="button" class="btn kbtn col" hidden
           data-bs-toggle="modal" data-bs-target="#workModal"
           v-bind:id="actions.kasb.pk">{{ actions.kasb.title_fa }}</button>
          <button type="button" class="btn kbtn col" hidden
           data-bs-toggle="modal" data-bs-target="#warModal"
           v-bind:id="actions.kasb.pk">{{ actions.kasb.title_fa }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'Actions',
  data () {
    return {
      actions: {
        kasb: {},
        safar: {},
        estekhraj: {}
      }
    }
  },
  methods: {
    getActions () {
      kapaAPI.get('action/list/').then((response) => {
        this.actions.kasb = response.data.kasb
        this.actions.safar = response.data.safar
        this.actions.estekhraj = response.data.estekhraj
      }).catch(error => {
        console.log(error)
      })
    }
  },
  beforeMount () {
    this.getActions()
  }
}
</script>

<style>
.kbtn {
  height: 70px;
  margin: 3px;

  color: rgb(62, 0, 84) !important;
  border: 2px solid rgb(62, 0, 84) !important;
  background-color: rgba(229, 154, 255, 0.45) !important;

  font-size: small !important;
  font-weight: bold !important;
}
</style>
