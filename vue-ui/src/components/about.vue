<template>
  <div>
    <el-card title="关于" class="box-card" shadow="hover">
      <el-result icon="success" title="Copyright" subTitle="-----------------------------">
        <template slot="extra">
          <el-form>
            <el-form-item>Vue2.x+ElementUI+Django</el-form-item>
            <el-form-item>作者：<el-tag>palpitate</el-tag><el-tag style="margin-left: 10px">suspect_x</el-tag> from <el-tag>计金（双）200</el-tag></el-form-item>
          </el-form>
        </template>
      </el-result>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'about'
}
</script>

<style scoped>
.box-card {
  width: 80%;
  margin: 20px auto 0;
}
</style>
