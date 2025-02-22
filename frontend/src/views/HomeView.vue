<template>
    <div>
      Daily message from Nagy Mark: <br />
      {{ data }}
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted,ref } from 'vue'

const data = ref(null)

onMounted(() => {
  axios.get('/get_nagy_mark')
  .then(response => {
    data.value = response.data.message
  })
  .catch(error => {
    console.log(error)
  })
})
</script>
