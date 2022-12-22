<template>
  <div class="col-7">
    <h5>انتخاب گروه</h5>
    <div v-for="(group, index) in groups" :key="index">
      <div class="form-check">
        <label class="form-check-label" v-bind:for="`flexCheckDefault` + index">
          {{ group.name }}
        </label>
        <input class="form-check-input" type="checkbox" name="flexCheckDefault" v-bind:id="`flexCheckDefault` + index">
      </div>
    </div>
    <div class="form-check gform">
      <button class="btn gbtn">
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor" class="bi bi-plus-square-fill gpath"
          viewBox="0 0 16 16">
          <path
            d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3a.5.5 0 0 1 1 0z" />
        </svg>
      </button>
      <label class="form-check-label glabel" data-bs-toggle="modal" data-bs-target="#addGroupModal">
        افزودن گروه
      </label>
    </div>
    <!-- <div class="form-check gform">
      <button class="btn gbtn">
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor" class="bi bi-dash-square-fill"
          viewBox="0 0 16 16">
          <path
            d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm2.5 7.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1z" />
        </svg>
      </button>
      <label class="form-check-label rglabel">
        حذف گروه ها
      </label>
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'GroupList',
  props: {
    groups: {}
  }
}
</script>

<style>
.gbtn {
  float: right;
  margin: 0px;
  padding: 0px;
  margin-top: 2px !important;
}

.gpath {
  color: white;
  padding: 0px !important;
  margin: 0px !important;
  border: 1px solid gray;
  border-radius: 20%;
  height: 15px;
  width: 15px;
}

.gpath:hover {
  color: rgb(13, 110, 253);
}

.glabel {
  margin-left: 8px;
  color: rgb(45, 124, 116);
}

.rglabel {
  margin-left: 8px;
  color: rgb(187, 49, 49);
}

.glabel:hover {
  cursor: pointer;
  color: rgb(62, 168, 158);
}

.rglabel:hover {
  cursor: pointer;
  color: rgb(233, 79, 79);
}
</style>
