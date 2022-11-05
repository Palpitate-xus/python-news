<template>
  <div>

    <div class="line"></div>

    <el-card class="box-card"  v-for="o in digestList" :key="o.id" shadow="hover">
      <div slot="header" class="clearfix">
        <span>{{o.author}}</span>
      </div>
      <div class="text item">
        {{o.words}}
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'digest',
  data () {
    return {
      activeIndex: '1',
      digestList: []
    }
  },
  mounted () {
    this.handleTestCors()
    this.handleFetchDigest()
  },
  methods: {
    handleTestCors () {
      axios.get('http://localhost:8000/api/test').then((res) => {
        console.log(res)
      })
    },
    async handleFetchDigest () {
      let _this = this
      await axios.post('http://localhost:8000/api/get_digest', {'id': 200}).then((res) => {
        const dd = res.data
        _this.digestList = dd.data
      })
      console.log(this.digestList)
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
