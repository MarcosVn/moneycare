import Vue from 'vue'
import VueResource from 'vue-resource'
import Tabela from './components/Tabela.vue'
import lodash from 'lodash'
Vue.use(VueResource, lodash)
new Vue(Tabela).$mount(".tabela-receita-despesa")