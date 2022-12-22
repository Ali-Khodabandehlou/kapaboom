<template>
  <div class="container">
    <!-- Earn Modal -->
    <div class="modal fade" id="earnModal" tabindex="-1" aria-labelledby="earnModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="earnModalLabel">کسب منابع اولیه</h5>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="earnWater" class="col-form-label" style="float: right;">آب:</label>
                <input type="text" class="form-control" id="earnWater" v-model="earnWater">
                <label for="earnFood" class="col-form-label" style="float: right;">غذا:</label>
                <input type="text" class="form-control" id="earnFood" v-model="earnFood">
                <label for="earnFuel" class="col-form-label" style="float: right;">سوخت:</label>
                <input type="text" class="form-control" id="earnFuel" v-model="earnFuel">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal"
             v-on:click="Earn()">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Travel Modal -->
    <div class="modal fade" id="travelModal" tabindex="-1" aria-labelledby="travelModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="travelModalLabel">سفر</h5>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="location" class="col-form-label" style="float: right;">موقعیت:</label>
                <input type="text" class="form-control" id="location" v-model="location">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal"
             v-on:click="Travel()">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Extract Modal -->
    <div class="modal fade" id="extractModal" tabindex="-1" aria-labelledby="extractModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="extractModalLabel">استخراج</h5>
          </div>
          <div class="modal-body">
            استخراج انجام شد.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Discover Modal -->
    <div class="modal fade" id="discoverModal" tabindex="-1" aria-labelledby="discoverModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="discoverModalLabel">اکتشاف</h5>
          </div>
          <div class="modal-body">
            اکتشاف انجام شد.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Trade Modal -->
    <div class="modal fade" id="tradeModal" tabindex="-1" aria-labelledby="tradeModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="tradeModalLabel">مبادله</h5>
          </div>
          <div class="modal-body">
            مبادله انجام شد.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Work Modal -->
    <div class="modal fade" id="workModal" tabindex="-1" aria-labelledby="workModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="workModalLabel">کسب و کار</h5>
          </div>
          <div class="modal-body">
            کسب و کار اعمال شد.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- War Modal -->
    <div class="modal fade" id="warModal" tabindex="-1" aria-labelledby="warModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="warModalLabel">جنگ</h5>
          </div>
          <div class="modal-body">
            جنگ انجام گرفت.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" data-bs-dismiss="modal">تایید</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Group Modal -->
    <div class="modal fade" id="addGroupModal" tabindex="-1" aria-labelledby="addGroupModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" v-on:click="ResetAddGroupModal()"></button>
            <h5 class="modal-title" id="addGroupModalLabel">جنگ</h5>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <div class="text-danger">
                  <p class="kmessage" :hidden="!groupError">گروه با این نام وجود دارد!</p>
                  <p class="kmessage" :hidden="!groupUnknownError">لطفا مجدد تلاش کنید.</p>
                </div>
                <label for="group-name" class="col-form-label" style="float: right;">نام گروه:</label>
                <input type="text" class="form-control" id="group-name" v-model="gName">
                <label for="group-user" class="col-form-label" style="float: right;">نام کاربری:</label>
                <input type="text" class="form-control" id="group-user" v-model="gUser">
                <label for="group-pass" class="col-form-label" style="float: right;">رمز عبور:</label>
                <input type="password" class="form-control" id="group-pass" v-model="gPass">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal" v-on:click="ResetAddGroupModal()">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary" v-on:click="AddGroup()">اضافه کن</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Timer Modal -->
    <div class="modal fade" id="addTimerModal" tabindex="-1" aria-labelledby="addTimerModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <h5 class="modal-title" id="addTimerModalLabel">افزودن تایمر</h5>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="year" class="col-form-label" style="float: right;">سال (دوره):</label>
                <input type="text" class="form-control" id="year" v-model="year">
                <label for="timer" class="col-form-label" style="float: right;">زمان تایمر (به ثانیه):</label>
                <input type="text" class="form-control" id="timer" v-model="timer">
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary kbtn-secondary" data-bs-dismiss="modal">بستن</button>
            <button type="button" class="btn btn-primary kbtn-primary"
              data-bs-dismiss="modal" v-on:click="AddTimer()">افزودن</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'Modals',
  data () {
    return {
      gName: '',
      gUser: '',
      gPass: '',
      groupError: false,
      groupUnknownError: false,
      year: 0,
      timer: 0,
      earnWater: 0,
      earnFood: 0,
      earnFuel: 0,
      location: ''
    }
  },
  methods: {
    AddGroup () {
      const data = {
        groupname: this.gName,
        username: this.gUser,
        password: this.gPass
      }

      kapaAPI.post('group/signup/', data, {
        auth: {
          username: 'alikh93',
          password: 'A_khodaL00'
        }
      }).then((response) => {
        this.ResetAddGroupModal()
        this.$router.go()
      }).catch(error => {
        console.log(error)
        const myError = error.response.data.username[0]
        if (myError === 'user profile with this username already exists.') {
          this.groupError = true
        } else {
          this.groupUnknownError = true
        }
      })
    },
    ResetAddGroupModal () {
      this.groupError = false
      this.groupUnknownError = false
      this.gName = ''
      this.gUser = ''
      this.gPass = ''
    },
    AddTimer () {
      const data = {
        year: this.year,
        timer: this.timer
      }

      kapaAPI.post('timer/add/', data, {
        auth: {
          username: localStorage.getItem('uname'),
          password: localStorage.getItem('upass')
        }
      }).then((response) => {
        this.ResetAddTimerModal()
        this.$router.go()
      }).catch(error => {
        console.log(error)
      })
    },
    ResetAddTimerModal () {
      this.year = ''
      this.timer = ''
    },
    Earn () {
      const data = {
        group_pk: localStorage.getItem('gpk'),
        action_pk: 1,
        water: this.earnWater,
        food: this.earnFood,
        fuel: this.earnFuel
      }

      kapaAPI.post('action/', data, {
        auth: {
          username: localStorage.getItem('uname'),
          password: localStorage.getItem('upass')
        }
      }).then((response) => {
        console.log(response)
        this.$router.go()
      }).catch(error => {
        console.log(error)
      })
    },
    Travel () {
      const data = {
        group_pk: localStorage.getItem('gpk'),
        action_pk: 2,
        destination: this.location
      }

      kapaAPI.post('action/', data, {
        auth: {
          username: localStorage.getItem('uname'),
          password: localStorage.getItem('upass')
        }
      }).then((response) => {
        console.log(response)
        this.$router.go()
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
.modal-content,
.modal-header,
.modal-title,
.modal-body,
.modal-footer {
  background-color: rgb(231, 255, 253) !important;
}

.kbtn-secondary {
  background-color: rgba(229, 154, 255, 0.45) !important;
  border: 2px solid rgb(62, 0, 84) !important;
  color: rgb(62, 0, 84) !important;
}

.kbtn-primary {
  background-color: rgb(62, 168, 158) !important;
  border: 2px solid rgb(57, 6, 62) !important;
  color: rgb(57, 6, 62) !important;
}

.kmessage {
  margin: 5px;
  padding: 0px;
  text-align: right;
}
</style>
