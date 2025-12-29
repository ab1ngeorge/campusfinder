import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LBS Campus Navigator",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    "<h2 style='text-align:center;margin-bottom:0;'>🎓 LBS Campus Navigator</h2>",
    unsafe_allow_html=True,
)
st.caption(
    "Tap a location card, share your location, and get Google Maps directions plus spoken route instructions."
)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #020617;
      --accent: #22c55e;
      --accent-soft: rgba(34, 197, 94, 0.15);
      --text: #e5e7eb;
      --muted: #9ca3af;
      --border: #1f2937;
      --shadow-soft: 0 18px 45px rgba(15, 23, 42, 0.65);
      --radius-xl: 18px;
      --radius-full: 999px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
        "Segoe UI", sans-serif;
    }

    body {
      min-height: 100vh;
      background: radial-gradient(circle at top, #1e293b, #020617 55%);
      color: var(--text);
      display: flex;
      justify-content: center;
      padding: 12px;
    }

    .app-shell {
      width: 100%;
      max-width: 960px;
      background: linear-gradient(145deg, #020617, #020617, #020617);
      border-radius: 28px;
      border: 1px solid rgba(148, 163, 184, 0.08);
      box-shadow: var(--shadow-soft);
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: 24px;
      background: radial-gradient(circle at top left, #1d283a, #020617);
      border: 1px solid rgba(148, 163, 184, 0.16);
    }

    .title {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .title-main {
      font-size: 1.1rem;
      font-weight: 650;
      letter-spacing: 0.03em;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .title-main span.badge {
      font-size: 0.55rem;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.5);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }

    .title-sub {
      font-size: 0.7rem;
      color: var(--muted);
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(34, 197, 94, 0.3);
      font-size: 0.7rem;
      color: var(--muted);
      white-space: nowrap;
    }

    .status-dot {
      width: 8px;
      height: 8px;
      border-radius: 999px;
      background: radial-gradient(circle at center, #4ade80, #22c55e);
      box-shadow: 0 0 12px rgba(34, 197, 94, 0.85);
    }

    .status-text strong {
      color: var(--accent);
      font-weight: 600;
    }

    .status-divider {
      width: 1px;
      height: 12px;
      background: linear-gradient(to bottom, transparent, #334155, transparent);
    }

    .status-chip {
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.4);
      font-size: 0.6rem;
      text-transform: uppercase;
      letter-spacing: 0.09em;
    }

    .controls-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      padding: 8px 12px 4px;
    }

    .pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.96);
      border: 1px solid rgba(148, 163, 184, 0.3);
      font-size: 0.7rem;
      color: var(--muted);
    }

    .pill-dot {
      width: 8px;
      height: 8px;
      border-radius: 999px;
      background: var(--accent);
    }

    .pill strong {
      color: var(--text);
      font-weight: 600;
    }

    .btn-primary {
      margin-left: auto;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 11px;
      border-radius: 999px;
      border: 1px solid rgba(34, 197, 94, 0.6);
      background: radial-gradient(circle at top, rgba(34, 197, 94, 0.18), rgba(15, 23, 42, 0.95));
      color: var(--accent);
      font-size: 0.72rem;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.18s ease, transform 0.08s ease, box-shadow 0.18s ease;
      box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.9), 0 10px 25px rgba(34, 197, 94, 0.35);
    }

    .btn-primary:hover {
      background: radial-gradient(circle at top, rgba(34, 197, 94, 0.26), rgba(15, 23, 42, 0.98));
      transform: translateY(-0.5px);
      box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.95), 0 14px 28px rgba(34, 197, 94, 0.48);
    }

    .btn-primary:active {
      transform: translateY(0.5px) scale(0.99);
      box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.9), 0 8px 18px rgba(34, 197, 94, 0.28);
    }

    .main {
      display: grid;
      grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
      gap: 12px;
    }

    .card {
      background: radial-gradient(circle at top left, #0b1220, #020617);
      border-radius: var(--radius-xl);
      border: 1px solid rgba(148, 163, 184, 0.15);
      padding: 12px;
      box-shadow: 0 18px 40px rgba(15, 23, 42, 0.9);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      color: var(--muted);
    }

    .card-header strong {
      color: var(--text);
      font-size: 0.8rem;
    }

    .search-box {
      position: relative;
      margin-top: 3px;
    }

    .search-input {
      width: 100%;
      padding: 7px 26px;
      border-radius: 999px;
      border: 1px solid rgba(51, 65, 85, 0.7);
      background: rgba(15, 23, 42, 0.96);
      color: var(--text);
      font-size: 0.75rem;
      outline: none;
    }

    .search-input::placeholder {
      color: rgba(148, 163, 184, 0.8);
    }

    .search-icon {
      position: absolute;
      left: 9px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 0.72rem;
      color: rgba(148, 163, 184, 0.9);
    }

    .list {
      max-height: 360px;
      overflow-y: auto;
      padding-right: 4px;
      scrollbar-width: thin;
      scrollbar-color: #4b5563 transparent;
    }

    .list::-webkit-scrollbar {
      width: 5px;
    }

    .list::-webkit-scrollbar-track {
      background: transparent;
    }

    .list::-webkit-scrollbar-thumb {
      background: #4b5563;
      border-radius: 999px;
    }

    .section-label {
      margin-top: 4px;
      margin-bottom: 4px;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: rgba(148, 163, 184, 0.9);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .section-label span.dot {
      width: 5px;
      height: 5px;
      border-radius: 999px;
      background: rgba(148, 163, 184, 0.8);
    }

    .place-card {
      border-radius: 14px;
      border: 1px solid rgba(30, 64, 175, 0.5);
      background: radial-gradient(circle at top left, rgba(15, 23, 42, 0.9), #020617 60%);
      padding: 9px 10px;
      margin-bottom: 6px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      gap: 8px;
      transition: border-color 0.16s ease, transform 0.06s ease, box-shadow 0.16s ease, background 0.16s ease;
    }

    .place-card:hover {
      border-color: rgba(59, 130, 246, 0.85);
      box-shadow: 0 10px 26px rgba(15, 23, 42, 0.85);
      transform: translateY(-0.5px);
      background: radial-gradient(circle at top left, rgba(15, 23, 42, 0.95), #020617 70%);
    }

    .place-card:active {
      transform: translateY(0.5px) scale(0.995);
      box-shadow: 0 8px 18px rgba(15, 23, 42, 0.7);
    }

    .place-main {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .place-category {
      font-size: 0.67rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: rgba(148, 163, 184, 0.9);
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .pill-mini {
      padding: 2px 7px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(148, 163, 184, 0.5);
      font-size: 0.6rem;
      color: var(--muted);
    }

    .place-name {
      font-size: 0.86rem;
      font-weight: 550;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .place-meta {
      font-size: 0.68rem;
      color: rgba(148, 163, 184, 0.9);
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .pill-verified {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(34, 197, 94, 0.6);
      background: rgba(22, 163, 74, 0.1);
      font-size: 0.6rem;
      color: #bbf7d0;
    }

    .pill-verified span.dot {
      width: 6px;
      height: 6px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 10px rgba(22, 163, 74, 0.9);
    }

    .pill-link {
      font-size: 0.64rem;
      color: rgba(96, 165, 250, 0.95);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .pill-link span.icon {
      font-size: 0.8rem;
    }

    .place-action {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      justify-content: space-between;
      gap: 4px;
      font-size: 0.62rem;
      color: var(--muted);
      text-align: right;
      min-width: 68px;
    }

    .chip {
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.5);
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }

    .chip-go {
      border-color: rgba(34, 197, 94, 0.8);
      color: #bbf7d0;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .chip-go span.icon {
      font-size: 0.75rem;
    }

    .secondary-text {
      font-size: 0.62rem;
      color: rgba(148, 163, 184, 0.85);
    }

    .action-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 6px;
      font-size: 0.7rem;
      color: var(--muted);
    }

    .chip-ghost {
      padding: 3px 8px;
      border-radius: 999px;
      border: 1px dashed rgba(148, 163, 184, 0.5);
    }

    .chip-ghost strong {
      color: var(--text);
      font-weight: 500;
    }

    .chip-soft {
      padding: 3px 8px;
      border-radius: 999px;
      border: 1px solid rgba(59, 130, 246, 0.55);
      background: rgba(37, 99, 235, 0.12);
      color: rgba(191, 219, 254, 0.98);
    }

    .status-text-small {
      font-size: 0.66rem;
      color: rgba(148, 163, 184, 0.9);
    }

    .status-text-small strong {
      color: var(--accent);
    }

    .mini-pill {
      padding: 2px 6px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.35);
      font-size: 0.6rem;
      color: rgba(148, 163, 184, 0.9);
    }

    .status-banner {
      padding: 8px 9px;
      border-radius: 14px;
      border: 1px solid rgba(148, 163, 184, 0.35);
      background: radial-gradient(circle at right, rgba(37, 99, 235, 0.34), rgba(15, 23, 42, 0.96));
      font-size: 0.7rem;
      color: var(--muted);
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    .status-banner strong {
      color: var(--text);
    }

    .banner-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .banner-chip {
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(148, 163, 184, 0.6);
      font-size: 0.6rem;
      text-transform: uppercase;
      letter-spacing: 0.11em;
      color: rgba(191, 219, 254, 0.98);
    }

    .banner-body {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .badge-inline {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .badge-inline span.dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 12px rgba(34, 197, 94, 0.9);
    }

    #status {
      font-size: 0.68rem;
      color: rgba(148, 163, 184, 0.97);
    }

    #status strong {
      color: var(--accent);
    }

    #last-spoken {
      font-size: 0.66rem;
      color: rgba(148, 163, 184, 0.9);
      margin-top: 4px;
    }

    @media (max-width: 768px) {
      body {
        padding: 8px;
      }

      .app-shell {
        border-radius: 18px;
        padding: 10px;
      }

      header {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
      }

      .controls-row {
        padding-top: 0;
      }

      .btn-primary {
        margin-left: 0;
      }

      .main {
        grid-template-columns: minmax(0, 1fr);
      }

      .card {
        padding: 10px;
      }

      .list {
        max-height: 340px;
      }
    }

    @media (max-width: 480px) {
      .title-main {
        font-size: 1rem;
      }

      .title-sub {
        font-size: 0.68rem;
      }

      .status-pill {
        width: 100%;
        justify-content: space-between;
      }
    }
  </style>
</head>
<body>
  <div class="app-shell">
    <header>
      <div class="title">
        <div class="title-main">
          <span>🎓 LBS Campus Navigator</span>
          <span class="badge">Kasaragod • Live</span>
        </div>
        <div class="title-sub">
          Tap any location card to open directions from your current position and hear the route summary.
        </div>
      </div>
      <div class="status-pill">
        <span class="status-dot"></span>
        <span class="status-text">
          Location <strong>ready</strong>
        </span>
        <span class="status-divider"></span>
        <span class="status-chip">Voice • Maps • Geo</span>
      </div>
    </header>

    <section class="controls-row">
      <div class="pill">
        <span class="pill-dot"></span>
        <span><strong>Auto</strong> detect current location when you choose a place.</span>
      </div>
      <button class="btn-primary" id="test-voice">
        <span>🔊 Test voice</span>
        <span>EN-IN</span>
      </button>
    </section>

    <section class="main">
      <section class="card">
        <div class="card-header">
          <div>
            <strong>Campus map</strong>
            <span style="color: var(--muted);">• Tap a card to start navigation</span>
          </div>
        </div>

        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input
            id="search"
            class="search-input"
            type="text"
            placeholder="Search: library, mechanical, hostel, canteen, ATM..."
          />
        </div>

        <div class="list" id="places-list">
        </div>
      </section>

      <section class="card">
        <div class="card-header">
          <div>
            <strong>Live navigation</strong>
            <span style="color: var(--muted);">• Status & spoken instructions</span>
          </div>
        </div>

        <div class="status-banner">
          <div class="banner-header">
            <span class="banner-chip">Secure geolocation</span>
            <span class="mini-pill">Browser permission required</span>
          </div>
          <div class="banner-body">
            <div>
              <div class="badge-inline">
                <span class="dot"></span>
                <span>Uses device GPS / network for your current position.</span>
              </div>
              <div style="margin-top: 4px;">
                Tap any location card and your browser will ask for permission (first time only).
              </div>
            </div>
          </div>
        </div>

        <div style="margin-top: 10px;">
          <div class="section-label">
            <span class="dot"></span>
            <span>Current session</span>
          </div>
          <div id="status">
            Waiting for a destination tap on the left panel.
          </div>
          <div id="last-spoken"></div>
        </div>

        <div class="action-row">
          <div class="chip-ghost">
            <span>🧭</span>
            <span>Route opens in<strong> Google Maps</strong>.</span>
          </div>
          <div class="chip-soft">
            <span>💡 Tip:</span>
            <span>Keep mobile GPS and data turned on.</span>
          </div>
        </div>
      </section>
    </section>
  </div>

  <script>
    const places = [
      {
        categoryLabel: "🏛️ Main Campus & Admin",
        items: [
          {
            name: "LBS College of Engineering (Main Entrance)",
            category: "Main Campus & Admin",
            url: "https://maps.app.goo.gl/ZGm4R6fiM6KgbfH97"
          },
          {
            name: "Academic Departments (General Area)",
            category: "Main Campus & Admin",
            url: "https://maps.app.goo.gl/2PvfbFGAkUFjFBjS6"
          },
          {
            name: "Dept. Of Mechanical Engineering",
            category: "Main Campus & Admin",
            url: "https://maps.app.goo.gl/Yas8hpFy3kNim1xD8"
          },
          {
            name: "Computer Science & IT Department Building",
            category: "Main Campus & Admin",
            url: "https://maps.app.goo.gl/DbwYQ6b984VTGDjm6"
          }
        ]
      },
      {
        categoryLabel: "🔬 Academic Facilities",
        items: [
          {
            name: "Central Library",
            category: "Academic Facilities",
            url: "https://maps.app.goo.gl/fh6Z8TEsomfuoFbJ9"
          },
          {
            name: "Campus Fab Lab",
            category: "Academic Facilities",
            url: "https://maps.app.goo.gl/3rz8e5WXZ3UytSze7"
          },
          {
            name: "Computer Lab",
            category: "Academic Facilities",
            url: "https://maps.app.goo.gl/6pasZGBNrC3opwTg8"
          },
          {
            name: "Reprographic Centre",
            category: "Academic Facilities",
            url: "https://maps.app.goo.gl/FZ72xAAczEwk2mgi7"
          }
        ]
      },
      {
        categoryLabel: "⚽ Sports & Recreation",
        items: [
          {
            name: "Multipurpose Sports Area",
            category: "Sports & Recreation",
            url: "https://maps.app.goo.gl/uyPH83UZo3rjEFEBA"
          },
          {
            name: "LBS College Football Ground",
            category: "Sports & Recreation",
            url: "https://maps.app.goo.gl/vjLN3ZgN2yUoxuSr5"
          }
        ]
      },
      {
        categoryLabel: "🏠 Student Amenities",
        items: [
          {
            name: "Men's Hostel (Verified Block)",
            category: "Student Amenities",
            url: "https://maps.app.goo.gl/fQ1QAUmNk5MDepgTA"
          },
          {
            name: "Shahanas Hostel (Ladies Hostel)",
            category: "Student Amenities",
            url: "https://maps.app.goo.gl/nPwgvr3U3fXSiUj47"
          },
          {
            name: "College Canteen",
            category: "Student Amenities",
            url: "https://maps.app.goo.gl/UN4s7g16zSMiHhYz8"
          },
          {
            name: "College ATM (SBI ATM)",
            category: "Student Amenities",
            url: "https://maps.app.goo.gl/ug6jLStaQDjnVZ239"
          },
          {
            name: "Bus Garage / Transport Area",
            category: "Student Amenities",
            url: "https://maps.app.goo.gl/9WUemftWwmGohsRW8"
          }
        ]
      }
    ];

    const listEl = document.getElementById("places-list");
    const searchInput = document.getElementById("search");
    const statusEl = document.getElementById("status");
    const lastSpokenEl = document.getElementById("last-spoken");
    const testVoiceBtn = document.getElementById("test-voice");

    function buildList(filterText = "") {
      listEl.innerHTML = "";
      const query = filterText.trim().toLowerCase();

      places.forEach(section => {
        const filteredItems = section.items.filter(item => {
          if (!query) return true;
          return (
            item.name.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query)
          );
        });

        if (!filteredItems.length) return;

        const sectionLabel = document.createElement("div");
        sectionLabel.className = "section-label";
        sectionLabel.innerHTML = `<span class="dot"></span><span>${section.categoryLabel}</span>`;
        listEl.appendChild(sectionLabel);

        filteredItems.forEach(item => {
          const card = document.createElement("article");
          card.className = "place-card";
          card.dataset.url = item.url;
          card.dataset.name = item.name;
          card.dataset.category = item.category;

          card.innerHTML = `
            <div class="place-main">
              <div class="place-category">
                <span>${item.category}</span>
                <span class="pill-mini">Tap to navigate</span>
              </div>
              <div class="place-name">
                <span>${item.name}</span>
              </div>
              <div class="place-meta">
                <span class="pill-verified">
                  <span class="dot"></span>
                  <span>Google Maps verified</span>
                </span>
                <span class="pill-link">
                  <span class="icon">↗</span>
                  <span>Open in Google Maps app</span>
                </span>
              </div>
            </div>
            <div class="place-action">
              <div class="chip chip-go">
                <span class="icon">📍</span>
                <span>Route</span>
              </div>
              <div class="secondary-text">
                From your current location
              </div>
            </div>
          `;

          card.addEventListener("click", () => handlePlaceClick(item));
          listEl.appendChild(card);
        });
      });

      if (!listEl.innerHTML) {
        listEl.innerHTML =
          '<div style="padding: 10px; font-size: 0.74rem; color: rgba(148, 163, 184, 0.9);">No places match your search. Try another keyword.</div>';
      }
    }

    buildList();

    searchInput.addEventListener("input", e => {
      buildList(e.target.value);
    });

    function speak(text) {
      if (!("speechSynthesis" in window)) {
        return;
      }

      window.speechSynthesis.cancel();

      const utterance = new SpeechSynthesisUtterance(text);
      const voices = window.speechSynthesis.getVoices();
      const preferred = voices.find(v =>
        v.lang.toLowerCase().startsWith("en-in")
      );
      utterance.voice = preferred || voices[0] || null;
      utterance.rate = 1.0;
      utterance.pitch = 1.0;
      utterance.volume = 1;

      window.speechSynthesis.speak(utterance);
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
    }

    testVoiceBtn.addEventListener("click", () => {
      const text =
        "Voice navigation is ready. Tap any place card to open Google Maps from your current location.";
      speak(text);
      lastSpokenEl.textContent = `Spoken: "${text}"`;
    });

    function handlePlaceClick(place) {
      const name = place.name;
      const url = place.url;

      statusEl.innerHTML =
        'Fetching your current location… Please keep GPS enabled and grant permission when asked.';

      if (!navigator.geolocation) {
        statusEl.innerHTML =
          "Geolocation is not supported by this browser. You can still open the Google Maps link directly.";
        window.open(url, "_blank");
        const fallbackText = `Opening Google Maps for ${name}.`;
        speak(fallbackText);
        lastSpokenEl.textContent = `Spoken: "${fallbackText}"`;
        return;
      }

      navigator.geolocation.getCurrentPosition(
        position => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;

          statusEl.innerHTML = `
            Location acquired.<br />
            From: <strong>${lat.toFixed(5)}, ${lng.toFixed(5)}</strong><br />
            To: <strong>${name}</strong> (Google Maps link opened in a new tab).
          `;

          const directionsUrl = `https://www.google.com/maps/dir/?api=1&origin=${lat},${lng}&destination=${encodeURIComponent(
            name
          )}&destination_place_id=&travelmode=driving`;

          window.open(directionsUrl, "_blank");

          const spoken = `Starting navigation from your current location to ${name}. Your route is now open in Google Maps.`;
          speak(spoken);
          lastSpokenEl.textContent = `Spoken: "${spoken}"`;
        },
        error => {
          let msg;
          switch (error.code) {
            case error.PERMISSION_DENIED:
              msg =
                "Location permission was denied. Opening the Google Maps place link without your current position.";
              break;
            case error.POSITION_UNAVAILABLE:
              msg =
                "Location information is unavailable. Opening the Google Maps place link.";
              break;
            case error.TIMEOUT:
              msg =
                "Location request timed out. Opening the Google Maps place link.";
              break;
            default:
              msg =
                "An unknown error occurred while fetching your location. Opening the Google Maps place link.";
          }

          statusEl.textContent = msg;
          window.open(url, "_blank");
          const spoken = `${msg}`;
          speak(spoken);
          lastSpokenEl.textContent = `Spoken: "${spoken}"`;
        },
        {
          enableHighAccuracy: true,
          timeout: 15000,
          maximumAge: 0
        }
      );
    }
  </script>
</body>
</html>
"""

components.html(
    html_code,
    height=700,     # tweak based on your screen
    scrolling=True,
)
