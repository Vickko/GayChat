<template>
  <div class="container">
    <div class="blurview"></div>
    <div class="decoration"></div>
    <div class="LoginBox" :style="{ transform: transformData }">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  components: {},
  data() {
    return {
      transformData: ''
    }
  },
  mounted() {
    window.onresize = () => {
      console.log('window resize detected')
      if (window.innerWidth < 500) {
        this.transformData =
          'translate(-' + (window.innerWidth + 320) / 2 + 'px, -50%)'
      } else this.transformData = 'translate(-125%, -50%)'
    }
  },
  watch: {}
}
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  background-image: url(../assets/bg.jpg);
  background-size: cover;
  background-position: center;
  background-color: rgba(0, 0, 0, 0.3);
  background-blend-mode: darken;
}
.blurview {
  width: 100%;
  height: 100%;
  background-image: url(../assets/bg.jpg);
  background-size: cover;
  filter: blur(10px);
  position: absolute;
  background-position: center;
}
.decoration {
  position: absolute;
  width: 60%;
  height: 45%;
  background: rgba(255, 248, 248, 0.7);
  transform: translate(60%, 70%);
  box-shadow: 2px 4px 8px 0px rgba(0, 0, 0, 0.2);
}
.image {
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background-image: url(../assets/bg.jpg);
  position: absolute;
}
.LoginBox {
  width: 40%;
  height: 80%;
  background-color: #ae8ae5;
  position: relative;
  left: 100%;
  top: 50%;
  transform: translate(-125%, -50%);
  box-shadow: 2px 4px 8px 0px rgba(0, 0, 0, 0.2);
  min-width: 320px;
}
</style>
