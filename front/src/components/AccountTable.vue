<template>
    <table class="divide-y divide-gray-200 w-full">
        <thead class="bg-gray-50">
            <tr>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Card No
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Account No
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Account Name
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Expiration Date
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Created
            </th>
            
            </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
            <tr
            v-for="account in accounts"
            :key="account.id">
            <td class="px-6 py-4 text-sm text-gray-500 break-all overflow-ellipsis overflow-hidden ...">
                {{account.card_no}}
            </td>
            <td class="px-6 py-4 text-sm text-gray-500 break-all overflow-ellipsis overflow-hidden ...">
                {{account.account_number}}
            </td>
            <td class="px-6 py-4 text-sm text-gray-500 break-all overflow-ellipsis overflow-hidden ...">
                {{account.account_name}}
            </td>
            <td class="px-6 py-4 text-sm text-gray-500 break-all overflow-ellipsis overflow-hidden ...">
                {{account.expiration_date}}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <span class="text-sm font-medium text-gray-900 truncate ...">{{ $moment(account.created).format("LLL") }}</span>
            </td>
            </tr>
            <!-- More people... -->
        </tbody>
    </table>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
export default defineComponent({
  name: 'AccountTable',
  components: {
  },
  props: ["accounts"]
})
</script>