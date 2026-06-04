// State Management
const state = {
  gallery: [],         // All DSLR items
  filteredGallery: [], // Items after applying search/location filters
  activeGalleryIndex: -1,
  initialLoadComplete: false,
  pagination: {
    currentPage: 1,
    itemsPerPage: 50
  },
  filters: {
    search: '',
    location: null,    // selected location name or null
    sortOrder: 'desc'  // 'desc' (newest first) or 'asc' (oldest first)
  }
};

// Intersection Observer for stagger reveal animation
let cardObserver;

document.addEventListener('DOMContentLoaded', () => {
  initGallery();
  setupEventListeners();
  initObserver();
});

// Initialize Gallery Data
async function initGallery() {
  try {
    const response = await fetch('gallery.json');
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    
    // Filter to DSLR images only (images/ag-edits)
    state.gallery = data.filter(item => item.filename && item.filename.startsWith('images/ag-edits/'));
    
    // Standardize camera models and lens models on load
    state.gallery.forEach(item => {
      if (item.camera === 'Sony Alpha 7 III') {
        item.camera = 'Sony Alpha 7';
      }
      if (item.lens && item.lens.includes('28-75')) {
        item.lens = 'Tamron 28-75mm f2.8';
      } else if (item.lens && item.lens.includes('70-300')) {
        item.lens = 'Tamron 70-300mm';
      }
    });

    console.log(`Loaded ${state.gallery.length} DSLR images.`);
    
    // Populate dynamic location filter badges
    renderLocationBadges();
    
    // Apply filters, sort, and render grid
    applyFiltersAndSort();
  } catch (error) {
    console.error('Failed to initialize photo gallery:', error);
    hideLoaderFailsafe();
    document.getElementById('galleryGrid').innerHTML = `
      <div class="no-results glass-panel">
        <h3>Error loading gallery</h3>
        <p>Could not load the photo canvas. Please try reloading the page.</p>
      </div>
    `;
  }
}

// Set up DOM interaction event listeners
function setupEventListeners() {
  const searchInput = document.getElementById('gallerySearch');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.filters.search = e.target.value.toLowerCase().trim();
      state.pagination.currentPage = 1; // Reset to page 1 on new search
      applyFiltersAndSort();
    });
  }
}

// Initialize Intersection Observer for card fade-ins
function initObserver() {
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.15
  };
  
  cardObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const card = entry.target;
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
        observer.unobserve(card);
      }
    });
  }, observerOptions);
}

// Render dynamic location filter badges
function renderLocationBadges() {
  const container = document.getElementById('locationBadgesContainer');
  if (!container) return;
  
  // Extract unique locations from DSLR gallery items
  const locationsMap = {};
  state.gallery.forEach(item => {
    if (item.location) {
      locationsMap[item.location] = (locationsMap[item.location] || 0) + 1;
    }
  });
  
  // Sort locations alphabetically
  const uniqueLocations = Object.keys(locationsMap).sort();
  
  let html = `
    <button class="location-badge-btn ${!state.filters.location ? 'active' : ''}" onclick="setLocationFilter(null)">
      All (${state.gallery.length})
    </button>
  `;
  
  uniqueLocations.forEach(loc => {
    const isActive = state.filters.location === loc;
    html += `
      <button class="location-badge-btn ${isActive ? 'active' : ''}" onclick="setLocationFilter('${loc.replace(/'/g, "\\'")}')">
        ${loc} <span class="badge-count">${locationsMap[loc]}</span>
      </button>
    `;
  });
  
  container.innerHTML = html;
}

// Set Location Filter
function setLocationFilter(location) {
  state.filters.location = location;
  state.pagination.currentPage = 1; // Reset to page 1 on new filter
  
  // Update badge UI states
  const badges = document.querySelectorAll('.location-badge-btn');
  badges.forEach(badge => {
    const isAllBtn = badge.textContent.includes('All') && location === null;
    const isMatchedBtn = badge.textContent.includes(location) && location !== null;
    
    if (isAllBtn || isMatchedBtn) {
      badge.classList.add('active');
    } else {
      badge.classList.remove('active');
    }
  });
  
  renderLocationBadges();
  applyFiltersAndSort();
}

// Toggle Sort Order between Ascending and Descending
function toggleSortOrder() {
  state.filters.sortOrder = state.filters.sortOrder === 'desc' ? 'asc' : 'desc';
  state.pagination.currentPage = 1; // Reset to page 1 on sorting change
  
  const sortBtn = document.getElementById('sortToggleBtn');
  const sortLabel = sortBtn.querySelector('span');
  const sortArrow = document.getElementById('sortArrowIcon');
  
  if (state.filters.sortOrder === 'desc') {
    sortLabel.textContent = 'Date (Newest First)';
    sortArrow.style.transform = 'rotate(0deg)';
  } else {
    sortLabel.textContent = 'Date (Oldest First)';
    sortArrow.style.transform = 'rotate(180deg)';
  }
  
  applyFiltersAndSort();
}

// Core filter, sort, and render manager
function applyFiltersAndSort() {
  const { search, location, sortOrder } = state.filters;
  
  // Apply filtering rules
  state.filteredGallery = state.gallery.filter(item => {
    // Search Query check (matches title, description, location, or camera details)
    const matchesSearch = !search || 
      (item.title && item.title.toLowerCase().includes(search)) ||
      (item.description && item.description.toLowerCase().includes(search)) ||
      (item.location && item.location.toLowerCase().includes(search)) ||
      (item.camera && item.camera.toLowerCase().includes(search)) ||
      (item.lens && item.lens.toLowerCase().includes(search));
      
    // Location badge check
    const matchesLocation = !location || item.location === location;
    
    return matchesSearch && matchesLocation;
  });

  // Apply sorting rules (default descending date)
  state.filteredGallery.sort((a, b) => {
    const dateA = new Date(a.date);
    const dateB = new Date(b.date);
    return sortOrder === 'desc' ? dateB - dateA : dateA - dateB;
  });

  renderGrid();
}

// Render dynamic photo cards into the grid
function renderGrid() {
  const grid = document.getElementById('galleryGrid');
  const noResults = document.getElementById('noResults');
  const pagControls = document.getElementById('paginationControls');
  
  grid.innerHTML = '';
  
  if (state.filteredGallery.length === 0) {
    noResults.classList.remove('hidden');
    if (pagControls) pagControls.innerHTML = '';
    hideLoaderFailsafe();
    return;
  }
  
  noResults.classList.add('hidden');
  
  // Apply pagination slicing
  const { currentPage, itemsPerPage } = state.pagination;
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const pageItems = state.filteredGallery.slice(startIndex, endIndex);
  
  // Pre-load images in memory to trigger loader transition if not completed
  if (!state.initialLoadComplete) {
    preloadFirstSet(pageItems);
  }

  pageItems.forEach((item, index) => {
    // The absolute index of this item in the full filtered array
    const absoluteIndex = startIndex + index;
    
    const card = document.createElement('div');
    card.className = 'gallery-card';
    card.style.opacity = '0';
    card.style.transform = 'translateY(25px)';
    card.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    
    // Add custom delay for grid staggering
    const delay = (index % 3) * 0.06;
    card.style.transitionDelay = `${delay}s`;
    
    // Compute thumbnail image path
    const thumbnailFilename = item.filename.replace('images/ag-edits/', 'images/ag-edits-thumbnails/');
    
    card.innerHTML = `
      <div class="gallery-card-img-wrapper" onclick="openGalleryModal(${absoluteIndex})">
        <img class="gallery-card-img" src="${thumbnailFilename}" alt="${item.title}" loading="lazy">
      </div>
      <div class="gallery-card-info">
        <div class="gallery-card-meta">
          <span class="gallery-card-location" onclick="setLocationFilter('${item.location.replace(/'/g, "\\'")}')">${item.location}</span>
          <span class="gallery-card-date">${item.date}</span>
        </div>
        <h3 class="gallery-card-title" onclick="openGalleryModal(${absoluteIndex})">${item.title}</h3>
      </div>
    `;
    
    grid.appendChild(card);
    
    // Observe card for entrance animations
    cardObserver.observe(card);
  });

  // Render pagination buttons
  renderPagination();
}

// Pre-load first set of thumbnail images to guarantee smooth fade-in
function preloadFirstSet(items) {
  // Grab the first 12 images (above the fold size) to check for load events
  const subset = items.slice(0, 12);
  if (subset.length === 0) {
    hideLoaderFailsafe();
    return;
  }

  let loadedCount = 0;
  const totalToLoad = subset.length;

  const checkFinish = () => {
    loadedCount++;
    if (loadedCount >= totalToLoad) {
      hideLoaderFailsafe();
    }
  };

  subset.forEach(item => {
    const img = new Image();
    img.onload = checkFinish;
    img.onerror = checkFinish;
    img.src = item.filename.replace('images/ag-edits/', 'images/ag-edits-thumbnails/');
  });

  // Failsafe backup timeout of 2 seconds
  setTimeout(hideLoaderFailsafe, 2000);
}

function hideLoaderFailsafe() {
  if (state.initialLoadComplete) return;
  state.initialLoadComplete = true;
  
  const loader = document.getElementById('pageLoader');
  const content = document.getElementById('galleryPageContent');
  
  if (loader) {
    loader.classList.add('fade-out');
    setTimeout(() => {
      loader.style.display = 'none';
    }, 500);
  }
  
  if (content) {
    content.classList.add('loaded');
  }
}

// Render Pagination Buttons
function renderPagination() {
  const container = document.getElementById('paginationControls');
  if (!container) return;
  
  const totalPages = Math.ceil(state.filteredGallery.length / state.pagination.itemsPerPage);
  
  // Hide pagination bar if there's only 1 page
  if (totalPages <= 1) {
    container.innerHTML = '';
    return;
  }
  
  const { currentPage } = state.pagination;
  let html = '';
  
  // Prev Button
  const prevDisabled = currentPage === 1 ? 'disabled' : '';
  html += `
    <button class="pag-btn prev-btn" ${prevDisabled} onclick="goToPage(${currentPage - 1})">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
      <span>Prev</span>
    </button>
  `;
  
  // Numeric Buttons (with ellipsis for large page lists if necessary)
  for (let i = 1; i <= totalPages; i++) {
    const isActive = i === currentPage ? 'active' : '';
    // Show first page, last page, and page numbers close to current page
    if (totalPages <= 7 || i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {
      html += `
        <button class="pag-number-btn ${isActive}" onclick="goToPage(${i})">${i}</button>
      `;
    } else if (i === currentPage - 3 || i === currentPage + 3) {
      html += `<span class="pag-ellipsis">&hellip;</span>`;
    }
  }
  
  // Next Button
  const nextDisabled = currentPage === totalPages ? 'disabled' : '';
  html += `
    <button class="pag-btn next-btn" ${nextDisabled} onclick="goToPage(${currentPage + 1})">
      <span>Next</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </button>
  `;
  
  container.innerHTML = html;
}

// Page Navigation Action Handler
function goToPage(pageNum) {
  state.pagination.currentPage = pageNum;
  
  // Scroll gallery grid area back into view smoothly
  const controlsSection = document.querySelector('.gallery-controls-section');
  if (controlsSection) {
    const topOffset = controlsSection.getBoundingClientRect().bottom + window.scrollY - 80;
    window.scrollTo({ top: topOffset, behavior: 'smooth' });
  }
  
  renderGrid();
}

// Clear all filter search values and badge triggers
function clearAllFilters() {
  state.filters.search = '';
  state.filters.location = null;
  state.filters.sortOrder = 'desc';
  state.pagination.currentPage = 1;
  
  const searchInput = document.getElementById('gallerySearch');
  if (searchInput) searchInput.value = '';
  
  const sortBtn = document.getElementById('sortToggleBtn');
  const sortLabel = sortBtn.querySelector('span');
  const sortArrow = document.getElementById('sortArrowIcon');
  sortLabel.textContent = 'Date (Newest First)';
  sortArrow.style.transform = 'rotate(0deg)';
  
  renderLocationBadges();
  applyFiltersAndSort();
}

// Lightbox Modal Logic
function openGalleryModal(index) {
  try {
    state.activeGalleryIndex = index;
    // Lightbox navigates through the ENTIRE filtered subset list
    const item = state.filteredGallery[index];
    if (!item) return;
    
    const modal = document.getElementById('galleryModal');
    const img = document.getElementById('lightboxImage');
    const title = document.getElementById('lightboxTitle');
    const location = document.getElementById('lightboxLocation');
    const description = document.getElementById('lightboxDescription');
    
    if (!modal || !img) return;
    
    title.textContent = item.title;
    location.textContent = item.location;
    description.textContent = item.description;
    
    modal.showModal();
    modal.classList.add('open');
    
    document.getElementById('exifCamera').textContent = 'Loading...';
    document.getElementById('exifLens').textContent = 'Loading...';
    document.getElementById('exifAperture').textContent = 'Loading...';
    document.getElementById('exifShutter').textContent = 'Loading...';
    document.getElementById('exifIso').textContent = 'Loading...';
    document.getElementById('exifFocal').textContent = 'Loading...';
    document.getElementById('exifDate').textContent = 'Loading...';
    
    img.onload = function() {
      try {
        if (typeof EXIF !== 'undefined' && typeof EXIF.getData === 'function') {
          EXIF.getData(img, function() {
            try {
              let camera = EXIF.getTag(this, "Model");
              let lens = EXIF.getTag(this, "LensModel");
              const aperture = EXIF.getTag(this, "FNumber");
              const shutter = EXIF.getTag(this, "ExposureTime");
              const iso = EXIF.getTag(this, "ISOSpeedRatings");
              const focal = EXIF.getTag(this, "FocalLength");
              const date = EXIF.getTag(this, "DateTimeOriginal");
              
              if (camera && typeof camera === 'string') {
                camera = camera.replace(/Alpha 7 III|Alpha 7III|a7iii|a7 III/gi, 'Alpha 7');
              }
              
              if (lens && typeof lens === 'string') {
                lens = lens.trim();
                if (lens.includes("28-75")) {
                  lens = "Tamron 28-75mm f2.8";
                } else if (lens.includes("70-300")) {
                  lens = "Tamron 70-300mm";
                } else {
                  lens = null;
                }
              }
              
              if (camera || lens || aperture || shutter || iso || focal || date) {
                document.getElementById('exifCamera').textContent = camera || item.camera || '-';
                document.getElementById('exifLens').textContent = lens || item.lens || '-';
                document.getElementById('exifAperture').textContent = formatAperture(aperture) || item.aperture || '-';
                document.getElementById('exifShutter').textContent = formatShutterSpeed(shutter) || item.shutterSpeed || '-';
                document.getElementById('exifIso').textContent = formatISO(iso) || item.iso || '-';
                document.getElementById('exifFocal').textContent = formatFocalLength(focal) || item.focalLength || '-';
                document.getElementById('exifDate').textContent = formatExifDate(date) || item.date || '-';
              } else {
                loadFallbackExif(item);
              }
            } catch (err) {
              loadFallbackExif(item);
            }
          });
        } else {
          loadFallbackExif(item);
        }
      } catch (err) {
        loadFallbackExif(item);
      }
    };
    
    img.onerror = function() {
      loadFallbackExif(item);
    };
    
    img.src = item.filename;
    window.addEventListener('keydown', handleGalleryKeyDown);
  } catch (err) {
    console.error('Error opening lightbox:', err);
  }
}

function loadFallbackExif(item) {
  document.getElementById('exifCamera').textContent = item.camera || 'Sony Alpha 7';
  document.getElementById('exifLens').textContent = item.lens || '-';
  document.getElementById('exifAperture').textContent = item.aperture || '-';
  document.getElementById('exifShutter').textContent = item.shutterSpeed || '-';
  document.getElementById('exifIso').textContent = item.iso || '-';
  document.getElementById('exifFocal').textContent = item.focalLength || '-';
  document.getElementById('exifDate').textContent = item.date || '-';
}

function closeGalleryModal() {
  const modal = document.getElementById('galleryModal');
  if (modal) {
    modal.close();
    modal.classList.remove('open');
  }
  window.removeEventListener('keydown', handleGalleryKeyDown);
}

function navigateGallery(direction) {
  if (!state.filteredGallery.length) return;
  const newIndex = (state.activeGalleryIndex + direction + state.filteredGallery.length) % state.filteredGallery.length;
  openGalleryModal(newIndex);
}

function handleGalleryKeyDown(event) {
  if (event.key === 'ArrowLeft') {
    navigateGallery(-1);
  } else if (event.key === 'ArrowRight') {
    navigateGallery(1);
  } else if (event.key === 'Escape') {
    closeGalleryModal();
  }
}

function handleBackdropClick(event) {
  const modal = document.getElementById('galleryModal');
  if (event.target === modal) {
    closeGalleryModal();
  }
}

// Metadata Formatter Helpers
function formatShutterSpeed(exposureTime) {
  if (!exposureTime) return null;
  if (typeof exposureTime === 'number') {
    if (exposureTime >= 1) {
      return `${Math.round(exposureTime * 10) / 10}s`;
    }
    const denominator = Math.round(1 / exposureTime);
    return `1/${denominator}s`;
  }
  if (exposureTime.numerator && exposureTime.denominator) {
    return `${exposureTime.numerator}/${exposureTime.denominator}s`;
  }
  return exposureTime.toString();
}

function formatAperture(fNumber) {
  if (!fNumber) return null;
  if (typeof fNumber === 'number') {
    return `f/${fNumber.toFixed(fNumber % 1 === 0 ? 1 : 2)}`;
  }
  if (fNumber.numerator && fNumber.denominator) {
    const val = fNumber.numerator / fNumber.denominator;
    return `f/${val.toFixed(val % 1 === 0 ? 1 : 2)}`;
  }
  return `f/${fNumber}`;
}

function formatFocalLength(focal) {
  if (!focal) return null;
  if (typeof focal === 'number') {
    return `${Math.round(focal)}mm`;
  }
  if (focal.numerator && focal.denominator) {
    return `${Math.round(focal.numerator / focal.denominator)}mm`;
  }
  return `${focal}mm`;
}

function formatISO(iso) {
  if (!iso) return null;
  if (Array.isArray(iso)) {
    return iso[0].toString();
  }
  return iso.toString();
}

function formatExifDate(dateStr) {
  if (!dateStr) return null;
  const parts = dateStr.split(' ');
  if (parts.length > 0) {
    const dateParts = parts[0].split(':');
    if (dateParts.length === 3) {
      const year = dateParts[0];
      const monthIndex = parseInt(dateParts[1], 10) - 1;
      const day = parseInt(dateParts[2], 10);
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      if (monthIndex >= 0 && monthIndex < 12) {
        return `${months[monthIndex]} ${day}, ${year}`;
      }
    }
  }
  return dateStr;
}
