<template>
  <div class="Box">
    <a-input-search
      v-model:value="value"
      placeholder="input search text"
      :style="{ width: '80%', transform: 'translate(-2%,10px)' }"
      @search="onSearch"
    />
    <a-button
      :style="{
        'font-size': '16px',
        height: '32px',
        width: '32px',
        padding: '0px 0px 0px 0px',
        transform: 'translate(20%,10px)'
      }"
    >
      <PlusOutlined :style="{ color: '#8b8c8c' }" />
    </a-button>
    <div class="dividerWarp">
      <a-divider class="divider" />
      <a-list class="list" item-layout="horizontal" :data-source="data">
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta description="Chat Message">
              <template #title>
                <p>{{ item.title }}</p>
              </template>
              <template #avatar>
                <a-avatar :size="48">
                    <template #icon><UserOutlined /></template>
                </a-avatar>
              </template>
            </a-list-item-meta>
          </a-list-item>
        </template>
      </a-list>
    </div>
  </div>
</template>

<script>
import { PlusOutlined, UserOutlined } from '@ant-design/icons-vue'
import { defineComponent } from 'vue'
const data = [
  {
    title: 'User 1'
  },
  {
    title: 'User 2'
  },
  {
    title: 'User 3'
  },
  {
    title: 'User 4'
  }
]
export default defineComponent({
  components: {
    PlusOutlined,
    UserOutlined
  },
  setup() {
    return {
      data
    }
  }
})
</script>

<style scoped>
.Box {
  width: 20%;
  height: 98%;
  background-color: #ae8ae5;
  position: relative;
  left: 0%;
  top: 0%;
  transform: translate(10px, 1%);
  box-shadow: 2px 4px 8px 0px rgba(0, 0, 0, 0.2);
  min-width: 250px;
  border-radius: 12px;
}
.dividerWarp {
  width: 94%;
}
.divider {
  height: 2px;
  background-color: #d8dad9;
  border: 0px;
  position: relative;
  left: 3%;
  border-radius: 1px;
}
.list {
  position: relative;
  left: 3%;
}
</style>
