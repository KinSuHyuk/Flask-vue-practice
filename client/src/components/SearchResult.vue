<template>
  <main>
    <div>
      <h1>제목</h1>
      <input v-model="searchName" type="text" placeholder="상호명을 입력하세요">
      <button @click="search">검색</button>
      <div v-if="searchResult">
        <h2>나와</h2>
        {{ searchResult }}
        <!-- <ul>
          <li v-for="item in searchResult" :key="item.상호명">
            <p>{{ item.업종코드 }}</p>
            <p>{{ item.업종명 }}</p>
            <p>{{ item.지번주소 }}</p>
            <p>{{ item.도로명주소 }}</p>
            <p>{{ item.경도 }}</p>
            <p>{{ item.위도 }}</p>
          </li>
        </ul> -->
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchName: '',
      searchResult: null
    }
  },
  methods: {
    search() {
      const path = 'http://localhost:5000/search'; 
      axios.get(path, { params: { name: this.searchName } })
        .then(response => {
          this.searchResult = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
}
</script>
