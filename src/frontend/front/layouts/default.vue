<template>
  <v-app>
    <TheHeader />
    <v-sheet elevation="0" height="64" width="100%"></v-sheet>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>

    <v-footer>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import TheHeader from '@/components/TheHeader.vue'
export default {
  name: 'DefaultLayout',
  components: {
    TheHeader,
  },
  data() {
    return {}
  },
}
</script>
