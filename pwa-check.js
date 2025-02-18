function checkPWA() {
    console.log('فحص إعدادات PWA...');
    
    // فحص Service Worker
    if ('serviceWorker' in navigator) {
        console.log('✅ Service Worker مدعوم');
        navigator.serviceWorker.getRegistrations().then(registrations => {
            console.log(`عدد Service Workers المسجلة: ${registrations.length}`);
        });
    }

    // فحص Manifest
    const manifestLink = document.querySelector('link[rel="manifest"]');
    if (manifestLink) {
        console.log('✅ تم العثور على ملف Manifest');
        fetch(manifestLink.href)
            .then(response => response.json())
            .then(manifest => {
                console.log('محتويات Manifest:', manifest);
            });
    }

    // فحص إمكانية التثبيت
    window.addEventListener('beforeinstallprompt', (e) => {
        console.log('✅ التطبيق قابل للتثبيت');
    });
}

// تشغيل الفحص عند تحميل الصفحة
window.addEventListener('load', checkPWA);
