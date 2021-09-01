<template>
  <div class="hidden md:flex md:flex-shrink-0">
    <div class="flex flex-col w-64">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="flex flex-col flex-grow bg-indigo-800 pt-5 pb-4 overflow-y-auto">
        <div class="flex justify-center flex-shrink-0 px-4">
          <img
            class=""
            src="../assets/logo.png"
            alt="Kanbanter"
            width="80"
            height="50"
          />
        </div>
        <h2 class="px-4 font-semibold text-white">
          Menu
        </h2>
        <div class="mt-1 flex-1 flex flex-col">
          <side-bar-link></side-bar-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

import SideBarLink from "../components/SideBarLink.vue";

export default defineComponent({
  name: 'SideBar',
  components: {
      SideBarLink
  },
  setup () {
    const username = ref("")

    const onSubmit = () => {
      console.log("i am submitting")
      console.log(username.value)
    }

    return {
      username,
      onSubmit
    }
  }
});
</script>
