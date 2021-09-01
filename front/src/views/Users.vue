<template>
  <div class="pt-2 pb-6 md:py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <h1 class="text-2xl font-semibold text-gray-900">Users</h1>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <!-- Replace with your content -->
      <div class="py-4">
        <div class="border-4 border-dashed border-gray-200 rounded-lg h-96">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Name
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Status
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Role
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Member Since
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="user in users"
                :key="user.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <img class="h-10 w-10 rounded-full" src="../assets/user.png" alt="">
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        {{user.username}}
                      </div>
                      <div class="text-sm text-gray-500">
                        {{user.email}}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="inline-flex items-center justify-center px-2 py-1 mr-2 text-xs font-bold leading-none bg-green-100 text-green-800 rounded-full" v-if="user.is_active">Active</span>
                  <span class="inline-flex items-center justify-center px-2 py-1 mr-2 text-xs font-bold leading-none text-red-100 bg-red-600 rounded-full" v-else>suspended</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  <span class="text-sm font-medium text-gray-900" v-if="Array.isArray(user.roles) && user.roles.length !== 0">{{[...user.roles.map((val) => val.name)].toString()}}</span>
                  <span class="text-sm font-medium text-gray-900" v-else>---No Roles Yet---</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="text-sm font-medium text-gray-900">
                    {{ $moment(user.created).format("LLL") }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900" v-if="roles.includes('superuser') | roles.includes('admin')">Edit</a>
                </td>
              </tr>
              <!-- More people... -->
            </tbody>
          </table>
        </div>
      </div>
      <!-- /End replace -->
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent, computed, onMounted} from 'vue'
import {useStore} from "vuex";
import {map} from "lodash"

export default defineComponent({
  name: 'Users',
  components: {
  },
  setup() {
    const store = useStore()

    const user = computed(() => store.state.user)
    const users = computed(() => store.state.users)
    const fetchUsers = store.dispatch("fetchUsers")
    const roles = computed(() => map(user.value.roles, "name"))

    onMounted(async () => {
      fetchUsers
    })
    return {
      user,
      users,
      roles,
      fetchUsers
    }
  }
});
</script>
