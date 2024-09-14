from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

# 指定 WebDriver 的路径
chromedriver_path = 'chromedriver.exe'  # 替换为你的 ChromeDriver 路径

# 设置 Service
service = Service(executable_path=chromedriver_path)

# 设置 WebDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("https://office.teacher.com.cn/views/loginAndRegister/login/login.html")

print("20秒后开始检测验证码 Ctrl+C或者关闭窗口结束程序")
time.sleep(20)

try:
    while True:
        # 使用 XPath 定位元素
        element = driver.find_element(By.XPATH, ' //*[@id="codespan"]/text()')  # 替换为你的 XPath 表达式

        # 获取元素的文本值
        text = element.text
        if not text.strip():  # 如果文本为空或只包含空白字符
            print("未检测到验证码，60s后再次检测")
        else:
            print("检测到的验证码是"+text)
            # 定位输入框并输入数字
            input_element = driver.find_element(By.XPATH, '//*[@id="code"]')  # 替换为你的输入框XPath表达式
            input_element.clear()
            input_element.send_keys(text)

            # 定位提交按钮并点击
            submit_button = driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a')  # 替换为你的提交按钮XPath表达式
            submit_button.click()
            print("验证码以提交")

        # 等待一分钟
        time.sleep(60)

except KeyboardInterrupt:
    # 如果需要停止循环，可以按 Ctrl+C
    print("程序被用户中断")


time.sleep(5)

# 关闭浏览器
driver.quit()