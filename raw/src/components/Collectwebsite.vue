<template>
    
    <div class="floating-button-window">
        <h1>工具网站</h1>
      <div class="button-grid">
        <!-- 示例链接，您需要根据实际需求替换 URL -->
        <a href="https://www.dayi.org.cn/" target="_blank" class="grid-item">中国医药信息查询平台
        </a>
        <a href="https://goblin.tools/" target="_blank" class="grid-item">AI语气转换</a>
        <a href="https://report.seedsufe.com/#/report" target="_blank" class="grid-item">报告查询网</a>
        <a href="https://www.sony.net/united/clock/heritage/westminster/" target="_blank" class="grid-item">SONY云观景</a>
        <a href="https://temp-mail.org/zh/" target="_blank" class="grid-item">临时电子邮箱</a>
        <a href="https://bongo.cat/" target="_blank" class="grid-item">猫猫演奏家</a>
        <a href="https://zoom.earth/maps/satellite/" target="_blank" class="grid-item">在线云图</a>
        <a href="https://www.tianxun.com/" target="_blank" class="grid-item">航班查询</a>
        <a href="https://flightadsb.variflight.com/tracker/" target="_blank" class="grid-item">实时航班轨迹</a>
        <a href="https://magiconch.com/vaporwave/?from=home" target="_blank" class="grid-item">蒸汽波转换器</a>
        <!-- 继续添加更多链接，总共 10 个 -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Collectwebsite",
  };
  </script>
  
  <style scoped>
 .floating-button-window {
    background-image: url('../assets/image/tools2.jpg'); /* 设置背景图片 */
    background-size: cover; /* 背景图片覆盖整个元素 */
    background-position: center; /* 背景图片居中显示 */
    background-repeat: no-repeat; /* 背景图片不重复 */
    color: #030303; /* 文字颜色 */
    position: fixed;
    top: 50%;
    left: 60%;
    transform: translate(-50%, -50%); /* 居中定位 */
    width: 70%; /* 宽度调整为视口宽度的90% */
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
    position: fixed;
    bottom: 10px;
    right: 10px;
    z-index: 1000;
    max-height: 300px; /* 根据按钮数量调整高度，确保显示 5 行 */
    overflow-y: auto;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.button-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 创建 2 列 */
  gap: 10px; /* 网格项之间的间隙 */
}

.grid-item {
  display: block; /* 使链接填充整个网格单元格 */
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  text-align: center; /* 使文本居中 */
  text-decoration: none; /* 移除下划线 */
  transition: background-color 0.3s;
}

.grid-item:hover {
  background-color: #0056b3;
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