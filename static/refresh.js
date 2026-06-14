/** Live refresh from SeatSidekick API — 60s cooldown via localStorage. */
(function () {
  const cfg = window.__wc2026Config;
  if (!cfg) return;

  const API_BASE =
    "https://dlvtfsmonledyyjaqjcn.supabase.co/rest/v1/match_seat_groups";
  const APIKEY =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsdnRmc21vbmxlZHl5amFxamNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY0MDk3NDcsImV4cCI6MjA5MTk4NTc0N30.warYGD7rBH_x_qx9i56WfcJ3RKhCALBEarzHSUpkq5k";
  const COOLDOWN_MS = 60_000;
  const LS_KEY = "wc2026_last_refresh_" + cfg.performanceId;
  const FETCH_LIMIT = 1000;

  function marketAvg(avg, catNum) {
    const range = cfg.catMarketRange[String(catNum)];
    if (!range) return true;
    return avg >= range[0] && avg <= range[1];
  }

  function buildUrl(category, groupSize) {
    const params = new URLSearchParams({
      select: "*",
      performance_id: `eq.${cfg.performanceId}`,
      dominant_bucket: "eq.Standard",
      dominant_category: `eq.${category}`,
      order: "total_price.asc",
      limit: String(FETCH_LIMIT),
      offset: "0",
      group_size: `eq.${groupSize}`,
    });
    return `${API_BASE}?${params}`;
  }

  async function fetchQuery(category, groupSize) {
    const res = await fetch(buildUrl(category, groupSize), {
      headers: {
        apikey: APIKEY,
        "accept-profile": "api",
        origin: "https://seatsidekick.com",
      },
    });
    if (!res.ok) throw new Error(`API ${res.status}`);
    return res.json();
  }

  function parseSide(area) {
    if (area.includes("Right")) return "Right";
    if (area.includes("Left")) return "Left";
    if (area.includes("Opposite")) return "Opposite";
    return "Center";
  }

  function parseStand(area) {
    return area.includes("Opposite") ? "Opposite" : "Main";
  }

  function formatSeats(seatNumbers) {
    const seats = seatNumbers.split(",").map((s) => s.trim());
    if (seats.length <= 2) return seats.join("–");
    return `${seats[0]}–${seats[seats.length - 1]}`;
  }

  function rowToDeal(row, catNum) {
    const rowNum = parseInt(row.row, 10);
    return {
      sec: String(row.block),
      row: isNaN(rowNum) ? String(row.row) : rowNum,
      seats: formatSeats(row.seat_numbers),
      stand: parseStand(row.area),
      side: parseSide(row.area),
      total: Math.round(row.total_price),
      avg: Math.round(row.avg_price),
      gs: row.group_size,
      cat: catNum,
      front: !isNaN(rowNum) && rowNum < 10,
      mixed: row.min_price !== row.max_price,
      derived: Boolean(row._derived),
    };
  }

  function derivePairs(g4Rows) {
    const pairs = [];
    for (const row of g4Rows) {
      const seats = row.seat_numbers.split(",").map((s) => parseInt(s.trim(), 10));
      if (seats.length < 2) continue;
      const avg = Math.round(row.avg_price);
      const block = String(row.block);
      const r = String(row.row);
      for (let i = 0; i < seats.length - 1; i++) {
        pairs.push({
          block, row: r,
          first_seat: seats[i], last_seat: seats[i + 1],
          avg, total: avg * 2, parent: row,
        });
      }
    }
    return pairs;
  }

  function mergeDerivedPairs(g2, g4) {
    if (!g2.length) return g2;
    const lookup = new Set(
      g2.map((r) => `${r.block}|${r.row}|${r.first_seat}|${r.last_seat}`)
    );
    const minG2Avg = Math.min(...g2.map((r) => Math.round(r.avg_price)));
    const merged = [...g2];
    for (const pair of derivePairs(g4)) {
      const key = `${pair.block}|${pair.row}|${pair.first_seat}|${pair.last_seat}`;
      if (lookup.has(key) || pair.avg >= minG2Avg) continue;
      merged.push({
        block: pair.block, row: pair.row,
        area: pair.parent.area, group_size: 2,
        first_seat: pair.first_seat, last_seat: pair.last_seat,
        seat_numbers: `${pair.first_seat},${pair.last_seat}`,
        min_price: pair.avg, max_price: pair.avg,
        avg_price: pair.avg, total_price: pair.total,
        _derived: true,
      });
      lookup.add(key);
    }
    merged.sort((a, b) => a.total_price - b.total_price);
    return merged;
  }

  function bucketIndex(catNum, avg) {
    const bounds = cfg.bucketRanges[String(catNum)];
    if (!bounds) return 0;
    if (avg < bounds[0]) return 0;
    for (let i = 1; i < bounds.length; i++) {
      if (avg < bounds[i]) return i;
    }
    return bounds.length;
  }

  function chartBucketsSingle(catNum, rows) {
    const c = [0, 0, 0, 0, 0, 0];
    for (const row of rows) c[bucketIndex(catNum, Math.round(row.avg_price))]++;
    const peak = Math.max(...c, 0);
    const ymax = peak ? Math.max(5, Math.ceil((peak * 1.15) / 5) * 5) : 5;
    const ystep = Math.max(1, Math.round(ymax / 5));
    return { c, ymax, ystep };
  }

  function topDeals(deals, n) {
    const seen = new Set();
    const picked = [];
    for (const d of [...deals].sort((a, b) => a.avg - b.avg)) {
      const key = `${d.sec}|${d.row}|${d.gs}|${d.derived}`;
      if (seen.has(key)) continue;
      seen.add(key);
      picked.push(d);
      if (picked.length >= n) break;
    }
    return picked;
  }

  function buildCatGs(catNum, gs, rawRows, g4Raw) {
    const filtered = rawRows.filter((r) => marketAvg(Math.round(r.avg_price), catNum));
    let rows = filtered;
    if (gs === 2) {
      const g4Filtered = (g4Raw || []).filter((r) => marketAvg(Math.round(r.avg_price), catNum));
      rows = mergeDerivedPairs(filtered, g4Filtered);
    }
    const deals = rows
      .map((r) => rowToDeal(r, catNum))
      .filter((d) => marketAvg(d.avg, catNum))
      .sort((a, b) => a.avg - b.avg)
      .slice(0, 10);
    const chart = chartBucketsSingle(catNum, rows);
    return { deals, chart };
  }

  function formatNow() {
    const now = new Date();
    const datePart = now.toLocaleDateString("en-US", {
      month: "long", day: "numeric", year: "numeric",
      timeZone: "America/New_York",
    });
    const timePart = now.toLocaleTimeString("en-US", {
      hour: "numeric", minute: "2-digit", timeZone: "America/New_York",
    });
    return `${datePart} at ${timePart} ET`;
  }

  function cooldownRemaining() {
    const last = parseInt(localStorage.getItem(LS_KEY) || "0", 10);
    return Math.max(0, COOLDOWN_MS - (Date.now() - last));
  }

  let cooldownTimer = null;

  function setButtonState(btn, label, disabled, loading) {
    const lbl = document.getElementById("refresh-btn-label");
    if (lbl) lbl.textContent = label;
    btn.disabled = disabled;
    btn.classList.toggle("loading", loading);
    btn.setAttribute("aria-busy", loading ? "true" : "false");
  }

  function scheduleCooldownUI(btn) {
    clearInterval(cooldownTimer);
    const tick = () => {
      const rem = cooldownRemaining();
      if (rem <= 0) {
        clearInterval(cooldownTimer);
        setButtonState(btn, "Refresh now", false, false);
        return;
      }
      const secs = Math.ceil(rem / 1000);
      setButtonState(btn, `Refresh in ${secs}s`, true, false);
    };
    tick();
    cooldownTimer = setInterval(tick, 500);
  }

  async function refreshNow() {
    const btn = document.getElementById("refresh-btn");
    if (!btn || btn.disabled) return;
    if (cooldownRemaining() > 0) return;

    setButtonState(btn, "Refreshing…", true, true);
    try {
      const settled = await Promise.allSettled(
        cfg.queries.map((q) => fetchQuery(q.category, q.gs))
      );
      const results = settled.map((r) => (r.status === "fulfilled" ? r.value : []));

      // Group raw rows by cat and gs
      const byKey = {};
      cfg.queries.forEach((q, i) => {
        const k = `${q.cat}|${q.gs}`;
        byKey[k] = results[i] || [];
      });

      // Get unique cat nums from queries
      const catNums = [...new Set(cfg.queries.map((q) => q.cat))].sort((a, b) => a - b);
      const gsList = [1, 2, 3, 4];

      // Build __wc2026Data structure
      const newData = { top3: {}, cats: {} };
      for (const catNum of catNums) {
        newData.cats[catNum] = {};
        const g4Raw = byKey[`${catNum}|4`] || [];
        for (const gs of gsList) {
          const raw = byKey[`${catNum}|${gs}`] || [];
          newData.cats[catNum][gs] = buildCatGs(catNum, gs, raw, g4Raw);
        }
      }
      for (const gs of gsList) {
        const allDeals = [];
        for (const catNum of catNums) {
          allDeals.push(...(newData.cats[catNum][gs].deals || []));
        }
        newData.top3[gs] = topDeals(allDeals, 3);
      }

      window.__wc2026Data = newData;

      // Re-init tab visibility and re-render current tab
      for (const gs of gsList) {
        const tab = document.getElementById("gs-tab-" + gs);
        if (!tab) continue;
        const hasData = catNums.some((catNum) => {
          const gsd = newData.cats[catNum][gs];
          return gsd && gsd.deals && gsd.deals.length > 0;
        });
        tab.hidden = !hasData;
      }

      if (typeof switchGs === "function") {
        switchGs(window.activeGs || 2, document.getElementById("gs-tab-" + (window.activeGs || 2)));
      }

      const lu = document.getElementById("last-updated");
      if (lu) {
        lu.innerHTML = `Last updated: <strong>${formatNow()}</strong> <span class="live-badge">live</span>`;
      }

      localStorage.setItem(LS_KEY, String(Date.now()));
      setButtonState(btn, "Refreshed", true, false);
      setTimeout(() => scheduleCooldownUI(btn), 1200);
    } catch (err) {
      console.error("Refresh failed:", err);
      setButtonState(btn, "Refresh failed — retry", false, false);
    }
  }

  function init() {
    const ctx = document.querySelector('meta[name="snapshot-context"]')?.content;
    const btn = document.getElementById("refresh-btn");
    if (!btn) return;

    btn.addEventListener("click", () => {
      if (ctx === "archive") {
        sessionStorage.setItem("wc2026_auto_refresh", "1");
        window.location.href = "../index.html";
        return;
      }
      refreshNow();
    });
    scheduleCooldownUI(btn);

    if (ctx !== "archive" && sessionStorage.getItem("wc2026_auto_refresh")) {
      sessionStorage.removeItem("wc2026_auto_refresh");
      refreshNow();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
