<template>
  <div class="pt-2 pb-6 md:py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <div class="flex flex-column justify-between">
        <h1 class="text-2xl font-semibold text-gray-900">Roles</h1>
        <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
        Create Role
      </button>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
      <!-- Replace with your content -->
      <div class="py-4">
        <div class="border-4 border-dashed border-gray-200 rounded-lg h-96">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Role
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Created
                </th>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Updated
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="role in roles"
                :key="role.id">
                <td class="px-6 py-4 text-sm text-gray-500">
                  <span class="text-sm font-medium text-gray-900">{{role.name}}</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium">
                  <span class="text-sm font-medium text-gray-900">{{ $moment(role.created).format("LLL") }}</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium">
                  <span class="text-sm font-medium text-gray-900" v-if="role.updated">{{ $moment(role.updated).format("LLL") }}</span>
                  <span class="text-sm font-medium text-gray-900" v-else>---Not Updated---</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                  <a href="#" class="text-indigo-600 hover:text-indigo-900" v-if="userRoles.includes('superuser') | userRoles.includes('admin')">Edit</a>
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
    const roles = computed(() => store.state.roles)
    const fetchRoles = store.dispatch("fetchRoles")
    const userRoles = computed(() => map(user.value.roles, "name"))

    onMounted(async () => {
      fetchRoles
    })

    return {
      user,
      users,
      roles,
      userRoles,
      fetchRoles
    }
  }
});
</script>
