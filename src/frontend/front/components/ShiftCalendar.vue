<template>
  <div>
    <v-sheet tile height="54" class="d-flex">
      <v-btn icon class="ma-2" @click="$refs.calendar.prev()">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-select
        v-model="type"
        :items="types"
        dense
        outlined
        hide-details
        class="ma-2"
        label="type"
      ></v-select>
      <v-spacer></v-spacer>
      <v-btn icon class="ma-2" @click="$refs.calendar.next()">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-sheet>
    <v-sheet height="800">
      <v-calendar
        ref="calendar"
        v-model="value"
        :type="type"
        :events="shifts"
      ></v-calendar>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: 'ShiftCalendar',
  data: () => ({
    type: 'month',
    types: ['month', 'week'],
    value: '',
    events: [],
    colors: [],
    names: [],
    shifts: [
      {
        name: '金子雄真',
        start: '2022-04-20 09:00',
        end: '2022-04-20 13:00',
        color: 'purple',
      },
      {
        name: '浅地春輝',
        start: '2022-04-20 13:00',
        end: '2022-04-20 17:00',
        color: 'green',
      },
      {
        name: '杉ノ原朋加',
        start: '2022-04-20 17:00',
        end: '2022-04-20 21:00',
        color: 'pink',
      },
      {
        name: '長井ゆうか',
        start: '2022-04-20 21:00',
        end: '2022-04-20 24:00',
        color: 'yellow',
      },
    ],
  }),
  methods: {
    getEvents({ start, end }) {
      const events = []
      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        })
      }

      this.events = events
    },
    getEventColor(event) {
      return event.color
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
  },
}
</script>