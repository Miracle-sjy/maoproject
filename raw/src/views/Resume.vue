<template>
  <div>
    <!-- 授权码输入区域 -->
    <div v-if="showAuthInput" class="input-area">
      <!-- <label style="color: white; font-size: 16px;">请输入授权码</label> -->
      <input v-model="authCode" placeholder="请输入授权码" @keyup.enter="submitAuthCode" />
      <button @click="submitAuthCode">提交</button>
      <p v-if="errorMessage" style="color: red; text-align: center;">{{ errorMessage }}</p>
    </div>

    <!-- PDF预览区域 -->
    <div v-if="pdfUrl" class="pdf-preview">
      <iframe :src="pdfUrl" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      authCode: '',
      pdfUrl: '',
      errorMessage: '',
      showAuthInput: true,
    };
  },
  methods: {
    submitAuthCode() {
      this.errorMessage = '';
      axios.get('http://localhost:8081/pdf/preview', { 
        params: { 
          authCode: this.authCode 
        }, 
        responseType: 'blob' // 修改响应类型为 blob
      })
      .then(response => {
        this.pdfUrl = URL.createObjectURL(response.data); // 创建PDF文件的URL
        this.showAuthInput = false;
      })
      .catch(error => {
        if (error.response && error.response.status === 401) {
          this.errorMessage = '授权码错误，请重新输入';
        } else {
          this.errorMessage = '发生错误，请稍后再试';
        }
      });
    },
  },
};
</script>

<style>
/* 输入区域的样式 */
.input-area {
  display: flex;
  flex-direction: column;
  align-items: center; /* 使内容在交叉轴上的起点对齐 */
  justify-content: center; /* 使内容在主轴上的起点对齐 */
  height: 100vh; /* 使输入区域占满整个视口的高度 */
}

/* 输入框的样式 */
input{
  width: 10%;
  padding: 10px;
  border: 1px solid #00dfc4;
  border-radius: 4px;
  outline: none;
  color: white; /* 输入字符颜色 */
  background: #1f242d; /* 输入框背景色 */
  font-size: 16px;
}

/* 占位符样式 */
input[type="text"]::placeholder {
  color: white; /* 占位符字体颜色 */
}

/* 提交按钮的样式 */
button {
  background-color: #0000ff; /* 按钮背景为蓝色 */
  color: white; /* 按钮字体颜色 */
  padding: 10px 20px; /* 内边距 */
  margin-top: 10px; /* 与输入框的距离 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 圆角边框 */
  cursor: pointer; /* 鼠标悬停时显示指针 */
  transition: background-color 0.3s; /* 过渡效果 */
}

button:hover {
  background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
}

/* 错误消息的样式 */
p {
  color: red; /* 错误消息颜色 */
  text-align: center; /* 文本居中 */
  margin-top: 10px; /* 与按钮的距离 */
}

/* PDF预览区域的样式 */
.pdf-preview {
  width: 100vw; /* 宽度占满整个视口 */
  height: 100vh; /* 高度占满整个视口 */
}

iframe {
  width: 100%; /* 宽度占满整个容器 */
  height: 100%; /* 高度占满整个容器 */
  border: none; /* 无边框 */
}

</style>