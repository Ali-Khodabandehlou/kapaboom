<template>
  <div class="loginc">
    <div class="container">
      <div class="row">
        <div class="col">
          <img src="@/assets/logo.png" class="login-logo" />
          <h2 class="kboom">کاپابوم</h2>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <div class="text-danger">
            <p class="kmessage" :hidden="!loginUsername">نام کاربری وارد شده اشتباه است.</p>
            <!-- <p class="kmessage" :hidden="!loginPassword">رمز وارد شده اشتباه است.</p> -->
            <p class="kmessage" :hidden="!groupUnknownError">لطفا مجدد تلاش کنید.</p>
          </div>
          <label for="group-name" class="col-form-label" style="float: right;">نام گروه:</label>
          <input type="text" class="form-control" id="group-name" v-model="lgName">
          <label for="group-pass" class="col-form-label" style="float: right;">رمز عبور:</label>
          <input type="password" class="form-control" id="group-pass" v-model="lgPass">
          <button class="btn w-100 cloginbtn" v-on:click="Login()">ورود</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { kapaAPI } from '@/plugins/axios.js'

export default {
  name: 'LoginClient',
  data () {
    return {
      lgName: '',
      lgPass: '',
      loginUsername: false,
      // loginPassword: false,
      groupUnknownError: false
    }
  },
  methods: {
    Login () {
      this.ResetLoginData()

      const data = {
        username: this.lgName,
        password: this.lgPass
      }
      kapaAPI.post(
        'login/', data
      ).then((response) => {
        localStorage.setItem('uname', this.lgName)
        localStorage.setItem('upass', this.lgPass)
        const type = response.data.type
        localStorage.setItem('utype', type)

        if (type === 'admin') {
          this.$router.push({
            name: 'Manager'
          })
        } else if (type === 'gov') {
          this.$router.push({
            name: 'GovHome'
          })
        } else {
          localStorage.setItem('gpk', response.data.group_pk)
          this.$router.push({
            path: 'client/'
          })
        }
      }).catch(error => {
        const myError = error.response.data.detail
        if (myError === 'username does not exist') {
          this.loginUsername = true
        // } else if (myError === 'Wrong password') {
        //   this.loginPassword = true
        } else {
          this.groupUnknownError = true
        }
      })
    },
    ResetLoginData () {
      this.loginUsername = false
      this.loginPassword = false
      this.groupUnknownError = false
    }
  }
}
</script>

<style>
.loginc {
  margin-top: 15vh;
}

.login-logo {
  height: 60px;
  width: auto;
}

.kboom{
  margin-top: 15px;
  margin-bottom: 5vh;

  font-weight: bolder;
}

#group-name, #group-pass {
  text-align: center;
}

.cloginbtn {
  color: white;
  background-color: rgb(229, 154, 255);
  border: 2px solid rgb(57, 6, 62);

  margin-top: 5vh;
  font-size: larger !important;
}
</style>
