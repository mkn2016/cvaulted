<template>
    <nav class="flex-1 px-2 bg-indigo-800">
        <router-link
        to="/secure/dashboard"
        class="mt-1 group flex items-center px-2 py-2 text-sm leading-5 font-medium text-indigo-300 rounded-md hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150" :class="$route.path === 'secure/dashboard' ? 'text-white' : 'text-gray-500'"
        
    >
        <svg
        class="mr-3 h-6 w-6 text-indigo-400 group-focus:text-indigo-300 transition ease-in-out duration-150"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        >
        <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
        />
        </svg>
        Dashboard
        </router-link>

        <router-link
            to="/secure/users"
            class="mt-1 group flex items-center px-2 py-2 text-sm leading-5 font-medium text-indigo-300 rounded-md hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150" :class="$route.path === '/secure/users' ? 'text-white' : 'text-gray-500'"
             v-if="roles.includes('superuser') || roles.includes('admin') || roles.includes('manager')"
        >
            <svg
            class="mr-3 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
            />
            </svg>
            Users
        </router-link>

        <router-link
            to="/secure/roles"
            class="mt-1 group flex items-center px-2 py-2 text-sm leading-5 font-medium text-indigo-300 rounded-md hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150" :class="$route.path === '/secure/roles' ? 'text-white' : 'text-gray-500'"
            v-if="roles.includes('superuser') || roles.includes('admin')"
        >
            <svg id="Capa_1" enable-background="new 0 0 512 512" height="512" viewBox="0 0 512 512" width="512"  class="mr-3 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150 fill-current">
            <g>
                <path d="m322.967 182.394c-5.857-5.857-15.355-5.857-21.213 0-5.857 5.857-5.857 15.355 0 21.213l21.213 21.213c2.929 2.929 6.768 4.394 10.606 4.394s7.678-1.465 10.606-4.394l42.426-42.426c5.858-5.857 5.858-15.355 0-21.213-5.857-5.859-15.354-5.857-21.213 0l-31.818 31.819z"/>
                <path d="m365.394 237.181-31.82 31.819-10.607-10.606c-5.857-5.857-15.355-5.857-21.213 0-5.857 5.857-5.857 15.355 0 21.213l21.213 21.213c2.929 2.929 6.768 4.394 10.606 4.394s7.678-1.465 10.606-4.394l42.426-42.426c5.858-5.857 5.858-15.355 0-21.213-5.856-5.86-15.353-5.858-21.211 0z"/>
                <path d="m256 178h-120c-8.284 0-15 6.716-15 15s6.716 15 15 15h120c8.284 0 15-6.716 15-15s-6.716-15-15-15z"/>
                <path d="m256 254h-120c-8.284 0-15 6.716-15 15s6.716 15 15 15h120c8.284 0 15-6.716 15-15s-6.716-15-15-15z"/>
                <path d="m256 330h-120c-8.284 0-15 6.716-15 15s6.716 15 15 15h120c8.284 0 15-6.716 15-15s-6.716-15-15-15z"/>
                <path d="m256 406h-120c-8.284 0-15 6.716-15 15s6.716 15 15 15h120c8.284 0 15-6.716 15-15s-6.716-15-15-15z"/>
                <path d="m436 60h-85.305c-5.653-11.992-17.776-20-31.637-20h-13.846l5.341-21.362c1.12-4.48.113-9.229-2.729-12.869-2.844-3.641-7.205-5.769-11.824-5.769h-80c-4.619 0-8.98 2.128-11.823 5.769-2.842 3.641-3.849 8.389-2.729 12.869l5.341 21.362h-13.846c-13.86 0-25.984 8.008-31.637 20h-85.306c-8.284 0-15 6.716-15 15v422c0 8.284 6.716 15 15 15h360c8.284 0 15-6.716 15-15v-422c0-8.284-6.716-15-15-15zm-243.058 10h33.058c4.619 0 8.98-2.128 11.823-5.769 2.842-3.641 3.849-8.389 2.729-12.869l-5.341-21.362h41.577l-5.341 21.362c-1.12 4.48-.113 9.229 2.729 12.869 2.844 3.641 7.205 5.769 11.824 5.769h33.058c2.454 0 4.528 1.757 4.932 4.178l4.303 25.822h-144.586l4.304-25.822c.403-2.421 2.477-4.178 4.931-4.178zm228.058 412h-330v-392h63.96l-3.756 22.534c-.725 4.349.5 8.797 3.351 12.161s7.036 5.305 11.445 5.305h180c4.409 0 8.595-1.94 11.445-5.305s4.076-7.813 3.351-12.161l-3.756-22.534h63.96z"/>
            </g>
            </svg>
            Roles
        </router-link>

         <router-link
            to="/secure/accounts"
            class="mt-1 group flex items-center px-2 py-2 text-sm leading-5 font-medium text-indigo-300 rounded-md hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150" :class="$route.path === '/secure/accounts' ? 'text-white' : 'text-gray-500'"
            v-if="roles.includes('superuser') || roles.includes('admin') || roles.includes('manager') || roles.includes('moderator')"
        >
            <svg enable-background="new 0 0 20 20"  class="mr-3 h-6 w-6 fill-current stroke-current text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
            viewBox="0 0 20 20"
            stroke="currentColor">
                <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="none">
                    <g id="Rounded" transform="translate(-273.000000, -157.000000)">
                        <g id="Action" transform="translate(100.000000, 100.000000)">
                            <g id="-Round-/-Action-/-account_box" transform="translate(170.000000, 54.000000)">
                                <g>
                                    <polygon id="Path" points="0 0 24 0 24 24 0 24"></polygon>
                                    <path d="M3,5 L3,19 C3,20.1 3.89,21 5,21 L19,21 C20.1,21 21,20.1 21,19 L21,5 C21,3.9 20.1,3 19,3 L5,3 C3.89,3 3,3.9 3,5 Z M15,9 C15,10.66 13.66,12 12,12 C10.34,12 9,10.66 9,9 C9,7.34 10.34,6 12,6 C13.66,6 15,7.34 15,9 Z M6,17 C6,15 10,13.9 12,13.9 C14,13.9 18,15 18,17 L18,18 L6,18 L6,17 Z" id="🔹Icon-Color" fill="rgba(99, 102, 241, 1)"></path>
                                </g>
                            </g>
                        </g>
                    </g>
                </g>
            </svg>
            Accounts
        </router-link>
    </nav>
</template>

<script lang="ts">
import { computed, defineComponent} from 'vue'
import {useStore} from "vuex"
import _ from "lodash"

export default defineComponent({
    name: 'SideBarLink',
    components: {

    },
    setup() {
        const store = useStore()

        const user = computed(() => store.state.user)
        const roles = computed(() => _.map(user.value.roles, "name"))
        
        return {
            user,
            roles
        }
    }
});
</script>