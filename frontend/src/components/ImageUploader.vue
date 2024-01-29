<template>
  <div>
    <!-- Форма загрузки изображений -->
    <form @submit.prevent="uploadImage">
      <input type="file" ref="fileInput" @change="handleFileChange" />
      <button type="submit">Загрузить</button>
    </form>

    <!-- Список загруженных изображений с параметрами -->
    <div v-for="(image, index) in images" :key="index">
      <img :src="image.url" alt="Image" />
      <div>
        <label>Порядок:</label>
        <input type="number" v-model="image.order" />
      </div>
      <div>
        <label>Время публикации:</label>
        <input type="datetime-local" v-model="image.publishTime" />
      </div>
    </div>

    <!-- Кнопка для отправки данных на бэкенд -->
    <button @click="submitImages">Отправить на бэкенд</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      images: [],
    };
  },
  methods: {
    handleFileChange() {
      const fileInput = this.$refs.fileInput;
      const files = fileInput.files;

      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const imageUrl = URL.createObjectURL(file);

        this.images.push({
          file,
          url: imageUrl,
          order: 0,
          publishTime: '',
        });
      }

      fileInput.value = '';
    },
    uploadImage() {
      this.images.forEach(async (image) => {
        const formData = new FormData();
        formData.append('file', image.file);

        try {
          // Вам нужно заменить '/api/upload' на соответствующий эндпоинт вашего бэкенда
          const response = await axios.post('/api/upload', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });

          console.log('Image uploaded successfully:', response.data);
        } catch (error) {
          console.error('Error uploading image:', error);
        }
      });
    },
    submitImages() {
      // Вы можете обработать дополнительные данные или логику перед отправкой
      // Добавьте ваш код здесь, если необходимо

      // Отправка данных на бэкенд
      this.uploadImage();
    },
  },
};
</script>

<style scoped>
/* Ваши стили здесь */
</style>
