<template>
<div class="h-screen flex overflow-hidden bg-gray-100">
    <transition leave-active-class="duration-300">
        <div v-show="sidebarOpen" class="md:hidden">
            <div class="fixed inset-0 flex z-40">
            <!--
                Off-canvas menu overlay, show/hide based on off-canvas menu state.
            -->
            <transition
                enter-active-class="transition-opacity ease-linear duration-300"
                enter-class="opacity-0"
                enter-to-class="opacity-100"
                leave-active-class="transition-opacity ease-linear duration-300"
                leave-class="opacity-100"
                leave-to-class="opacity-0"
            >
                <div v-show="sidebarOpen" class="fixed inset-0">
                <div class="absolute inset-0 bg-gray-600 opacity-75"></div>
                </div>
            </transition>
            <!--
                Off-canvas menu, show/hide based on off-canvas menu state.
            -->
            <transition
                enter-active-class="transition ease-in-out duration-300 transform"
                enter-class="-translate-x-full"
                enter-to-class="translate-x-0"
                leave-active-class="transition ease-in-out duration-300 transform"
                leave-class="translate-x-0"
                leave-to-class="-translate-x-full"
            >
                <div
                v-show="sidebarOpen"
                class="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-indigo-800"
                >
                <div class="absolute top-0 right-0 -mr-14 p-1">
                    <button
                    v-show="sidebarOpen"
                    @click="sidebarOpen = false"
                    class="flex items-center justify-center h-12 w-12 rounded-full focus:outline-none focus:bg-gray-600"
                    aria-label="Close sidebar"
                    >
                    <svg
                        class="h-6 w-6 text-white"
                        stroke="currentColor"
                        fill="none"
                        viewBox="0 0 24 24"
                    >
                        <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M6 18L18 6M6 6l12 12"
                        />
                    </svg>
                    </button>
                </div>
                <div class="flex-shrink-0 flex items-center px-4">
                    <img
                    class="h-8 w-auto"
                    src=""
                    alt="Workflow"
                    />
                </div>
                <div class="mt-5 flex-1 h-0 overflow-y-auto">
                    <nav class="px-2">
                    <a
                        href="#"
                        class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-white bg-indigo-900 focus:outline-none focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
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
                    </a>
                    <a
                        href="#"
                        class="mt-1 group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-indigo-300 hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
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
                        Team
                    </a>
                    <a
                        href="#"
                        class="mt-1 group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-indigo-300 hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
                        />
                        </svg>
                        Projects
                    </a>
                    <a
                        href="#"
                        class="mt-1 group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-indigo-300 hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                        />
                        </svg>
                        Calendar
                    </a>
                    <a
                        href="#"
                        class="mt-1 group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-indigo-300 hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                        />
                        </svg>
                        Documents
                    </a>
                    <a
                        href="#"
                        class="mt-1 group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md text-indigo-300 hover:text-white hover:bg-indigo-700 focus:outline-none focus:text-white focus:bg-indigo-700 transition ease-in-out duration-150"
                    >
                        <svg
                        class="mr-4 h-6 w-6 text-indigo-400 group-hover:text-indigo-300 group-focus:text-indigo-300 transition ease-in-out duration-150"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                        />
                        </svg>
                        Reports
                    </a>
                    </nav>
                </div>
                </div>
            </transition>
            <div class="flex-shrink-0 w-14">
                <!-- Dummy element to force sidebar to shrink to fit close icon -->
            </div>
            </div>
        </div>
    </transition>

    <side-bar></side-bar>
    <div class="flex flex-col w-0 flex-1 overflow-hidden">
        <div class="relative z-10 flex-shrink-0 flex h-16 bg-white shadow">
            <button
            @click="sidebarOpen = true"
            class="px-4 border-r border-gray-200 text-gray-500 focus:outline-none focus:bg-gray-100 focus:text-gray-600 md:hidden"
            aria-label="Open sidebar"
            >
            <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h7"
                />
            </svg>
            </button>
            <div class="flex-1 px-4 flex justify-between">
            <div class="flex-1 flex">
                <form class="w-full flex md:ml-0" action="#" method="GET">
                <label for="search_field" class="sr-only">Search</label>
                <div class="relative w-full text-gray-400 focus-within:text-gray-600">
                    <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
                    <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
                        <path
                        fill-rule="evenodd"
                        clip-rule="evenodd"
                        d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                        />
                    </svg>
                    </div>
                    <input
                    id="search_field"
                    class="block w-full h-full pl-8 pr-3 py-2 rounded-md text-gray-900 placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 sm:text-sm"
                    placeholder="Search"
                    type="search"
                    />
                </div>
                </form>
            </div>
            <div class="ml-4 flex items-center md:ml-6">
                <button
                class="p-1 text-gray-400 rounded-full hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:shadow-outline focus:text-gray-500"
                aria-label="Notifications"
                >
                <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                    <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                    />
                </svg>
                </button>

                <div class="ml-3 relative">
                    <div class="flex flex-cols">
                        <span class="p-2">{{user.username}}</span>
                        
                        <button
                            @click="dropdownOpen = !dropdownOpen"
                            class="max-w-xs flex items-center text-sm rounded-full focus:outline-none focus:shadow-outline"
                            id="user-menu"
                            aria-label="User menu"
                            aria-haspopup="true"
                            >
                            <img
                                class="h-8 w-8 rounded-full"
                                src="../assets/user.png"
                                alt=""
                            />
                        </button>
                    </div>
                    <transition
                        enter-active-class="transition ease-out duration-100"
                        enter-class="transform opacity-0 scale-95"
                        enter-to-class="transform opacity-100 scale-100"
                        leave-active-class="transition ease-in duration-75"
                        leave-class="transform opacity-100 scale-100"
                        leave-to-class="transform opacity-0 scale-95"
                    >
                        <div
                        v-show="dropdownOpen"
                        class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg"
                        >
                        <div
                            class="py-1 rounded-md bg-white shadow-xs"
                            role="menu"
                            aria-orientation="vertical"
                            aria-labelledby="user-menu"
                        >
                            <a
                            href="#"
                            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition ease-in-out duration-150"
                            role="menuitem"
                            >Your Profile</a
                            >
                            <a
                            href="#"
                            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition ease-in-out duration-150"
                            role="menuitem"
                            >Settings</a
                            >
                            <router-link
                            to=""
                            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 transition ease-in-out duration-150"
                            role="menuitem"
                            @click="logout"
                            >Sign Out</router-link
                            >
                        </div>
                        </div>
                    </transition>
                </div>
            </div>
            </div>
        </div>

        <main class="flex-1 relative z-0 overflow-y-auto focus:outline-none" tabindex="0">
            <router-view/>
        </main>
    </div>
</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, computed} from 'vue'
import {useStore} from "vuex"
import axios from "axios"
import {head} from "lodash"

import SideBar from "../components/SideBar.vue";

export default defineComponent({
    name: 'BaseLayout',
    data() {
        return {
            dropdownOpen: false,
            sidebarOpen: false,
        }
    },
    components: {
        SideBar
    },
    setup() {
        type User = {
            [key: string]: string | number | []
        }

        const store = useStore()
        const user = computed(() => store.state.user)
        let token = sessionStorage.getItem("token")


        onMounted(async () => {
            await axios.get(
                "users/user",
                {
                    headers: {
                    "Authorization": "Bearer " + token,
                    },
                    withCredentials: true
                }
            ).then(response => {
                let responseData:any = head(response.data)
                let user:User = responseData["data"]
                console.log(user)
                store.dispatch("setUser", user)
            }).catch(error => {
                console.log(head(error.message))
            })
        })

        function logout() {
            store.dispatch("logout")
        }
        
        return {
            user,
            token,
            logout
        }
    }
});
</script>