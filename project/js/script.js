console.log("Hello, Solo Trae!");

// 简单的交互功能
document.addEventListener("DOMContentLoaded", function() {
    console.log("网页加载完成！");
    
    // 获取按钮和消息元素
    const greetButton = document.getElementById('greetButton');
    const greetMessage = document.getElementById('greetMessage');
    
    // 为按钮添加点击事件
    if (greetButton) {
        greetButton.addEventListener('click', function() {
            // 生成问候消息
            const messages = [
                '你好！欢迎使用Solo Trae Web Code！',
                '很高兴见到你！',
                '祝你学习愉快！',
                'Solo Trae是你的编程助手！',
                '加油，你可以的！'
            ];
            
            // 随机选择一条消息
            const randomMessage = messages[Math.floor(Math.random() * messages.length)];
            
            // 显示消息
            greetMessage.textContent = randomMessage;
            greetMessage.style.display = 'block';
            
            // 添加动画效果
            greetMessage.style.opacity = '0';
            greetMessage.style.transition = 'opacity 0.5s ease';
            
            setTimeout(() => {
                greetMessage.style.opacity = '1';
            }, 100);
            
            // 3秒后隐藏消息
            setTimeout(() => {
                greetMessage.style.opacity = '0';
                setTimeout(() => {
                    greetMessage.style.display = 'none';
                }, 500);
            }, 3000);
        });
    }
    
    // 添加页面加载动画
    const sections = document.querySelectorAll('.section');
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 100 * (index + 1));
    });
});