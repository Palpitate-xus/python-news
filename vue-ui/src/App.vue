<template>
  <div id="app">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
      <el-menu-item index="/">首页</el-menu-item>
      <el-menu-item index="digest">摘要</el-menu-item>
      <el-menu-item index="all">所有新闻</el-menu-item>
      <el-menu-item index="huanqiu">环球网</el-menu-item>
      <el-menu-item index="netease">网易新闻</el-menu-item>
      <el-menu-item index="papernews">澎湃新闻</el-menu-item>
      <el-menu-item index="peopledaily">人民日报</el-menu-item>
      <el-menu-item index="tencent">腾讯新闻</el-menu-item>
      <el-menu-item index="sohu">搜狐新闻</el-menu-item>
      <!--      <el-submenu index="2">-->
      <!--        <template slot="title">我的工作台</template>-->
      <!--        <el-menu-item index="2-1">选项1</el-menu-item>-->
      <!--        <el-menu-item index="2-2">选项2</el-menu-item>-->
      <!--        <el-menu-item index="2-3">选项3</el-menu-item>-->
      <!--        <el-submenu index="2-4">-->
      <!--          <template slot="title">选项4</template>-->
      <!--          <el-menu-item index="2-4-1">选项1</el-menu-item>-->
      <!--          <el-menu-item index="2-4-2">选项2</el-menu-item>-->
      <!--          <el-menu-item index="2-4-3">选项3</el-menu-item>-->
      <!--        </el-submenu>-->
      <!--      </el-submenu>-->
      <el-menu-item index="about">关于</el-menu-item>
    </el-menu>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      if (key === 1) {
        this.$router.push('/')
      }
      if (key === 2) {
        this.$router.push('/digest')
      }
      if (key === 3) {
        this.$router.push('/all')
      }
      if (key === 4) {
        this.$router.push('/huanqiu')
      }
      if (key === 5) {
        this.$router.push('/netease')
      }
      if (key === 6) {
        this.$router.push('/papernews')
      }
      if (key === 7) {
        this.$router.push('/peopledaily')
      }
      if (key === 8) {
        this.$router.push('/tencent')
      }
      if (key === 9) {
        this.$router.push('/sohu')
      }
      if (key === 10) {
        this.$router.push('/about')
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
