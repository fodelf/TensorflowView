import { getProjectType } from '@/api/projectManage'

const state = {
  allSelect: {}
}

const getters = {}

const actions = {
  getAllSelect({ commit }) {
    let reqInfo = {}
    getProjectType(reqInfo).then(res => {
      commit('setAllSelect', res)
    })
  }
}

const mutations = {
  setAllSelect(state, allSelect) {
    state.allSelect = allSelect
  }
}
export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
