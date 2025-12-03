<template>
  <div class="w-full h-full">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'

export default {
  name: 'RoomTypeChart',
  props: {
    data: Array,
    metric: String
  },
  mounted() {
    this.renderChart()
  },
  methods: {
    renderChart() {
      Chart.register(...registerables)
      
      const ctx = this.$refs.chartCanvas.getContext('2d')
      const labels = this.data.map(item => item.type)
      const dataset = this.data.map(item => item[this.metric])
      
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: this.getMetricLabel(),
            data: dataset,
            backgroundColor: '#137fec',
            borderColor: '#137fec',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                callback: (value) => this.formatValue(value)
              }
            }
          }
        }
      })
    },
    getMetricLabel() {
      const labels = {
        revenue: 'Revenue ($)',
        occupancy: 'Occupancy (%)',
        adr: 'ADR ($)'
      }
      return labels[this.metric] || this.metric
    },
    formatValue(value) {
      if (this.metric === 'revenue' || this.metric === 'adr') {
        return '$' + value.toLocaleString()
      } else if (this.metric === 'occupancy') {
        return value + '%'
      }
      return value
    }
  },
  watch: {
    metric() {
      this.renderChart()
    }
  }
}
</script>