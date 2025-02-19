from PIL import Image
import os

def create_favicon():
    # افتح الأيقونة الحالية
    icon = Image.open('icons/icon-72x72.png')
    # حفظ كـ favicon.ico
    icon.save('favicon.ico')

if __name__ == '__main__':
    create_favicon()
