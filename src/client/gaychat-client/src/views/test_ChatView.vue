<template>
  <div class="container">
    <FriendList />
    <ChatBox />
  </div>
</template>

<script>
import FriendList from '@/components/FriendList'
import ChatBox from '@/components/ChatBox'
export default {
  components: {
    FriendList,
    ChatBox
  }
}
</script>

<style scoped>
.container{
    height: 100%;
    width: 100%;
}
</style>
