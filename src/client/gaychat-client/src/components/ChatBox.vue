<template>
  <div id="container">
    <form id="form" action="">
      <input id="input" autocomplete="off" /><button>Send</button>
    </form>
    <ul id="messages">
      <li v-for="(msg, index) in messages" :key="index">
        {{ msg }}
      </li>
    </ul>

  </div>
</template>

<script>
import { io } from 'socket.io-client'
export default {
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
    form.addEventListener('submit', function(e) {
      e.preventDefault()
      if (input.value) {
        socket.emit('chat message', input.value)
        input.value = ''
      }
    })

    socket.on('chat message', function(msg) {
      console.log(msg)
      console.log(that.messages)
      that.messages.push(msg)
    })
  }
}
</script>

<style style='less' scoped>
#container {
  height: 100%;
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
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  height: 3rem;
  box-sizing: border-box;
  backdrop-filter: blur(10px);
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
  padding: 0;
}
#messages > li {
  padding: 0.5rem 1rem;
}
#messages > li:nth-child(odd) {
  background: #efefef;
}
</style>
