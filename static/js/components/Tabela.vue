<template>
  <div id="exemplo">
    <table class="table table-striped">
      <thead>
        <th><a href="#" @click="sort($event, 'fields.descricao')">Descricao</a></th>
        <th><a href="#" @click="sort($event, 'fields.valor')">Valor</a></th>
        <th><a href="#" @click="sort($event, 'fields.conta')">Conta</a></th>
        <th><a href="#" @click="sort($event, 'fields.data_lancamento')">Data de Lançamento</a></th>
      </thead>
      <tbody>
        <tr v-for="item in lista">
          <td>{{ item.fields.descricao }}</td>
          <td>{{ item.fields.valor }}</td>
          <td>{{ item.fields.conta }}</td>
          <td>{{ item.fields.data_lancamento }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      sortDirection: 'desc',
      lista: []
    }
  },
  mounted() {
    this.$http.get("/core/receita-despesa").then( (req) => this.lista = req.data )
  },
  methods:{
    sort(event, campo){
      event.preventDefault()
      if ( this.sortDirection == "desc" )
      {
          this.sortDirection = "asc"
      }else{
        this.sortDirection = "desc"
      }
      this.lista = _.orderBy(this.lista, campo, this.sortDirection)
    }
  }
}
</script>
<style>
</style>