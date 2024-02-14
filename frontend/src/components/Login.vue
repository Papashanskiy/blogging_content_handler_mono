<!-- Login.vue -->
<template>
    <div>
        <button @click="login">Login with Instagram</button>
    </div>
</template>

<script>
export default {
    methods: {
        login() {
            window.location.href = 'http://localhost:8000/auth'
        }
    }
}
</script>
