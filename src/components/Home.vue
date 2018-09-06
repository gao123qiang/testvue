<template>
    <div>
        <MHeader>首页</MHeader>
        <div class="content">
          <Swiper :swiperSlides="sliders"></Swiper>
          <div class="container">
            <h3>热门图书</h3>
            <ul>
              <li v-for="hot in hotBooks">
                <img :src="hot.bookCover">
                <b>{{hot.bookName}}</b>
              </li>
            </ul>
          </div>
        </div>
    </div>
</template>

<script>
  import MHeader from '../base/MHeader.vue';
  import Swiper from '../base/swiper.vue';
  import {getSliders,getHotBook} from "../api";
  export default {
        async created(){
          this.getSlider();
          this.getHotbook();
        },
        name: "",
        data() {
            return {sliders:[],
                    hotBooks:[]
            }
        },
        methods: {
          async getSlider(){
            //给data起别名，对象中的属性名字必须和得到的结果名字一致
            this.sliders = await getSliders();
          },
          async getHotbook(){
            this.hotBooks = await getHotBook();
          }
        },
        computed: {},
        components: {
          MHeader,
          Swiper
        }
    }
</script>

<style scoped lang="less">
 .container{
   width:90%;
   margin:0 auto;
   h3{
     margin-bottom: 10px;
   }
   ul{
      display:flex;
      flex-wrap:wrap;
     li{
        width:33.33333333%;
        b{margin-left: 30px;
          color:darkgreen;
          font-size: 15px;
        }
       img{width:80%}
     }
   }
 }
</style>
