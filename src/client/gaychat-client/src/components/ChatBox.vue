<template>
  <div id="container">
    <ul id="messages">
      <li v-for="(msg, index) in messages" :key="index">
        {{ msg }}
      </li>
      <form id="form" action="">
        <input id="input" autocomplete="off" /><button>Send</button>
      </form>
    </ul>
    <div id="messages1">
      <a-tooltip placement="right" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="right" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="right" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="right" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
    </div>
    <div id="messages2">
      <a-tooltip placement="left" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="left" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="left" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
      <a-tooltip placement="left" visible="true">
        <template #title>prompt text</template>
        <a-avatar :size="48">
          <template #icon><UserOutlined /></template>
        </a-avatar>
      </a-tooltip>
    </div>
  </div>
</template>

<script>
import { io } from 'socket.io-client'
import { UserOutlined } from '@ant-design/icons-vue'
export default {
  components: { UserOutlined },
  data() {
    return {
      messages: []
    }
  },
  mounted() {
    var socket = io('http://localhost:4000/socket123123')

    var form = document.getElementById('form')
    var input = document.getElementById('input')
    console.log(this.messages)
    console.log(this)
    var that = this
    form.addEventListener('submit', (e) => {
      e.preventDefault()
      if (input.value) {
        socket.emit('chat message', input.value)
        input.value = ''
      }
    })

    socket.on('chat message', (msg) => {
      console.log(msg)
      console.log(that.messages)
      that.messages.push(msg)
    })
  }
}
</script>

<style style='less' scoped>
#container {
  height: 98%;
  width: 78%;
  background-color: #d3adf7;
  position: relative;
  left: 100%;
  transform: translate(-101%, 0);
  top: -97%;
  border-radius: 12px;
  box-shadow: 2px 4px 8px 0px rgba(0, 0, 0, 0.2);
}
body {
  margin: 0;
  padding-bottom: 3rem;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,
    Arial, sans-serif;
}

#form {
  background: rgba(0, 0, 0, 0.15);
  padding: 0.25rem;
  position: relative;
  top: 100%;
  transform: translate(0px, -100%);
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  height: 3rem;
  box-sizing: border-box;
  backdrop-filter: blur(10px);
  border-radius: 12px;
}
#input {
  border: none;
  padding: 0 1rem;
  flex-grow: 1;
  border-radius: 2rem;
  margin: 0.25rem;
}
#input:focus {
  outline: none;
}
#form > button {
  background: #333;
  border: none;
  padding: 0 1rem;
  margin: 0.25rem;
  border-radius: 3px;
  outline: none;
  color: #fff;
}

#messages {
  list-style-type: none;
  height: 100%;
  padding: 0;
}
#messages > li {
  padding: 0.5rem 1rem;
}
#messages > li:nth-child(odd) {
  background: #efefef;
}
#messages1 {
  display: flex;
  flex-direction: column;
  margin: 10px;
  transform: translate(0px, -250%);
}
#messages2 {
  display: flex;
  flex-direction: column;
  margin: 10px;
  transform: translate(95%, -250%);
}
</style>
