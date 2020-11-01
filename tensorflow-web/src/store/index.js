import Vue from 'vue'
import Vuex from 'vuex'
import select from './modules/select.js'
Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    select
  },
  strict: debug
})
