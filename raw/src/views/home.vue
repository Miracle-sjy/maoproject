<template>
 <!-- 根元素包裹整个组件内容 -->
 <div id="app" :class="`theme-${theme}`">
    <header class="header">
      <a href="#" class="logo">Raw</a>
      <nav class="navbar">
        
        <!-- 按钮列表，绑定点击事件来切换内容 -->
        <a href="#" class="item" v-for="(item, index) in menuItems" :key="index" @click="toggleContent(index)" :class="{'active': currentContentIndex === index}" style="--i: {{ index }}">
          {{ item }}
        </a>
        <!-- <a href="#" class="active item" style="--i: 1">Home</a> -->
        <!-- <a href="#" class="item" style="--i: 2">Login</a>
        <a href="#" class="item" style="--i: 3">tools</a> -->
        <!-- <a href="#" class="item" style="--i: 4">Portfolio</a>
        <a href="#" class="item" style="--i: 5">Contact</a> -->
      </nav>
    </header>

    
        <section class="home">
            <div class="home-content">
                <h3>ようこそ！😍</h3>
                <h1>Call Me RAW！</h1>
                <h3>And I'm a <span class="multiple-text"></span></h3>
                <p>星星之火，可以燎原🔥🔥🔥🔥🔥</p>
                <div class="social-media">
                    <a href="https://www.xiaohongshu.com/user/profile/5d366ea50000000012011ad1?xhsshare=CopyLink&appuid=5d366ea50000000012011ad1&apptime=1724719694&share_id=c199441a1b35474880d0a79f2c3dd20d"
                    style="--i: 7"><img src="../assets/image/R-C.png" alt="red"></img></a>
                    <a href="https://github.com/Miracle-sjy" style="--i: 8"><img src="../assets/image/github.png" alt="github"></img></a>
                    <a href="https://blog.csdn.net/lmiraclel?type=blog" style="--i: 9"><img src="../assets/image/csdn.png" alt="csdn"></img></a>
                    <a href="#" style="--i: 10"><img src="../assets/image/cloud.png" alt="cloud"></img></a>
                </div>
                <RouterLink to="/CV">
                <a href="#" class="btn">➡️➡️➡️简历入口⬅️⬅️⬅️</a>
                </RouterLink>
            </div>
        <!-- Home页面 -->
        <div v-if="currentContentIndex === 0">
            <div class="home-img">
                <img src="..\assets\image\title1.png" alt="" />
            </div>
        </div>
        <!-- login 内容 -->
        <div v-if="currentContentIndex === 1">
        <Login />
        </div>

        <!-- Tools 内容 -->
         <div v-if="currentContentIndex === 2">
            <ImageConverter />
            <Collectwebsite />
        </div>
        </section>
</div>
    
</template>

<script>
import Typed from 'typed.js';
import ImageConverter from '../components/ImageConverter.vue';
import Collectwebsite from '../components/Collectwebsite.vue';
import Login from '../components/login.vue';
export default {
  components: {
    ImageConverter,
    Collectwebsite,
    Login
  },

  data() {
    return {
      currentContentIndex: 0, // 默认显示第一个内容
      menuItems: ['Home', 'Login', 'Tools'], // 菜单项
      typed: null, // Typed.js 实例
      titleLibrary: [
        '你来辣！',
        '等你好久了🤗',
        '😍😍😍😍😍😍',
        // ...更多标题
      ],
      currentTitleIndex: 0, // 当前标题索引
    };
  },
  mounted() {
    // 初始化 Typed.js
    this.typed = new Typed(".multiple-text", {
      strings: ['Code Developer', "Libra-INFJ", "Photography enthusiasts"],
      typeSpeed: 100,
      backSpeed: 100,
      backDelay: 1000,
      loop: true
    });

    // 动态标题
    this.timer = setInterval(() => {
      this.cycleTitles();
    }, 5000);
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 清除定时器
    }
  },
  methods: {
    toggleContent(index) {
      this.currentContentIndex = index;
      // 这里可以根据 index 来更新 Typed.js 的内容，如果需要的话
    },
    cycleTitles() {
      document.title = this.titleLibrary[this.currentTitleIndex];
      this.currentTitleIndex = (this.currentTitleIndex + 1) % this.titleLibrary.length;
    }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

body {
    background: #1f242d;
    color: #fff;
}

.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 20px 10%;
    background: transparent;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
}

.logo {
    font-size: 25px;
    color: #fff;
    text-decoration: none;
    font-weight: 600;
    cursor: default;
    opacity: 0;
    animation: slideRight 1s ease forwards;
}

.navbar a {
    display: inline-block;
    font-size: 18px;
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    margin-left: 35px;
    opacity: 0;
    transition: 0.3s;
    animation: slideTop 1s ease forwards;
    animation-delay: calc(.2s * var(--i));
}

.navbar a:hover,
.navbar a.active {
    color: #b7b2a9;
}

.home {
    position: relative;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 70px 10% 0;
}

.home-content {
    color: #e4e4e4;
    max-width: 600px;
}

.home-content h3 {
    font-size: 32px;
    font-weight: 700;
    opacity: 0;
    animation: slideBottom 1s ease forwards;
    animation-delay: .7s;
}

.home-content h3:nth-of-type(2) {
    margin-bottom: 30px;
    opacity: 0;
    animation: slideTop 1s ease forwards;
    animation-delay: .7s;
}

.home-content h3 span {
    color: #b7b2a9;
}

.home-content h1 {
    font-size: 56px;
    font-weight: 700;
    margin: -3px 0;
    opacity: 0;
    animation: slideRight 1s ease forwards;
    animation-delay: 1s;
}

.home-content p {
    font-size: 16px;
    opacity: 0;
    color: #e4e4e4;
    animation: slideLeft 1s ease forwards;
    animation-delay: 0.7s;
}

.home-img img {
    max-width: 450px;
    border-radius: 50%;
    margin-right: -20px;
    box-shadow: 0 0 20px #b7b2a9;
    opacity: 0;
    animation: zoomIn 1s ease forwards, floatImage 4s ease-in-out infinite;
    animation-delay: 0.5s,3s;
}

.social-media a {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    background: transparent;
    border: 2px solid #b7b2a9;
    border-radius: 50%;
    color: #b7b2a9;
    font-size: 20px;
    text-decoration: none;
    margin: 30px 15px 30px 0;
    transition: 0.5s ease;
    opacity: 0;
    animation: slideLeft 1s ease forwards;
    animation-delay: calc(0.2s * var(--i));
}

.social-media a img {
    width: 100%; /* 或者具体的像素值，如 width: 40px; */
    height: 100%; /* 或者具体的像素值，如 height: 40px; */
    object-fit: contain; /* 保持图片比例 */
    border-radius: 50%; /* 与链接按钮的圆角一致 */
    opacity: 0.9; /* 透明度 */
}

.social-media a:hover {
    background: #b7b2a9;
    color: #1f242d;
    box-shadow: 0 0 20px #b7b2a9;
}

.btn {
    display: inline-block;
    padding: 12px 28px;
    background: #b7b2a9;
    text-decoration: none;
    border-radius: 40px;
    box-shadow: 0 0 10px #b7b2a9;
    font-size: 16px;
    color: #1f242d;
    letter-spacing: 1px;
    font-weight: 600;
    transition: 0.5s ease;
    opacity: 0;
    animation: slideTop 1s ease forwards;
    animation-delay: 2s;
}

.btn:hover {
    box-shadow: 0 0 20px #b7b2a9;
}

.btn:active {
    background: none;
    color: #b7b2a9;
    border: 2px solid #b7b2a9;
}

/* 动画 */

@keyframes slideRight {
    0% {
        transform: translateX(-100px);
    }

    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes slideLeft {
    0% {
        transform: translateX(100px);
    }

    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes slideTop {
    0% {
        transform: translateY(100px);
    }

    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes slideBottom {
    0% {
        transform: translateY(-100px);
    }

    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes zoomIn {
    0% {
        transform: scale(0);
        opacity: 0;
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}


@keyframes floatImage {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-24px);
    }

    100% {
        transform: translateY(0);
    }
}
</style>