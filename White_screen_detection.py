import pyautogui
import time
from PIL import ImageGrab

# 定义屏幕检测函数
def detect_white_screen():
    # 获取屏幕尺寸
    screen_width, screen_height = pyautogui.size()

    # 截取整个屏幕的图像
    screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

    # 将截图转换为RGB模式
    screenshot = screenshot.convert('RGB')

    # 初始化计数器
    white_pixel_count = 0

    # 遍历图像的每个像素
    for x in range(screen_width):
        for y in range(screen_height):
            pixel = screenshot.getpixel((x, y))
            r, g, b = pixel
            # 如果像素是纯白的（R、G、B 均为 255），则增加计数器
            if r == 255 and g == 255 and b == 255:
                white_pixel_count += 1

    # 计算屏幕上纯白像素的百分比
    white_pixel_percentage = (white_pixel_count / (screen_width * screen_height)) * 100

    return white_pixel_percentage

# 主程序
if __name__ == "__main__":
    # 定义纯白像素的阈值
    white_threshold = 90.0

    while True:
        # 检测屏幕上的纯白像素百分比
        white_percentage = detect_white_screen()

        # 如果白色像素百分比大于阈值，执行打开某程序的操作
        if white_percentage >= white_threshold:
            # 这里可以添加打开程序的代码
            print("检测到")
        # 每隔一段时间进行检测（例如，每5秒检测一次）
        time.sleep(1)
