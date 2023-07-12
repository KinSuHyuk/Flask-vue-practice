<template>
  <main>
    <div>
      <h2>상호명 검색</h2>
      <input v-model="searchName" type="text" placeholder="상호명을 입력하세요">
      <button @click="search">검색</button>
      <div v-if="searchResult !== []">
         <ul>
          <li v-for="item in searchResult" :key="item.상호명">
            <p>{{ decodeText(item.상권업종대분류코드) }}</p>
            <p>{{ decodeText(item.상권업종대분류명) }}</p>
            <p>{{ decodeText(item.지번주소) }}</p>
            <p>{{ decodeText(item.도로명주소) }}</p>
            <p>{{ decodeText(item.경도) }}</p>
            <p>{{ decodeText(item.위도) }}</p>
          </li>
        </ul> 
      </div>
      <div v-else>
         <p>Loading...</p>
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
      searchResult: []
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
    },
    decodeText(text) {
      const element = document.createElement('div');
      element.innerHTML = text;
      return element.innerText;
    }
  }
}
</script>
