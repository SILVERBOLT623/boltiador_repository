// ── Nav scroll state ─────────────────────────────────────────
const nav = document.querySelector('.nav');
if (nav) {
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// ── Mobile nav toggle ─────────────────────────────────────────
const toggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const bars = toggle.querySelectorAll('span');
    const isOpen = navLinks.classList.contains('open');
    bars[0].style.transform = isOpen ? 'rotate(45deg) translate(5px, 5px)' : '';
    bars[1].style.opacity   = isOpen ? '0' : '';
    bars[2].style.transform = isOpen ? 'rotate(-45deg) translate(5px, -5px)' : '';
  });
  // Close on link click
  navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    navLinks.classList.remove('open');
  }));
}

// ── Skill bar animation (Intersection Observer) ───────────────
const skillFills = document.querySelectorAll('.skill-fill');
if (skillFills.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        el.style.width = el.dataset.width + '%';
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.3 });
  skillFills.forEach(el => observer.observe(el));
}

// ── Scroll-reveal for cards ───────────────────────────────────
const revealItems = document.querySelectorAll('.project-card, .skill-category, .edu-item');
if (revealItems.length) {
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        entry.target.style.animationDelay = (i * 0.08) + 's';
        entry.target.classList.add('fade-up');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  revealItems.forEach(el => revealObserver.observe(el));
}

// ── Smooth active link highlight ──────────────────────────────
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(a => {
  const href = a.getAttribute('href');
  const isHome = href === '/' && (currentPath === '/' || currentPath === '');
  const isActive = !isHome && href !== '/' && currentPath.startsWith(href);
  if (isHome || isActive) a.classList.add('active');
});
