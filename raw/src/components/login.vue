<template>
    <div class="login-container">
      <div class="login-form">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
          <div class="form-control" :class="{ error: errors.username }">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="loginForm.username" required />
            <span v-if="errors.username" class="error-message">{{ errors.username }}</span>
          </div>
          <div class="form-control" :class="{ error: errors.password }">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="loginForm.password" required />
            <span v-if="errors.password" class="error-message">{{ errors.password }}</span>
          </div>
          <button type="submit" :disabled="isSubmitting">Login</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        loginForm: {
          username: '',
          password: '',
        },
        errors: {},
        isSubmitting: false,
      };
    },
    methods: {
  handleLogin() {
    this.validateForm();
    if (Object.keys(this.errors).length === 0) {
      this.submitLoginForm();
    }
  },
  validateForm() {
    // 重置错误信息
    this.errors = {};

    // 用户名验证规则：至少5个字符，只包含大小写字母和数字
    const usernameRegex = /^(?=.*[A-Za-z0-9])([\w]){5,}$/;

    if (!this.loginForm.username.trim()) {
      this.errors.username = 'Username is required.';
    } else if (!usernameRegex.test(this.loginForm.username)) {
      this.errors.username = '请输入至少五个大小写字母或者数字';
    }

    // 密码验证规则：至少5个字符，只包含大小写字母和数字
    const passwordRegex = /^(?=.*[A-Za-z0-9])(?=.{5,})/;

    if (!this.loginForm.password) {
      this.errors.password = 'Password is required.';
    } else if (!passwordRegex.test(this.loginForm.password)) {
      this.errors.password = '请输入至少五个大小写字母或者数字';
    }
  },
  submitLoginForm() {
    this.isSubmitting = true;
    // 在这里添加登录逻辑，比如调用 API 并处理响应
    console.log('Login form submitted:', this.loginForm);

    // 假设登录请求成功，我们模拟一个延迟
    setTimeout(() => {
      this.isSubmitting = false;
      alert('欢迎回来!');
      // 登录成功后的操作
    }, 500);
  },
},
  };
  </script>

<style scoped>
/* 样式中添加 .error 和 .error-message 类的样式 */
.form-control.error input {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 0.8em;
}

.login-container {
  max-width: 300px;
  margin: 50px auto;
  transform: translate(-30%, -10%);
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);

  opacity: 0;
    animation: zoomIn 1s ease forwards;
    animation-delay: 0s,2s;
}

.login-form h2 {
  text-align: center;
  color: #fff;
}

.form-control {
  position: relative;
  margin-bottom: 20px;
}

.form-control label {
  position: absolute;
  top: -10px; /* 初始位置在输入框上方，稍微偏移 */
  left: 10px;
  color: #00dfc4; /* 标签颜色 */
  font-size: 16px;
  background: #1f242d; /* 与输入框背景色一致 */
  padding: 0 5px; /* 根据需要调整内边距 */
  border-radius: 3px; /* 圆角边框 */
  transition: all 0.3s ease;
  z-index: 1; /* 确保标签在输入框之上 */
}

.form-control input {
  width: 100%;
  padding: 10px;
  border: 1px solid #00dfc4;
  border-radius: 4px;
  outline: none;
  color: white; /* 输入字符颜色 */
  background: #1f242d; /* 输入框背景色 */
  font-size: 16px;
}


button {
  width: 100%;
  padding: 10px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
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
</style>