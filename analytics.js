/**
 * Advanced Event Tracking Suite for Wanderer's Wails (Wayfarer's Woes)
 * Integrates directly with GA4 (Measurement ID: G-48WEYC58S7)
 */

// Safe wrapper to dispatch GA4 events
function trackGAEvent(eventName, params = {}) {
  if (typeof window.gtag === 'function') {
    window.gtag('event', eventName, {
      ...params,
      page_path: window.location.pathname,
      page_title: document.title
    });
    console.log(`[Analytics Event Logged] Name: "${eventName}", Params:`, params);
  } else {
    console.warn(`[Analytics Error] gtag is not loaded. Tried to log "${eventName}" with params:`, params);
  }
}

// Track Scroll Depth
let scrollDepthTracks = { 25: false, 50: false, 75: false, 90: false };
function initScrollTracking() {
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (scrollHeight <= 0) return;
    
    const percent = Math.round((scrollTop / scrollHeight) * 100);
    
    [25, 50, 75, 90].forEach(depth => {
      if (percent >= depth && !scrollDepthTracks[depth]) {
        scrollDepthTracks[depth] = true;
        trackGAEvent('scroll_depth', { depth_percentage: depth });
      }
    });
  }, { passive: true });
}

// Initialize general DOM tracking listeners on load
document.addEventListener('DOMContentLoaded', () => {
  // 1. Navbar Clicks
  const navLinks = document.querySelectorAll('.nav-link, .nav-logo');
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const label = link.textContent.trim() || 'Logo';
      const destination = link.getAttribute('href');
      trackGAEvent('navbar_click', {
        link_label: label,
        destination_url: destination
      });
    });
  });

  // 2. Substack/Subscribe Clicks
  const subscribeLinks = document.querySelectorAll('.nav-link.highlight, .footer-social-link, .subscribe-form button, .subscribe-card button');
  subscribeLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const isSubstack = link.href && link.href.includes('substack.com');
      trackGAEvent('subscribe_click', {
        element_text: link.textContent.trim() || 'Subscribe Button',
        is_substack_redirection: isSubstack,
        url: link.href || 'Form Submission'
      });
    });
  });

  // 3. Map Interactions (USA State Clicks on interactive maps)
  // Check if map paths exist on the page
  const mapContainer = document.getElementById('map');
  if (mapContainer) {
    mapContainer.addEventListener('click', (e) => {
      const path = e.target.closest('path');
      if (path) {
        const stateId = path.getAttribute('id');
        const stateName = path.getAttribute('data-name') || stateId;
        const isVisited = path.classList.contains('visited');
        trackGAEvent('map_state_click', {
          state_id: stateId,
          state_name: stateName,
          state_visited: isVisited
        });
      }
    });
  }

  // 4. Exclude / Clear filters track
  const clearFilterBtns = document.querySelectorAll('.clear-filters-btn');
  clearFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      trackGAEvent('clear_filters_click', { action: 'clear_all' });
    });
  });

  // Start Scroll Depth Tracking
  initScrollTracking();
  
  // Track Page View
  trackGAEvent('page_view_custom', {
    referrer: document.referrer || 'direct'
  });
});

// Search Debounce Tracker
let searchDebounceTimeout;
function trackSearchQuery(query) {
  if (searchDebounceTimeout) clearTimeout(searchDebounceTimeout);
  if (!query) return;
  
  searchDebounceTimeout = setTimeout(() => {
    trackGAEvent('search_usage', { search_term: query });
  }, 1000); // Track search after 1s of inactivity
}
