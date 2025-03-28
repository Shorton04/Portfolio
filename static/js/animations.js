// static/js/animations.js

document.addEventListener('DOMContentLoaded', function() {
    // Add animation class to theme toggle button
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            const themeIcon = document.getElementById('theme-icon');
            themeIcon.classList.add('theme-toggle-spin');

            // Remove class after animation completes
            setTimeout(function() {
                themeIcon.classList.remove('theme-toggle-spin');
            }, 500);
        });
    }

    // Set up Intersection Observer for animation on scroll
    const animatedElements = document.querySelectorAll(
        '.animate-fade-in, .animate-slide-left, .animate-slide-right'
    );

    // Initially set elements invisible
    animatedElements.forEach(element => {
        element.style.opacity = '0';
    });

    const animationObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Keep the original animation class that was assigned
                entry.target.style.opacity = '1';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    // Observe each animated element
    animatedElements.forEach(element => {
        animationObserver.observe(element);
    });

    // Add animation classes to section titles
    const sectionTitles = document.querySelectorAll('section h1, section h2, section .lead');
    sectionTitles.forEach(title => {
        if (!title.classList.contains('animate-fade-in') &&
            !title.classList.contains('animate-slide-left') &&
            !title.classList.contains('animate-slide-right')) {
            title.classList.add('animate-fade-in');
        }
    });

    // Add animation classes to project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        if (index % 2 === 0) {
            card.classList.add('animate-slide-left');
        } else {
            card.classList.add('animate-slide-right');
        }
    });

    // Add animation to skill cards
    const skillCards = document.querySelectorAll('.skill-icon');
    skillCards.forEach(card => {
        card.classList.add('animate-fade-in');
    });

    // Add pulse animation to primary CTA buttons
    const primaryCTAs = document.querySelectorAll('.btn-primary');
    primaryCTAs.forEach(btn => {
        btn.classList.add('animate-pulse');
    });

    // Remove animation classes on mobile devices for better performance
    function checkMobile() {
        if (window.innerWidth < 768) {
            document.querySelectorAll('.animate-fade-in, .animate-slide-left, .animate-slide-right').forEach(el => {
                el.style.opacity = '1';
                el.style.transform = 'none';
                el.style.animation = 'none';
            });
        }
    }

    // Check on load and resize
    checkMobile();
    window.addEventListener('resize', checkMobile);
});