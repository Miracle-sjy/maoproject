from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# 指定 WebDriver 的路径
chromedriver_path = 'chromedriver.exe'  # 替换为你的 ChromeDriver 路径

# 设置 Service
service = Service(executable_path=chromedriver_path)

# 设置 WebDriver
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("https://office.teacher.com.cn/views/loginAndRegister/login/login.html")
# 替换为你想要检查的网页地址
print("20秒内请打开课时窗口，60秒后开始检测验证码 Ctrl+C或者关闭窗口结束程序")
time.sleep(20)
try:
    while True:
        try:
            # 获取打开的多个窗口句柄
            windows = driver.window_handles
            # 切换到当前最新打开的窗口
            driver.switch_to.window(windows[-1])

            # 等待一分钟
            time.sleep(60)

            # 使用 XPath 定位元素
            element = driver.find_element(By.XPATH, '//*[@id="codespan"]')  # 替换为你的 XPath 表达式

            # 获取元素的文本值
            text = element.text.strip()
            print("检测到的验证码是" + text)

            # 定位输入框并输入数字
            input_element = driver.find_element(By.XPATH, '//*[@id="code"]')  # 替换为你的输入框XPath表达式
            input_element.clear()
            input_element.send_keys(text)
            time.sleep(1)
            # 定位提交按钮并点击
            submit_button = driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-page newLayer layer-anim"]//a')  # 替换为你的提交按钮XPath表达式
            submit_button.click()
            print("验证码已提交")

        except NoSuchElementException:
            print("未找到验证码，跳过本次循环")
            continue  # 如果元素未找到，也跳过当前循环的剩余部分



except KeyboardInterrupt:
    # 如果需要停止循环，可以按 Ctrl+C
    print("循环被用户中断")

finally:
    # 关闭浏览器
    driver.quit()