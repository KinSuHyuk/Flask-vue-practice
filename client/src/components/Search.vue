<template>
    <div>
      <div class="input-group mb-3">
        <input type="text" class="form-control" v-model="searchTerm" placeholder="검색어를 입력하세요" />
        <button class="btn btn-primary" @click="search">검색</button>
      </div>
      <div v-if="searchResults.length > 0">
        <h2>검색 결과</h2>
        <ul class="list-group">
          <li v-for="result in searchResults" :key="result.상호명" class="list-group-item">
            <h3>{{ result.상호명 }}</h3>
            <p>업종명: {{ result.상권업종대분류명 }}</p>
            <p>업종코드: {{ result.상권업종대분류코드 }}</p>
            <p>지번주소: {{ result.지번주소 }}</p>
            <p>도로명주소: {{ result.도로명주소 }}</p>
            <p>경도: {{ result.경도 }}</p>
            <p>위도: {{ result.위도 }}</p>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        searchTerm: '',
        searchResults: [],
      };
    },
    methods: {
      async search() {
        try {
          console.log(this.searchTerm)
          const response = await axios.get(`http://127.0.0.1:5000/search?name=${this.searchTerm}`);
          console.log('searchresult', response.data)
          this.searchResults = response.data
          //console.log('수량:',searchResults.length)
        } catch (error) {
          console.error(error);
        }
      }
    },
  };
  </script>
  