// تحديث الوقت والتاريخ
function updateDateTime() {
    const now = new Date();
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    document.getElementById('datetime').textContent = now.toLocaleDateString('ar-SA', options);
}

// تغيير اللغة
function changeLanguage(lang) {
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    
    const elements = document.querySelectorAll('[data-translate]');
    elements.forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
    
    localStorage.setItem('preferred-language', lang);
}

// تبديل الوضع الليلي
function toggleTheme() {
    const isDark = document.body.getAttribute('data-theme') === 'dark';
    document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
    localStorage.setItem('theme', isDark ? 'light' : 'dark');
}

// إضافة وظيفة التنبيه عند النقر على زر التوجيه
function redirectWithAlert() {
    const currentLang = document.documentElement.lang || 'ar';
    const alertText = translations[currentLang].alertMessage;
    const savedUrl = localStorage.getItem('websiteUrl') || 'http://t.com';
    
    if (confirm(alertText)) {
        window.location.href = savedUrl;
    }
}

// إضافة وظيفة الخروج
function exitApp() {
    const currentLang = document.documentElement.lang || 'ar';
    if (confirm(translations[currentLang].exitConfirm)) {
        window.close();
        // إذا لم تعمل window.close() (في معظم المتصفحات الحديثة)
        // يمكن توجيه المستخدم إلى صفحة خروج خاصة
        if (window.location.href === window.location.href) {
            window.location.href = 'about:blank';
        }
    }
}

// وظائف الإعدادات
function openSettings() {
    const modal = document.getElementById('settingsModal');
    const urlInput = document.getElementById('websiteUrl');
    urlInput.value = localStorage.getItem('websiteUrl') || 'http://t.com';
    modal.style.display = 'block';
}

function closeSettings() {
    const modal = document.getElementById('settingsModal');
    modal.style.display = 'none';
}

function saveSettings() {
    const urlInput = document.getElementById('websiteUrl');
    const url = urlInput.value.trim();
    
    if (url) {
        localStorage.setItem('websiteUrl', url);
        const currentLang = document.documentElement.lang || 'ar';
        alert(translations[currentLang].urlSaved);
        closeSettings();
    }
}

// تهيئة الصفحة
document.addEventListener('DOMContentLoaded', () => {
    // استعادة اللغة المفضلة
    const preferredLanguage = localStorage.getItem('preferred-language') || 'ar';
    changeLanguage(preferredLanguage);
    
    // استعادة الوضع المفضل
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    // إعداد مستمع لزر تبديل الوضع
    document.getElementById('themeToggle').addEventListener('click', toggleTheme);
    
    // إضافة مستمع لزر التوجيه
    document.querySelector('.redirect-btn').onclick = function(e) {
        e.preventDefault();
        redirectWithAlert();
    };
    
    // بدء تحديث الوقت
    updateDateTime();
    setInterval(updateDateTime, 60000);

    // تحديث نص WhatsApp في التحميل وعند تغيير اللغة
    function updateWhatsAppText() {
        const currentLang = document.documentElement.lang || 'ar';
        const whatsappBtn = document.querySelector('.whatsapp-btn');
        if (whatsappBtn) {
            const icon = whatsappBtn.querySelector('i');
            whatsappBtn.innerHTML = '';
            whatsappBtn.appendChild(icon);
            whatsappBtn.appendChild(document.createTextNode(' ' + translations[currentLang].whatsappContact));
        }
    }
    
    // إضافة تحديث نص WhatsApp إلى وظيفة تغيير اللغة
    const originalChangeLanguage = changeLanguage;
    changeLanguage = function(lang) {
        originalChangeLanguage(lang);
        updateWhatsAppText();
    };
    
    // تحديث النص عند التحميل
    updateWhatsAppText();
});

// إغلاق النافذة عند النقر خارجها
window.onclick = function(event) {
    const modal = document.getElementById('settingsModal');
    if (event.target === modal) {
        closeSettings();
    }
};
