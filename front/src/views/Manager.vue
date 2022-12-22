<template>
  <div class="container">
    <h1>مدیر</h1>
    <br/>
    <div class="row">
      <div class="col col-actions rounded">
        <div class="row justify-content-around">
          <GroupList :groups="groups" />
          <Actions />
        </div>
      </div>
      <div class="col col-table">
        <DataTable />
      </div>
    </div>
  </div>
</template>

<script>
import Actions from '@/components/Manager/Actions.vue'
import DataTable from '@/components/Manager/DataTable.vue'
import GroupList from '@/components/Manager/GroupList.vue'

import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'Manager',
  components: {
    Actions,
    DataTable,
    GroupList
  },
  data () {
    return {
      groups: {}
    }
  },
  methods: {
    loadGroups () {
      const authData = {
        username: 'alikh93',
        password: 'A_khodaL00'
      }
      kapaAPI.get('group/list/', {
        auth: authData
      }).then((response) => {
        console.log(response.data)
        this.groups = response.data
      })
    }
  },
  beforeMount () {
    this.loadGroups()
  }
}
</script>

<style>
.col {
  margin: 5px;
}

.col-actions {
  background-color: rgba(62, 168, 158, 0.45);
  border: 2px solid rgb(62, 168, 158);

  padding: 20px;
}

.form-check-input {
  float: right !important;
}
</style>
