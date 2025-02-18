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

def main():
    sizes = [72, 192, 512]
    for size in sizes:
        create_icon(size, 'T', f'icon-{size}x{size}.png')
    print("\nتم إنشاء جميع الأيقونات بنجاح!")

if __name__ == '__main__':
    main()
