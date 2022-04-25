<template>
  <v-app-bar fixed>
    <v-toolbar-title class="font-weight-bold">
      {{ title }}
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {
  name: 'TheHeader',
  data: () => ({
    title: '白天狗',
  }),
}
</script>