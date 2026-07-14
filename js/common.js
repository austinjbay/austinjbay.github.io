document.addEventListener("DOMContentLoaded", function() {
  'use strict';

  var html = document.querySelector('html'),
    menuOpenIcon = document.querySelector(".icon__menu"),
    menuCloseIcon = document.querySelector(".nav__icon-close"),
    menuList = document.querySelector(".main-nav"),
    searchOpenIcon = document.querySelector(".icon__search"),
    searchCloseIcon = document.querySelector(".search__close"),
    searchInput = document.querySelector(".search__text"),
    search = document.querySelector(".search"),
    searchBox = document.querySelector(".search__box"),
    toggleTheme = document.querySelector(".toggle-theme"),
    btnScrollToTop = document.querySelector(".top");


  /* =======================================================
  // Menu + Search + Theme Switcher
  ======================================================= */
  menuOpenIcon.addEventListener("click", () => {
    menuOpen();
  });

  menuCloseIcon.addEventListener("click", () => {
    menuClose();
  });

  function menuOpen() {
    menuList.classList.add("is-open");
  }
  
  function menuClose() {
    menuList.classList.remove("is-open");
  }

  searchOpenIcon.addEventListener("click", () => {
    searchOpen();
  });

  searchCloseIcon.addEventListener("click", () => {
    searchClose();
  });

  function searchOpen() {
    search.classList.add("is-visible");
    setTimeout(function () {
      searchInput.focus();
    }, 250);
  }

  function searchClose() {
    search.classList.remove("is-visible");
  }

  searchBox.addEventListener("keydown", function(event) {
    if (event.target == this || event.keyCode == 27) {
      search.classList.remove('is-visible');
    }
  });

  if (toggleTheme) {
    toggleTheme.addEventListener("click", () => {
      darkMode();
    });
  };


  // Theme Switcher
  function darkMode() {
    if (html.classList.contains('dark-mode')) {
      html.classList.remove('dark-mode');
      localStorage.removeItem("theme");
      document.documentElement.removeAttribute("dark");
    } else {
      html.classList.add('dark-mode');
      localStorage.setItem("theme", "dark");
      document.documentElement.setAttribute("dark", "");
    }
  }


  // =====================
  // Simple Jekyll Search
  // =====================
  SimpleJekyllSearch({
    searchInput: document.getElementById("js-search-input"),
    resultsContainer: document.getElementById("js-results-container"),
    json: "/search.json",
    searchResultTemplate: '{article}',
    noResultsText: '<h3 class="no-results">No results found</h3>'
  });


  /* =======================
  // Responsive Videos
  ======================= */
  reframe(".post__content iframe:not(.reframe-off), .page__content iframe:not(.reframe-off)");


  /* =======================
  // LazyLoad Images
  ======================= */
  var lazyLoadInstance = new LazyLoad({
    elements_selector: ".lazy"
  })


  /* =======================
  // Zoom Image
  ======================= */
  const lightense = document.querySelector(".page__content img, .post__content img, .gallery__image img"),
  imageLink = document.querySelectorAll(".page__content a img, .post__content a img, .gallery__image a img");

  if (imageLink) {
    for (var i = 0; i < imageLink.length; i++) imageLink[i].parentNode.classList.add("image-link");
    for (var i = 0; i < imageLink.length; i++) imageLink[i].classList.add("no-lightense");
  }

  if (lightense) {
    Lightense(".page__content img:not(.no-lightense), .post__content img:not(.no-lightense), .gallery__image img:not(.no-lightense)", {
    padding: 60,
    offset: 30
    });
  }



  /* =======================
  // Homepage Hero Lottie
  ======================= */
  const heroLottie = document.querySelector("[data-hero-lottie]");

  if (heroLottie) {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    const staticHero = window.matchMedia("(max-width: 576px)");
    let heroAnimation;
    let heroObserver;

    function heroLottiePath() {
      const isDark = document.documentElement.hasAttribute("dark") || document.documentElement.classList.contains("dark-mode");
      return isDark ? heroLottie.dataset.darkSrc : heroLottie.dataset.lightSrc;
    }

    function destroyHeroAnimation() {
      if (heroAnimation) {
        heroAnimation.destroy();
        heroAnimation = null;
      }
      heroLottie.classList.remove("is-loaded");
    }

    function loadHeroAnimation() {
      if (reduceMotion.matches || staticHero.matches || typeof lottie === "undefined") {
        destroyHeroAnimation();
        return;
      }

      destroyHeroAnimation();
      heroAnimation = lottie.loadAnimation({
        container: heroLottie,
        renderer: "svg",
        loop: true,
        autoplay: false,
        path: heroLottiePath(),
        rendererSettings: {
          preserveAspectRatio: "xMidYMid meet",
          progressiveLoad: true
        }
      });

      heroAnimation.addEventListener("DOMLoaded", function() {
        heroLottie.classList.add("is-loaded");
      });
    }

    loadHeroAnimation();

    if ("IntersectionObserver" in window) {
      heroObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (!heroAnimation) {
            return;
          }
          if (entry.isIntersecting) {
            heroAnimation.play();
          } else {
            heroAnimation.pause();
          }
        });
      }, { threshold: 0.2 });
      heroObserver.observe(heroLottie);
    } else if (heroAnimation) {
      heroAnimation.play();
    }

    if (reduceMotion.addEventListener) {
      reduceMotion.addEventListener("change", loadHeroAnimation);
    }

    if (staticHero.addEventListener) {
      staticHero.addEventListener("change", loadHeroAnimation);
    }

    const heroThemeObserver = new MutationObserver(function() {
      loadHeroAnimation();
    });
    heroThemeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ["class", "dark"] });
  }


  /* =================================
  // Smooth scroll to the tags page
  ================================= */
  document.querySelectorAll(".tag__link, .top__link").forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });


  /* =======================
  // Scroll Top Button
  ======================= */
  btnScrollToTop.addEventListener("click", function () {
    if (window.scrollY != 0) {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
      })
    }
  });

});