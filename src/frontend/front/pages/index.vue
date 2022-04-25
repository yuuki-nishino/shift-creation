<template>
  <div class="container">
    <h1 align="center">{{ store }}</h1>
    <ShiftCalendar />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data: () => ({
    store: '蛍池本店',
  }),
}
</script>
