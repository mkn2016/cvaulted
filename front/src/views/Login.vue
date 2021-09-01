<template>
    <div>
      <div>
          <img class="mx-auto w-24 h-20" src="../assets/logo.png" alt="CVaulted">
          <h2 class="mt-2 text-center text-3xl font-extrabold text-gray-900">
            Sign in to your account
          </h2>
      </div>
      <form class="mt-8 space-y-6" action="#" @submit.prevent="onSubmit">
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert" v-if="errorOccurred">
          <span class="block sm:inline">{{errorMessage}}</span>
          <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
            <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><title>Close</title><path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/></svg>
          </span>
        </div>
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
                <label for="username" class="sr-only">Email address</label>
                <input id="username" name="username" type="text" autocomplete="username" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username" v-model="username">
            </div>
            <div>
                <label for="password" class="sr-only">Password</label>
                <input id="password" name="password" type="password" autocomplete="current-password" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password" v-model="password">
            </div>
        </div>

        <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded">
              <label for="remember-me" class="ml-2 block text-sm text-gray-900">
                  Remember me
              </label>
            </div>

            <div class="text-sm">
              <router-link
                    to="/register"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                >
                    Register Account?
              </router-link>
            </div>
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <!-- Heroicon name: solid/lock-closed -->
                <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                </svg>
            </span>
            Sign in
            </button>
        </div>
      </form>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import {useRouter} from "vue-router";
import axios from "axios";

export default defineComponent({
  name: 'Login',
  components: {
  },
  setup () {
    const username = ref("")
    const password = ref("")
    const errorOccurred = ref(false)
    const errorMessage = ref("")
    const router = useRouter()

    const onSubmit = async () => {
      if (username.value === "" && password.value === "") {
        errorOccurred.value = true
        errorMessage.value = "username or password is required"
      } else {
        await axios.post(
          "auth/login",
          {
            username: username.value,
            password: password.value
          },
          {
            withCredentials: true
          },
        )
        .then(res => {
          setAccessToken(res.data[0]["access_token"])
          router.push("/secure/dashboard")
        })
        .catch(error => {
          errorOccurred.value = true
          if (error.response) {
            errorMessage.value = error.response.data.message
          } else if (error.request) {
            console.log(error.request);
            console.log(error.request.message);
          } else {
            console.log('Error', error.message);
          }
        })
      }
    }

    function setAccessToken(token:string) {
      sessionStorage.setItem("token", token)
    }

    return {
      username,
      password,
      errorOccurred,
      errorMessage,
      setAccessToken,
      onSubmit,
    }
  }
});
</script>