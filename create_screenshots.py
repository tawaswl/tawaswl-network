from PIL import Image, ImageDraw, ImageFont
import os

def create_screenshot(width, height, filename):
    # إنشاء صورة بخلفية متدرجة
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # رسم خلفية متدرجة
    for y in range(height):
        r = int((y / height) * (37 - 106) + 106)  # من #6a11cb إلى #2575fc
        g = int((y / height) * (117 - 17) + 17)
        b = int((y / height) * (252 - 203) + 203)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # إضافة نص "تواصل"
    try:
        font_size = int(min(width, height) * 0.2)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "تواصل"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill='white', font=font)
    
    # حفظ الصورة
    screenshots_dir = 'screenshots'
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    img.save(os.path.join(screenshots_dir, filename))
    print(f"تم إنشاء: {filename}")

def main():
    # إنشاء صورة سطح المكتب
    create_screenshot(1920, 1080, 'desktop.png')
    
    # إنشاء صورة الجوال
    create_screenshot(750, 1334, 'mobile.png')
    
    print("\nتم إنشاء جميع الصور بنجاح!")

if __name__ == '__main__':
    main()
