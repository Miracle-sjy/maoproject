<template>
   <div class="image-converter-container">
    <div class="image-converter"> 
        <h1>图片格式转换器</h1>
        <input type="file" @change="fileChange" ref="fileList" />
        <select v-model="format" @change="changeFormat">
          <option v-for="(format, index) in formatList" :key="index" :value="index">{{ format }}</option>
        </select>
        <button @click="getImg">开始转换</button>
        <a :href="imgURL" download>下载图片</a>
        <canvas :data-href="imgURL" style="display: none;"></canvas>
    </div>
  </div>
    
  </template>
  
  <script>
  export default {
    name: 'ImageConverter',
    data() {
      return {
        filename: undefined,
        formatList: ['png', 'jpeg', 'webp'],
        format: 0,
        imgURL: undefined,
      };
    },
    methods: {
      imgToCanvas(image) {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;
        canvas.getContext('2d').drawImage(image, 0, 0);
        return canvas;
      },
      getImg() {
        const imgFile = new FileReader();
        imgFile.onload = e => {
          const image = new Image();
          image.src = e.target.result;
          image.onload = () => {
            const canvas = this.imgToCanvas(image);
            this.imgURL = canvas.toDataURL(`image/${this.formatList[this.format]}`);
            this.filename = undefined;
          };
        };
        if (this.$refs.fileList.files[0]) {
          imgFile.readAsDataURL(this.$refs.fileList.files[0]);
        }
      },
      fileChange(e) {
        const file = e.target.files[0];
        if (file && /^image/.test(file.type)) {
          this.filename = file.name;
        } else {
          alert('请上传正确图片格式!');
        }
      },
      changeFormat() {
        if (this.imgURL) {
          const canvas = document.createElement('canvas');
          const img = new Image();
          img.src = this.imgURL;
          img.onload = () => {
            canvas.width = img.width;
            canvas.height = img.height;
            canvas.getContext('2d').drawImage(img, 0, 0);
            this.imgURL = canvas.toDataURL(`image/${this.formatList[this.format]}`);
          };
        }
      },
      downloadFile() {
        if (this.imgURL) {
          const link = document.createElement('a');
          link.href = this.imgURL;
          link.download = new Date().getTime();
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        }
      },
    },
  };
  </script>
  
  <style>
.image-converter-container {
  background-image: url('../assets/image/tools1.jpg'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个元素 */
  background-position: center; /* 背景图片居中显示 */
  background-repeat: no-repeat; /* 背景图片不重复 */
  color: #fff; /* 文字颜色 */
  position: fixed;
  top: 25%;
  left: 60%;
  transform: translate(-50%, -50%); /* 居中定位 */
  width: 90%; /* 宽度调整为视口宽度的90% */
  max-width: 500px; /* 最大宽度限制 */
  padding: 20px;
  border-radius: 8px; /* 圆角边框 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* 轻微的阴影 */
  z-index: 200;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center; /* 使文本居中 */
  animation: fadeIn 0.5s ease forwards; /* 淡入动画 */
}

.image-converter {
  width: 100%; /* 占满容器宽度 */
  padding: 10px; /* 内边距 */
  box-sizing: border-box; /* 边框计算在宽度内 */
}

.image-converter input[type="file"] {
  display: block; /* 块级元素 */
  margin: 10px 0; /* 外边距 */
}

.image-converter select {
  margin: 10px 0; /* 外边距 */
  padding: 8px; /* 内边距 */
  border-radius: 4px; /* 下拉框圆角 */
  background-color: #fff; /* 下拉框背景色 */
  color: #333; /* 下拉框文字颜色 */
}

.image-converter button {
  margin: 10px 0; /* 外边距 */
  padding: 8px 15px; /* 内边距 */
  border: none; /* 无边框 */
  border-radius: 4px; /* 按钮圆角 */
  background-color: #6a5acd; /* 按钮背景色 */
  color: #fff; /* 按钮文字颜色 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: background-color 0.3s; /* 背景色变化过渡效果 */
}

.image-converter button:hover {
  background-color: #5a48c2; /* 鼠标悬浮时的背景色 */
}

.image-converter a {
  display: inline-block;
  margin-top: 10px; /* 外边距 */
  text-decoration: none; /* 去除下划线 */
  color: #fff; /* 文字颜色 */
}

/* 淡入动画 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.5); /* 开始时缩小 */
  }
  to {
    opacity: 1;
    transform: scale(1); /* 结束时正常大小 */
  }
}
</style>