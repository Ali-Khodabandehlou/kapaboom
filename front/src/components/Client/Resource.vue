<template>
  <div class="resource container">
    <div class="row">
      <div class="col kborder rounded">
        <div class="rsrc-top">قدرت گروه </div>
        <div class="rsrc-bottom">{{ group.power }}</div>
      </div>
      <div class="col kborder rounded">
        <div class="rsrc-top">شهرت</div>
        <div class="rsrc-bottom">{{ group.reputation }}</div>
      </div>
      <div class="col kborder rounded">
        <div class="rsrc-top">ثروت</div>
        <div class="rsrc-bottom">{{ group.wealth }}</div>
      </div>
    </div>
  </div>

  <div class="resource container">
    <div class="row">
      <div class="col-2 kborder rounded">
        <div class="rsrc-top">AP</div>
        <div class="rsrc-bottom">{{ group.action_point }}</div>
      </div>
      <div class="col">
        <div class="row">
          <div class="col kborder rounded">
            <div class="rsrc-top">سکه</div>
            <div class="rsrc-bottom">{{ group.money }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">آب</div>
            <div class="rsrc-bottom">{{ group.primary_water }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">غذا</div>
            <div class="rsrc-bottom">{{ group.primary_food }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">سوخت</div>
            <div class="rsrc-bottom">{{ group.primary_fuel }}</div>
          </div>
        </div>
        <div class="row">
          <div class="col kborder rounded">
            <div class="rsrc-top">آهن</div>
            <div class="rsrc-bottom">{{ group.secondary_iron }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">مس</div>
            <div class="rsrc-bottom">{{ group.secondary_copper }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">طلا</div>
            <div class="rsrc-bottom">{{ group.secondary_gold }}</div>
          </div>
          <div class="col kborder rounded">
            <div class="rsrc-top">الماس</div>
            <div class="rsrc-bottom">{{ group.secondary_diamond }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resource',
  props: {
    group: Object
  }
}
</script>

<style>
.container {
  margin-top: 20px;
}

.kborder {
  border: 2px solid rgb(0, 90, 82);
  color: rgb(0, 90, 82);
  background-color: rgba(62, 168, 158, 0.45);

  margin: 2px;
}

.rsrc-top {
  font-size: small;
  font-weight: bold;
}

.rsrc-bottom {
  font-size: large;
  font-weight: bold;
}
</style>
