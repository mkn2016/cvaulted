<template>
  <div class="pt-2 pb-6 md:py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <h1 class="text-2xl font-semibold text-gray-900">Dashboard</h1>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <!-- Replace with your content -->
      <div class="rows">
        <div class="row" v-if="userRoles.includes('superuser') | userRoles.includes('admin')">
          <div class="grid grid-flow-col grid-cols-4">
            <div class="w-full xl:w-full px-2">
              <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-2 mb-2 xl:mb-0">
                <svg class="w-16 h-16 fill-current mr-4 hidden lg:block pt-3" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>

                <div class="text-gray-700">
                  <p class="font-semibold text-3xl">{{statistics.users_count}}</p>
                  <p>Users</p>
                </div>

              </div>
            </div>
            <div class="w-full xl:w-full px-2">
              <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-2 mb-2 xl:mb-0">
                <svg data-name="Layer 1" class="w-16 h-16 fill-current mr-4 hidden lg:block pt-4" viewBox="0 0 48 48"><path fill="#58565d" d="M22.5,16.5h-7a.5.5,0,0,1,0-1h7a.5.5,0,0,1,0,1Z"/><path fill="#58565d" d="M22.5,27.5h-2A2.50263,2.50263,0,0,1,18,25V7a2.50263,2.50263,0,0,1,2.5-2.5h2a.5.5,0,0,1,0,1h-2A1.50164,1.50164,0,0,0,19,7V25a1.50164,1.50164,0,0,0,1.5,1.5h2a.5.5,0,0,1,0,1Z"/><circle cx="27" cy="27" r="4.5" fill="#37b678"/><path fill="#00a653" d="M23.5,27a4.4847,4.4847,0,0,1,4-4.44958A4.42989,4.42989,0,0,0,27,22.5a4.5,4.5,0,0,0,0,9,4.42989,4.42989,0,0,0,.5-.05042A4.4847,4.4847,0,0,1,23.5,27Z"/><circle cx="27" cy="16" r="4.5" fill="#fdd402"/><path fill="#fbbf13" d="M23.5,16a4.4847,4.4847,0,0,1,4-4.44958A4.42989,4.42989,0,0,0,27,11.5a4.5,4.5,0,0,0,0,9,4.42989,4.42989,0,0,0,.5-.05042A4.4847,4.4847,0,0,1,23.5,16Z"/><circle cx="27" cy="5" r="4.5" fill="#e5303e"/><path fill="#b72732" d="M23.5,5a4.4847,4.4847,0,0,1,4-4.44958A4.42989,4.42989,0,0,0,27,.5a4.5,4.5,0,0,0,0,9,4.42989,4.42989,0,0,0,.5-.05042A4.4847,4.4847,0,0,1,23.5,5Z"/><path fill="#3c3b41" d="M28,7.50013H26a.5.5,0,1,1,0-1h2a.5.5,0,0,1,0,1Z"/><path fill="#3c3b41" d="M27 7.50013a.49971.49971 0 0 1-.5-.5V4.42591l-.10937.13672a.50024.50024 0 1 1-.78125-.625l1-1.25a.50024.50024 0 0 1 .89063.3125v4A.49971.49971 0 0 1 27 7.50013zM28 18.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1zM28 14.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1zM28 16.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1z"/><path fill="#3c3b41" d="M28 16.5a.49971.49971 0 0 1-.5-.5V14a.5.5 0 0 1 1 0v2A.49971.49971 0 0 1 28 16.5zM26 18.5a.49971.49971 0 0 1-.5-.5V16a.5.5 0 0 1 1 0v2A.49971.49971 0 0 1 26 18.5zM28 29.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1zM28 25.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1zM28 27.5H26a.5.5 0 0 1 0-1h2a.5.5 0 0 1 0 1z"/><path fill="#3c3b41" d="M28,29.5a.49971.49971,0,0,1-.5-.5V25a.5.5,0,0,1,1,0v4A.49971.49971,0,0,1,28,29.5Z"/><circle cx="8" cy="16" r="7.5" fill="#4ebaea"/><path fill="#2e99d4" d="M1.5,16a7.49442,7.49442,0,0,1,7-7.47479C8.334,8.51422,8.16882,8.5,8,8.5a7.5,7.5,0,0,0,0,15c.16882,0,.334-.01422.5-.02521A7.49442,7.49442,0,0,1,1.5,16Z"/><circle cx="8" cy="16" r="5.5" fill="#fff"/><path fill="#e0e0e2" d="M3.5,16a5.49864,5.49864,0,0,1,5-5.47479C8.33508,10.51031,8.16882,10.5,8,10.5a5.5,5.5,0,0,0,0,11c.16882,0,.33508-.01031.5-.02521A5.49868,5.49868,0,0,1,3.5,16Z"/><path fill="#58565d" d="M10.25 16.5H9a.5.5 0 0 1 0-1h1.25a.5.5 0 0 1 0 1zM8 15.5a.49971.49971 0 0 1-.5-.5V13.25a.5.5 0 0 1 1 0V15A.49971.49971 0 0 1 8 15.5z"/><circle cx="8" cy="16" r="1" fill="#4ebaea" transform="rotate(-37.84 8 16)"/></svg>
                <div class="text-gray-700">
                  <p class="font-semibold text-3xl">{{statistics.roles_count}}</p>
                  <p>Roles</p>
                </div>

              </div>
            </div>
            <div class="w-full xl:w-full px-2">
              <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-2 mb-2 xl:mb-0">
                <svg class="w-16 h-16 fill-current mr-4 hidden lg:block pt-4" viewBox="0 0 28 28">
                  <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <g id="Rounded" transform="translate(-646.000000, -1484.000000)">
                          <g id="Content" transform="translate(100.000000, 1428.000000)">
                              <g id="-Round-/-Content-/-block" transform="translate(544.000000, 54.000000)">
                                  <g>
                                      <polygon id="Path" points="0 0 24 0 24 24 0 24"></polygon>
                                      <path d="M12,2 C6.48,2 2,6.48 2,12 C2,17.52 6.48,22 12,22 C17.52,22 22,17.52 22,12 C22,6.48 17.52,2 12,2 Z M4,12 C4,7.58 7.58,4 12,4 C13.85,4 15.55,4.63 16.9,5.69 L5.69,16.9 C4.63,15.55 4,13.85 4,12 Z M12,20 C10.15,20 8.45,19.37 7.1,18.31 L18.31,7.1 C19.37,8.45 20,10.15 20,12 C20,16.42 16.42,20 12,20 Z" id="🔹Icon-Color" fill="#1D1D1D"></path>
                                  </g>
                              </g>
                          </g>
                      </g>
                  </g>
              </svg>

                <div class="text-gray-700">
                  <p class="font-semibold text-3xl">7</p>
                  <p>Permissions</p>
                </div>

              </div>
            </div>
            <div class="w-full xl:w-full px-2">
              <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-2 mb-2 xl:mb-0">
                <svg class="w-16 h-16 fill-current mr-4 hidden lg:block pt-4" viewBox="0 0 28 28">
                  <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                      <g id="Rounded" transform="translate(-307.000000, -157.000000)">
                          <g id="Action" transform="translate(100.000000, 100.000000)">
                              <g id="-Round-/-Action-/-account_balance_wallet" transform="translate(204.000000, 54.000000)">
                                  <g>
                                      <polygon id="Path" points="0 0 24 0 24 24 0 24"></polygon>
                                      <path d="M10,16 L10,8 C10,6.9 10.89,6 12,6 L21,6 L21,5 C21,3.9 20.1,3 19,3 L5,3 C3.89,3 3,3.9 3,5 L3,19 C3,20.1 3.89,21 5,21 L19,21 C20.1,21 21,20.1 21,19 L21,18 L12,18 C10.89,18 10,17.1 10,16 Z M13,8 C12.45,8 12,8.45 12,9 L12,15 C12,15.55 12.45,16 13,16 L22,16 L22,8 L13,8 Z M16,13.5 C15.17,13.5 14.5,12.83 14.5,12 C14.5,11.17 15.17,10.5 16,10.5 C16.83,10.5 17.5,11.17 17.5,12 C17.5,12.83 16.83,13.5 16,13.5 Z" id="🔹Icon-Color" fill="#1D1D1D"></path>
                                  </g>
                              </g>
                          </g>
                      </g>
                  </g>
                </svg>

                <div class="text-gray-700">
                  <p class="font-semibold text-3xl">{{statistics.accounts_count}}</p>
                  <p>Accounts</p>
                </div>

              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="py-4">
            <div class="border-4 border-dashed border-gray-200 rounded-lg h-100 flex flex-col">
              <div class="h-5/6">
                <user-table :users="users" :userRoles="userRoles"/>
              </div>
              <div class="h-1/6">
                <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
                  <div class="flex-1 flex justify-between sm:hidden">
                    <a href="#" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                      Previous
                    </a>
                    <a href="#" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                      Next
                    </a>
                  </div>
                  <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                    <div>
                      <p class="text-sm text-gray-700">
                        Showing
                        <span class="font-medium">1</span>
                        to
                        <span class="font-medium">10</span>
                        of
                        <span class="font-medium">97</span>
                        results
                      </p>
                    </div>
                    <div>
                      <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                        <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                          <span class="sr-only">Previous</span>
                          <!-- Heroicon name: solid/chevron-left -->
                          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                          </svg>
                        </a>
                        <!-- Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" -->
                        <a href="#" aria-current="page" class="z-10 bg-indigo-50 border-indigo-500 text-indigo-600 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          1
                        </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          2
                        </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 hidden md:inline-flex relative items-center px-4 py-2 border text-sm font-medium">
                          3
                        </a>
                        <span class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                          ...
                        </span>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 hidden md:inline-flex relative items-center px-4 py-2 border text-sm font-medium">
                          8
                        </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          9
                        </a>
                        <a href="#" class="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium">
                          10
                        </a>
                        <a href="#" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                          <span class="sr-only">Next</span>
                          <!-- Heroicon name: solid/chevron-right -->
                          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                          </svg>
                        </a>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      <!-- /End replace -->
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, computed, onMounted} from 'vue'
import {useStore} from "vuex";
import {map} from "lodash"

import UserTable from "../components/UserTable.vue"

export default defineComponent({
  name: 'Dashboard',
  components: {
    UserTable
  },
  setup() {
    const store = useStore()

    const user = computed(() => store.state.user)
    const users = computed(() => store.state.users)
    const fetchUsers = store.dispatch("fetchUsers")
    const statistics = computed(() => store.state.statistics)
    const fetchStatistics = store.dispatch("fetchStatistics")
    const userRoles = computed(() => map(user.value.roles, "name"))

    onMounted(async () => {
      fetchUsers
      fetchStatistics
    })
    return {
      user,
      users,
      userRoles,
      statistics,
      fetchUsers,
      fetchStatistics
    }
  }
});
</script>