<template>
  <div class="col">
    <button type="button" class="btn kbtn col-12"
      data-bs-toggle="modal" data-bs-target="#addTimerModal"
      >افزودن تایمر</button>
    <button type="button" class="btn kbtn col-12">شروع دهه جدید</button>
    <button type="button" class="btn kbtn col-12">نگه داشتن بازی</button>
    <button type="button" class="btn kbtn col-12">اتمام دهه</button>
    <button type="button" class="btn kbtn col-12">بلایای طبیعی</button>
  </div>
</template>

<script>
export default {
  name: 'Actions'
}
</script>

<style>
.kbtn {
  background-color: rgb(229, 154, 255) !important;
  border: 2px solid rgb(62, 0, 84) !important;
  color: rgb(62, 0, 84) !important;

  margin-bottom: 5px;
  font-size: large;
  padding-top: 15px !important;
  padding-bottom: 15px !important;
}
</style>
