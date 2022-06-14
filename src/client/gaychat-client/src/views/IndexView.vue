<template>
  <a-layout
    :style="{
      height: '100%',
      'background-color': '#b37feb'
    }"
  >
    <a-layout-sider :defaultCollapsed="true" theme="light" :style="{
      'background-color': '#fff'
    }">
      <a-menu
        v-model:selectedKeys="selectedKeys"
        mode="inline"
        :inline-collapsed="true"
        style="width: 80px"
      >
        <a-menu-item key="1" title="">
          <pie-chart-outlined />
        </a-menu-item>
        <a-menu-item key="2" title="">
          <desktop-outlined />
        </a-menu-item>
        <a-menu-item key="9" title="">
          <file-outlined />
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
      <a-layout-content
        :style="{
          margin: '10px 10px 10px 10px',
          width: '100%',
          'border-radius': '20px',
          'background-color': '#efdbff'
        }"
      >
        <router-view />
      </a-layout-content>
  </a-layout>
</template>
<script>
import {
  PieChartOutlined,
  DesktopOutlined,
  FileOutlined
} from '@ant-design/icons-vue'
import { defineComponent, ref } from 'vue'
export default defineComponent({
  components: {
    PieChartOutlined,
    DesktopOutlined,
    FileOutlined
  },

  data() {
    return {
      collapsed: ref(false),
      selectedKeys: ref(['1'])
    }
  }
})
</script>
<style>
</style>
