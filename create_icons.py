import os
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# الحصول على المسار الحالي للسكريبت
SCRIPT_DIR = Path(__file__).parent.absolute()

def create_icon(size, text, output_filename):
    # إنشاء صورة جديدة بخلفية زرقاء
    img = Image.new('RGB', (size, size), '#2196f3')
    draw = ImageDraw.Draw(img)
    
    # حجم الخط يتناسب مع حجم الأيقونة
    font_size = int(size * 0.6)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # وضع الحرف في وسط الصورة
    text_width = draw.textlength(text, font=font)
    text_height = font_size
    x = (size - text_width) / 2
    y = (size - text_height) / 2
    
    # رسم النص
    draw.text((x, y), text, fill='white', font=font)
    
    # إنشاء مجلد icons إذا لم يكن موجوداً
    icons_dir = SCRIPT_DIR / 'icons'
    icons_dir.mkdir(exist_ok=True)
    
    # حفظ الأيقونة
    output_path = icons_dir / output_filename
    img.save(output_path)
    print(f"تم إنشاء: {output_filename}")

def create_maskable_icon(size, text, output_filename):
    # إنشاء أيقونة مع هامش آمن للـ maskable
    padding = size * 0.1  # 10% padding
    img = Image.new('RGB', (size, size), '#2196f3')
    draw = ImageDraw.Draw(img)
    
    # حجم الخط أصغر للـ maskable
    font_size = int(size * 0.5)  # تقليل حجم الخط
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (size - text_width) / 2
    y = (size - text_height) / 2
    
    draw.text((x, y), text, fill='white', font=font)
    
    icons_dir = SCRIPT_DIR / 'icons'
    icons_dir.mkdir(exist_ok=True)
    
    output_path = icons_dir / output_filename
    img.save(output_path)
    print(f"تم إنشاء: {output_filename}")

def main():
    sizes = [72, 192, 512]
    for size in sizes:
        # إنشاء أيقونة عادية
        create_icon(size, 'T', f'icon-{size}x{size}.png')
        # إنشاء أيقونة maskable
        create_maskable_icon(size, 'T', f'icon-{size}x{size}-maskable.png')
    print("\nتم إنشاء جميع الأيقونات بنجاح!")

if __name__ == '__main__':
    main()
