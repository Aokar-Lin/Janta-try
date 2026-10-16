/* Janta — main.js (no dependencies) */
(function () {
  "use strict";
  var doc = document.documentElement;

  /* ---------- Sticky header shadow ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = doc.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open);
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { doc.classList.remove("nav-open", "filters-open"); toggle.setAttribute("aria-expanded", "false"); }
    });
    window.addEventListener("resize", function () { if (window.innerWidth >= 1024) doc.classList.remove("nav-open"); });
  }

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Buy Now: product details window ---------- */
  (function buyNow() {
    var dataEl = document.getElementById("product-data");
    var dlg = document.getElementById("buy-now");
    if (!dataEl || !dlg || typeof dlg.showModal !== "function") return; // falls back to the product page link

    var D = JSON.parse(dataEl.textContent);
    var $ = function (k) { return dlg.querySelector('[data-qv="' + k + '"]'); };
    var current = null, qty = 1, fromPop = false;
    var minus = dlg.querySelector('[data-qty="-1"]');
    var plus = dlg.querySelector('[data-qty="1"]');

    function npr(n) {
      var s = String(Math.round(n)), last3 = s.slice(-3), rest = s.slice(0, -3);
      if (rest) last3 = rest.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + "," + last3;
      return "Rs. " + last3;
    }

    var sel = [];
    var optBox = $("options");

    function unit() {
      var add = 0;
      current.options.forEach(function (g, i) { add += g.values[sel[i]].add || 0; });
      return add;
    }

    function fmtAdd(a) { return (a > 0 ? "+" : "−") + npr(Math.abs(a)).slice(4); }

    function renderOptions() {
      optBox.innerHTML = "";
      current.options.forEach(function (g, gi) {
        var fs = document.createElement("fieldset");
        fs.className = "opt-group" + (g.kind === "colour" ? " is-colour" : "");
        var lg = document.createElement("legend");
        lg.innerHTML = '<span></span>: <b></b>';
        lg.firstChild.textContent = g.name;
        fs.appendChild(lg);
        var list = document.createElement("div");
        list.className = "opt-list";
        g.values.forEach(function (v, vi) {
          var lab = document.createElement("label");
          lab.className = g.kind === "colour" ? "opt-swatch" : "opt-pill";
          var inp = document.createElement("input");
          inp.type = "radio"; inp.name = "qv-opt-" + gi; inp.value = vi; inp.checked = vi === sel[gi];
          inp.addEventListener("change", function () { sel[gi] = vi; updateOrder(); });
          var box = document.createElement("span");
          box.className = "box";
          if (g.kind === "colour") {
            box.style.setProperty("--c", v.hex);
            lab.title = v.label + (v.add ? " (" + fmtAdd(v.add) + ")" : "");
            var sr = document.createElement("span"); sr.className = "visually-hidden"; sr.textContent = v.label;
            box.appendChild(sr);
          } else {
            var t = document.createElement("span"); t.textContent = v.label; box.appendChild(t);
            if (v.add) { var sm = document.createElement("small"); sm.textContent = fmtAdd(v.add); box.appendChild(sm); }
          }
          lab.appendChild(inp); lab.appendChild(box); list.appendChild(lab);
        });
        fs.appendChild(list);
        optBox.appendChild(fs);
      });
      optBox.hidden = !current.options.length;
    }

    function updateOrder() {
      var p = current, add = unit(), price = p.price + add, img = p.img, chosen = [];
      // legends + selected image
      Array.prototype.forEach.call(optBox.querySelectorAll("legend b"), function (b, i) {
        b.textContent = p.options[i].values[sel[i]].label;
      });
      p.options.forEach(function (g, i) {
        var v = g.values[sel[i]];
        if (v.img) img = v.img;
        chosen.push(g.name + ": " + v.label);
      });
      var el = $("img"), src = D.root + img;
      if (el.getAttribute("src") !== src) { el.classList.remove("swap"); void el.offsetWidth; el.classList.add("swap"); el.src = src; }
      $("price").textContent = npr(price);
      $("old").textContent = p.old ? npr(p.old + add) : "";
      $("save").textContent = p.old ? "Save " + npr(p.old - p.price) : "";
      $("qty").textContent = qty;
      minus.disabled = qty <= 1;
      plus.disabled = qty >= 10;
      $("total").textContent = npr(price * qty);
      var msg = "Hello Janta! I'd like to buy:\n\n" +
        "Product: " + p.name + "\n" +
        "Brand: " + p.brand + "\n" +
        (chosen.length ? chosen.join("\n") + "\n" : "") +
        "Price: " + npr(price) + "\n" +
        "Quantity: " + qty + "\n" +
        "Total: " + npr(price * qty) + "\n\n" +
        p.url + "\n\nIs it available?";
      $("wa").href = "https://wa.me/" + D.wa + "?text=" + encodeURIComponent(msg);
    }

    function open(slug, push) {
      var p = D.items[slug];
      if (!p) return false;
      current = p; qty = 1;
      sel = p.options.map(function () { return 0; });
      var img = $("img");
      img.alt = p.name;
      var b = $("badge");
      b.hidden = !p.badge; b.textContent = p.badge || "";
      b.className = "badge" + (p.badge === "Sale" ? " sale" : p.badge === "Hot" ? " hot" : "");
      $("brand").textContent = p.brand + " · " + p.type;
      $("name").textContent = p.name;
      $("desc").textContent = p.desc;
      var dl = $("specs"); dl.innerHTML = "";
      p.specs.forEach(function (s) {
        var row = document.createElement("div"), dt = document.createElement("dt"), dd = document.createElement("dd");
        dt.textContent = s[0]; dd.textContent = s[1];
        row.appendChild(dt); row.appendChild(dd); dl.appendChild(row);
      });
      $("page").href = D.root + p.page;
      renderOptions();
      updateOrder();
      if (!dlg.open) dlg.showModal();
      dlg.scrollTop = 0;
      doc.style.overflow = "hidden";
      if (push && history.pushState) history.pushState({ buy: slug }, "", location.pathname + location.search + "#buy-" + slug);
      return true;
    }

    // Open from any Buy Now button (ctrl/cmd-click still opens the full product page)
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("[data-buy]") : null;
      if (!a || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
      if (open(a.getAttribute("data-buy"), true)) e.preventDefault();
    });

    dlg.querySelectorAll("[data-qty]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        qty = Math.min(10, Math.max(1, qty + Number(btn.getAttribute("data-qty"))));
        updateOrder();
      });
    });

    dlg.querySelector("[data-qv-close]").addEventListener("click", function () { dlg.close(); });
    // Click on the dark backdrop closes the window
    dlg.addEventListener("click", function (e) {
      if (e.target !== dlg) return;
      var r = dlg.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
    });
    dlg.addEventListener("close", function () {
      doc.style.overflow = "";
      if (fromPop) { fromPop = false; return; }
      if (history.state && history.state.buy) history.back();
      else if (location.hash.indexOf("#buy-") === 0 && history.replaceState) history.replaceState(null, "", location.pathname + location.search);
    });
    // Phone "back" button closes the window instead of leaving the page
    window.addEventListener("popstate", function () {
      if (dlg.open) { fromPop = true; dlg.close(); }
      else if (location.hash.indexOf("#buy-") === 0) open(location.hash.slice(5), false);
    });
    // Shareable link: page.html#buy-iphone-16 opens that product directly
    if (location.hash.indexOf("#buy-") === 0) open(location.hash.slice(5), false);
  })();

  /* ---------- Shop: filter, search, sort ---------- */
  var shop = document.getElementById("shop");
  if (!shop) return;

  var grid = shop.querySelector("[data-grid]");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".product-card"));
  var boxes = Array.prototype.slice.call(shop.querySelectorAll('input[name="filter"]'));
  var search = document.getElementById("q");
  var sort = document.getElementById("sort");
  var countEl = shop.querySelector("[data-count]");
  var empty = shop.querySelector(".empty-state");
  var chips = shop.querySelector(".active-chips");
  var fToggle = shop.querySelector(".filter-toggle");
  var fCount = shop.querySelector(".fcount");

  // Read state from URL (?filter=apple,samsung&q=pro&sort=price-asc)
  var params = new URLSearchParams(location.search);
  var initial = (params.get("filter") || "").split(",").filter(Boolean);
  boxes.forEach(function (b) { b.checked = initial.indexOf(b.value) !== -1; });
  if (params.get("q")) search.value = params.get("q");
  if (params.get("sort")) sort.value = params.get("sort");

  function labelFor(val) {
    var b = boxes.filter(function (x) { return x.value === val; })[0];
    return b ? b.parentNode.querySelector("span").textContent : val;
  }

  function apply(updateUrl) {
    var selected = boxes.filter(function (b) { return b.checked; }).map(function (b) { return b.value; });
    var q = search.value.trim().toLowerCase();
    var terms = q.split(/\s+/).filter(Boolean);
    var shown = 0;

    cards.forEach(function (c) {
      var okFilter = !selected.length || selected.indexOf(c.dataset.key) !== -1;
      var name = c.dataset.name;
      var okSearch = terms.every(function (t) { return name.indexOf(t) !== -1; });
      var show = okFilter && okSearch;
      c.hidden = !show;
      if (show) shown++;
    });

    // Sort
    var mode = sort.value;
    var sorted = cards.slice().sort(function (a, b) {
      if (mode === "price-asc") return a.dataset.price - b.dataset.price;
      if (mode === "price-desc") return b.dataset.price - a.dataset.price;
      if (mode === "name") return a.dataset.name.localeCompare(b.dataset.name);
      return a.dataset.order - b.dataset.order;
    });
    sorted.forEach(function (c) { grid.appendChild(c); });

    countEl.textContent = shown;
    empty.hidden = shown !== 0;
    grid.hidden = shown === 0;
    fCount.textContent = selected.length ? selected.length : "";

    // Active chips
    chips.innerHTML = "";
    selected.forEach(function (v) {
      var chip = document.createElement("span");
      chip.className = "chip";
      chip.textContent = labelFor(v);
      var x = document.createElement("button");
      x.type = "button";
      x.setAttribute("aria-label", "Remove filter " + labelFor(v));
      x.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>';
      x.addEventListener("click", function () {
        boxes.forEach(function (b) { if (b.value === v) b.checked = false; });
        apply(true);
      });
      chip.appendChild(x);
      chips.appendChild(chip);
    });

    if (updateUrl && window.history.replaceState) {
      var p = new URLSearchParams();
      if (selected.length) p.set("filter", selected.join(","));
      if (q) p.set("q", q);
      if (mode !== "featured") p.set("sort", mode);
      var s = p.toString();
      history.replaceState(null, "", location.pathname + (s ? "?" + s : ""));
    }
  }

  boxes.forEach(function (b) { b.addEventListener("change", function () { apply(true); }); });
  sort.addEventListener("change", function () { apply(true); });
  var t;
  search.addEventListener("input", function () { clearTimeout(t); t = setTimeout(function () { apply(true); }, 120); });
  shop.querySelectorAll("[data-clear]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      boxes.forEach(function (b) { b.checked = false; });
      search.value = "";
      sort.value = "featured";
      apply(true);
    });
  });

  // Mobile filter drawer
  function setDrawer(open) {
    doc.classList.toggle("filters-open", open);
    fToggle.setAttribute("aria-expanded", open);
    document.body.style.overflow = open ? "hidden" : "";
  }
  fToggle.addEventListener("click", function () { setDrawer(true); });
  shop.querySelectorAll("[data-close-filters]").forEach(function (el) {
    el.addEventListener("click", function () { setDrawer(false); });
  });
  window.addEventListener("resize", function () { if (window.innerWidth >= 1024 && doc.classList.contains("filters-open")) setDrawer(false); });

  apply(false);
})();
