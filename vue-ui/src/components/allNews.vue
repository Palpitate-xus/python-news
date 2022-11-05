<template>
  <div>

    <div class="line"></div>

    <el-card class="box-card"  v-for="o in newsList" :key="o.id" shadow="hover">
      <div slot="header" class="clearfix">
        <span><el-tag size="small">{{ o.author }}  </el-tag>  {{o.title}}</span>
        <el-popconfirm
          confirm-button-text='好的'
          cancel-button-text='不用了'
          icon="el-icon-info"
          icon-color="#409EFF"
          title="减少类似推荐"
          @confirm="handleDelete(o.id)"
        >
          <el-button slot="reference" type="text" style="float: right; padding: 3px 0;margin-right: 10px">不感兴趣</el-button>
        </el-popconfirm>
      </div>
      <div class="text item">
        {{o.content}}
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'allNews',
  data () {
    return {
      activeIndex: '1',
      dialogTableVisible: false,
      newsList: []
    }
  },
  mounted () {
    this.handleTestCors()
    this.handleFetchNews()
  },
  methods: {
    handleTestCors () {
      axios.get('http://localhost:8000/api/test').then((res) => {
        console.log(res)
      })
    },
    async handleFetchNews () {
      let _this = this
      await axios.post('http://localhost:8000/api/get_news', {'id': 200}).then((res) => {
        const dd = res.data
        _this.newsList = dd.data
      })
      console.log(this.newsList)
    },
    async handleDelete (id) {
      await this.$axios({
        method: 'post',
        url: 'http://localhost:8000/api/delete_news',
        data: {
          id: id
        }
      })
      this.handleFetchNews()
    }
  }
}
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.box-card {
  width: 80%;
  margin: 20px auto 0;
}
</style>
