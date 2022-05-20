<template>
  <div id="components-form-demo-normal-login">
    <a-button
      type=""
      html-type="submit"
      class="test-button"
      size="large"
      @click="testlogin"
    >
      test
    </a-button>
    <a-form
      :model="formState"
      name="normal_login"
      class="login-form"
      @finish="onFinish"
      @finishFailed="onFinishFailed"
    >
      <a-form-item
        name="username"
        :rules="[{ required: true, message: '请输入用户名' }]"
      >
        <a-input
          v-model:value="formState.username"
          placeholder="用户名"
          size="large"
          id="username"
        >
          <template #prefix>
            <UserOutlined
              class="site-form-item-icon"
              style="color: rgba(0, 0, 0, 0.25)"
            />
          </template>
        </a-input>
      </a-form-item>

      <br />
      <a-form-item
        name="password"
        :rules="[{ required: true, message: '请输入密码' }]"
      >
        <a-input-password
          v-model:value="formState.password"
          placeholder="密码"
          size="large"
        >
          <template #prefix>
            <LockOutlined
              class="site-form-item-icon"
              style="color: rgba(0, 0, 0, 0.25)"
            />
          </template>
        </a-input-password>
      </a-form-item>
      <br />
      <br />

      <a-form-item id="remember">
        <div class="login-form-wrap">
          <a-checkbox v-model:checked="formState.remember">记住我</a-checkbox>
          <a-button
            :disabled="disabled"
            type="primary"
            html-type="submit"
            class="login-form-button"
            size="large"
          >
            登录
          </a-button>
        </div>
      </a-form-item>
      <br />
      <div class="login-form-wrap">
        <router-link class="login-form-forgot" to="/forgetPasswd"
          >忘记密码？</router-link
        >
        <router-link to="/signUp">注册</router-link>
      </div>
    </a-form>
  </div>
</template>

<script>
import { defineComponent, reactive, computed } from 'vue'
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'
import axios from 'axios'

import router from '../router'

export default defineComponent({
  components: {
    UserOutlined,
    LockOutlined
  },
  setup() {
    const formState = reactive({
      username: '',
      password: '',
      remember: false
    })

    const testlogin = () => {
      message.info('test button touched, sending request to {{url}}/api/develop/testlogin')
      axios
        .post('/api/develop/testlogin', { username: 'user', passwd: 'passwd' })
        .then((response) => {
          console.log(response.data)
          /* if (
            response.data.meta.status === undefined ||
            !response.data.meta.msg ||
            !response.data.data.token ||
            !response.data.data.id
          )  */
          try {
            if (response.data.data.token && response.data.meta.status === 200) {
              message.success('login success')
              // TODO: sessionStorage
              router.push('/index')
            } else message.error('response not right')
          } catch (err) {
            message.error('response not right, refuse jumping')
          }
        })
    }

    const onFinish = (values) => {
      console.log('Success:', values)
      router.push('/')
    }

    const onFinishFailed = (errorInfo) => {
      console.log('Failed:', errorInfo)
    }

    const disabled = computed(() => {
      return !(formState.username && formState.password)
    })
    return {
      testlogin,
      formState,
      onFinish,
      onFinishFailed,
      disabled
    }
  }
})
</script>

<style scoped style="less">
.test-button {
  position: absolute;
  top: 1%;
}
#components-form-demo-normal-login .login-form {
  width: 80%;
  position: relative;
  left: 10%;
  transform: translate(0%, 50%);
}
#components-form-demo-normal-login .login-form-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
#components-form-demo-normal-login .login-form-button {
  width: 56%;
}
</style>
