<template>
  <div class="kalert rounded">
    <div class="d-flex align-items-center">
      <i class="bi bi-exclamation-square"></i>
      <div>
        <p>زلزله در منطقه شما (g7)!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Alerts'
}
</script>

<style>
.kalert {
  margin: 3px;
  margin-top: 20px;

  font-weight: bold;
  color: rgb(57, 6, 62);

  box-shadow: 1px 6px 6px rgba(57, 6, 62, 0.2);
  border: 2px solid rgb(57, 6, 62);
  background-color: rgb(255, 132, 204);
}

i {
  margin: auto 10px;
}

p {
  padding-top: 15px;
}
</style>
