<template>
  <LoginBox class="LoginBox" />
</template>

<script>
import LoginBox from '@/components/LoginBox'

export default {
  name: 'LoginView',
  components: {
    LoginBox
  }
}
</script>

<style>
.LoginBox {
  width: 80%;
  height: 80%;
  position: relative;
  left: 10%;
  margin-top: 10%;
}
</style>
