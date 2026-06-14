/** Live refresh from SeatSidekick API — 60s cooldown via localStorage. */
(function () {
  const cfg = window.__wc2026Config;
  if (!cfg) return;

  const API_BASE =
    "https://dlvtfsmonledyyjaqjcn.supabase.co/rest/v1/match_seat_groups";
  const APIKEY =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsdnRmc21vbmxlZHl5amFxamNuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY0MDk3NDcsImV4cCI6MjA5MTk4NTc0N30.warYGD7rBH_x_qx9i56WfcJ3RKhCALBEarzHSUpkq5k";
  const COOLDOWN_MS = 60_000;
  const LS_KEY = "wc2026_last_refresh";
  const FETCH_LIMIT = 1000;

  function marketAvg(avg, catNum) {
    const range = cfg.catMarketRange[String(catNum)];
    if (!range) return true;
    return avg >= range[0] && avg <= range[1];
  }

  function marketDeal(deal, catNum) {
    return marketAvg(deal.avg, catNum);
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

  function rowToDeal(row) {
    const rowNum = parseInt(row.row, 10);
    return {
      sec: String(row.block),
      row: rowNum,
      seats: formatSeats(row.seat_numbers),
      stand: parseStand(row.area),
      side: parseSide(row.area),
      total: Math.round(row.total_price),
      avg: Math.round(row.avg_price),
      gs: row.group_size,
      front: rowNum < 20,
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
          block,
          row: r,
          first_seat: seats[i],
          last_seat: seats[i + 1],
          avg,
          total: avg * 2,
          parent: row,
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
        block: pair.block,
        row: pair.row,
        area: pair.parent.area,
        group_size: 2,
        first_seat: pair.first_seat,
        last_seat: pair.last_seat,
        seat_numbers: `${pair.first_seat},${pair.last_seat}`,
        min_price: pair.avg,
        max_price: pair.avg,
        avg_price: pair.avg,
        total_price: pair.total,
        _derived: true,
      });
      lookup.add(key);
    }
    merged.sort((a, b) => a.total_price - b.total_price);
    return merged;
  }

  function medianRounded(values) {
    const sorted = [...values].sort((a, b) => a - b);
    const mid = Math.floor(sorted.length / 2);
    if (sorted.length % 2) return Math.round(sorted[mid]);
    return Math.round((sorted[mid - 1] + sorted[mid]) / 2);
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

  function chartBuckets(catNum, g2, g4) {
    const c2 = [0, 0, 0, 0, 0, 0];
    const c4 = [0, 0, 0, 0, 0, 0];
    for (const row of g2) c2[bucketIndex(catNum, Math.round(row.avg_price))]++;
    for (const row of g4) c4[bucketIndex(catNum, Math.round(row.avg_price))]++;
    const peak = Math.max(...c2, ...c4, 0);
    const ymax = peak ? Math.max(5, Math.ceil((peak * 1.15) / 5) * 5) : 5;
    const ystep = Math.max(1, Math.round(ymax / 5));
    return { c2, c4, ymax, ystep };
  }

  function buildInventory(g2Deals, g4Deals) {
    const blocks = {};
    for (const [deals, cntKey, minKey] of [
      [g2Deals, "g2c", "g2m"],
      [g4Deals, "g4c", "g4m"],
    ]) {
      for (const d of deals) {
        if (!blocks[d.sec]) {
          blocks[d.sec] = {
            sec: d.sec,
            stand: d.stand,
            side: d.side,
            g2c: 0,
            g2m: null,
            g4c: 0,
            g4m: null,
          };
        }
        const b = blocks[d.sec];
        b[cntKey]++;
        if (b[minKey] === null || d.avg < b[minKey]) b[minKey] = d.avg;
      }
    }
    return Object.values(blocks);
  }

  function metricsFor(rows, ticketLabel, catNum) {
    rows = rows.filter((r) => marketAvg(Math.round(r.avg_price), catNum));
    if (!rows.length) {
      return {
        listings: "0",
        cheapest_value: "—",
        cheapest_sub: "No listings in market range",
        median_value: "—",
        median_sub: "",
        min_total_value: "—",
        min_total_sub: "",
        ticket_label: ticketLabel,
      };
    }
    const avgs = rows.map((r) => r.avg_price);
    const cheapest = rows.reduce((a, b) => (a.avg_price < b.avg_price ? a : b));
    const minTotal = rows.reduce((a, b) =>
      a.total_price < b.total_price ? a : b
    );
    const n = rows.length;
    return {
      listings: String(n),
      cheapest_value: `$${Math.round(cheapest.avg_price).toLocaleString()}`,
      cheapest_sub: `Section ${cheapest.block} · Row ${cheapest.row}`,
      median_value: `$${medianRounded(avgs).toLocaleString()}`,
      median_sub: `Across ${n} groups`,
      min_total_value: `$${Math.round(minTotal.total_price).toLocaleString()}`,
      min_total_sub: `Section ${minTotal.block}, Row ${minTotal.row}`,
      ticket_label: ticketLabel,
    };
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

  function buildCategory(catNum, g2Raw, g4Raw) {
    const g2Native = g2Raw.filter((r) =>
      marketAvg(Math.round(r.avg_price), catNum)
    );
    const g4Native = g4Raw.filter((r) =>
      marketAvg(Math.round(r.avg_price), catNum)
    );
    const g2Merged = mergeDerivedPairs(g2Native, g4Native);
    const g2Deals = g2Merged
      .map((r) => rowToDeal(r))
      .filter((d) => marketDeal(d, catNum));
    const g4Deals = g4Native
      .map((r) => rowToDeal(r))
      .filter((d) => marketDeal(d, catNum));
    const top3 = topDeals([...g2Deals, ...g4Deals], 3);
    const inv = buildInventory(g2Deals, g4Deals).sort(
      (a, b) => b.g2c + b.g4c - (a.g2c + a.g4c)
    );
    const { c2, c4, ymax, ystep } = chartBuckets(catNum, g2Merged, g4Native);
    const labels = cfg.bucketLabels[String(catNum)] || [];
    return {
      g2_top: [...g2Deals].sort((a, b) => a.avg - b.avg).slice(0, 10),
      g4_top: [...g4Deals].sort((a, b) => a.avg - b.avg).slice(0, 10),
      top3,
      inv,
      chart: { c2, c4, labels, ymax, ystep },
      metrics_g2: metricsFor(g2Merged, "Groups of 2 tickets", catNum),
      metrics_g4: metricsFor(g4Native, "Groups of 4 tickets", catNum),
    };
  }

  function updateMetricsBlock(el, m) {
    const vals = el.querySelectorAll(".metric-value");
    const subs = el.querySelectorAll(".metric-sub");
    vals[0].textContent = m.listings;
    subs[0].textContent = m.ticket_label;
    vals[1].textContent = m.cheapest_value;
    subs[1].textContent = m.cheapest_sub;
    vals[2].textContent = m.median_value;
    subs[2].textContent = m.median_sub;
    vals[3].textContent = m.min_total_value;
    subs[3].textContent = m.min_total_sub;
  }

  function applyCategory(catNum, data) {
    const prefix = `cat${catNum}`;
    const section = document.getElementById(prefix);
    if (!section) return;
    const metricBlocks = section.querySelectorAll(".metrics");
    updateMetricsBlock(metricBlocks[0], data.metrics_g2);
    updateMetricsBlock(metricBlocks[1], data.metrics_g4);

    renderDeals(
      data.top3,
      data.g2_top,
      data.g4_top,
      `${prefix}-top3`,
      `${prefix}-list2`,
      `${prefix}-list4`
    );
    renderInv(data.inv, `${prefix}-inv`);
    const ch = data.chart;
    makeChart(
      `${prefix}-chart`,
      ch.c2,
      ch.c4,
      ch.labels,
      ch.ymax,
      ch.ystep
    );
  }

  function formatNow() {
    const now = new Date();
    const datePart = now.toLocaleDateString("en-US", {
      month: "long",
      day: "numeric",
      year: "numeric",
      timeZone: "America/New_York",
    });
    const timePart = now.toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "2-digit",
      timeZone: "America/New_York",
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
      const results = await Promise.all(
        cfg.queries.map((q) => fetchQuery(q.category, q.gs))
      );

      // Group by cat + gs
      const byCat = {};
      cfg.queries.forEach((q, i) => {
        if (!byCat[q.cat]) byCat[q.cat] = { g2: null, g4: null };
        byCat[q.cat][q.gs === 2 ? "g2" : "g4"] = results[i];
      });

      // Unhide cat sections/tabs for active cats
      const activeCats = new Set(cfg.queries.map((q) => q.cat));
      activeCats.forEach((catNum) => {
        const sec = document.getElementById(`cat${catNum}`);
        const tab = document.getElementById(`cat${catNum}-tab`);
        if (sec) sec.removeAttribute("hidden");
        if (tab) tab.removeAttribute("hidden");
      });

      for (const catNum of Object.keys(byCat).map(Number)) {
        applyCategory(
          catNum,
          buildCategory(catNum, byCat[catNum].g2 || [], byCat[catNum].g4 || [])
        );
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
