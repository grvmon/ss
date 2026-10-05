/* ==========================================================================
   SELF STORAGE INDIA — SECTION 1: HERO SECTION REDESIGN INTERACTIVE LOGIC
   ========================================================================== */

// 1. Navbar Scroll Transition & Mobile Menu
function updateNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        if (window.scrollY > 20) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
}

window.addEventListener('scroll', updateNavbarScroll, { passive: true });
document.addEventListener('DOMContentLoaded', updateNavbarScroll);
updateNavbarScroll();

function toggleMobileMenu() {
    const navLinks = document.getElementById('navLinks');
    const overlay = document.getElementById('mobileNavOverlay');
    if (!navLinks) return;
    
    const isOpen = navLinks.classList.contains('mobile-open');
    if (isOpen) {
        closeMobileMenu();
    } else {
        navLinks.classList.add('mobile-open');
        if (overlay) overlay.classList.add('active');
        document.body.classList.add('no-scroll');
        document.body.classList.add('mobile-menu-open');
    }
}

function closeMobileMenu() {
    const navLinks = document.getElementById('navLinks');
    const overlay = document.getElementById('mobileNavOverlay');
    if (navLinks) navLinks.classList.remove('mobile-open');
    if (overlay) overlay.classList.remove('active');
    document.body.classList.remove('no-scroll');
    document.body.classList.remove('mobile-menu-open');
}

// 2. Quote & Policy Modal Toggle Functions
function openQuoteModal(pref) {
    if (window.openModal) {
        window.openModal(pref);
    } else {
        const modal = document.getElementById('quote-modal');
        if (modal) {
            if (pref) {
                const target = document.getElementById('storage-size');
                if (target) target.value = pref;
            }
            modal.style.display = 'flex';
            modal.classList.add('lf-modal-open');
            modal.classList.add('open');
            document.body.classList.add('quote-modal-open');
        }
    }
}

function closeQuoteModal(event) {
    if (window.closeModal) {
        window.closeModal();
    } else {
        const modal = document.getElementById('quote-modal');
        if (!event || event.target === modal) {
            if (modal) {
                modal.classList.remove('lf-modal-open');
                modal.classList.remove('open');
                modal.style.display = 'none';
            }
            document.body.classList.remove('quote-modal-open');
        }
    }
}

function openTermsModal() {
    const modal = document.getElementById('terms-modal');
    if (modal) modal.classList.add('open');
}

function closeTermsModal(event) {
    const modal = document.getElementById('terms-modal');
    if (!event || event.target === modal) {
        if (modal) modal.classList.remove('open');
    }
}

function openPrivacyModal() {
    const modal = document.getElementById('privacy-modal');
    if (modal) modal.classList.add('open');
}

function closePrivacyModal(event) {
    const modal = document.getElementById('privacy-modal');
    if (!event || event.target === modal) {
        if (modal) modal.classList.remove('open');
    }
}

// 3. Video Modal Toggle Functions
function openVideoModal() {
    const modal = document.getElementById('video-modal');
    modal.classList.add('open');
}

function closeVideoModal(event) {
    const modal = document.getElementById('video-modal');
    if (!event || event.target === modal) {
        modal.classList.remove('open');
    }
}

// 4. Conversion Form Submission Logic (Zoho CRM Web-to-Lead Integration)
const ZOHO_WEB_TO_LEAD = {
    action: 'https://crm.zoho.in/crm/WebToLeadForm',
    xnQsjsdp: 'f16e947a58c920d3d9bbb4b80e92c047ca04ed4d68bb240204297c44c42d8001',
    xmIwtLD: 'e9726bf6b19e499bf582aa195c8e5d128958792568633ff8fe046537f9cb109d26d208f333e4ee6aef5c1bebc25b1097',
    actionType: 'TGVhZHM=',
    
};

function getThankYouUrl() {
    var isGh = window.location.pathname.startsWith('/ss');
    return window.location.origin + (isGh ? '/ss/thank-you' : '/thank-you');
}

async function handleFormSubmit(event) {
    if (event) event.preventDefault();

    var form = event ? event.target : document.getElementById('quoteModalForm');
    var nameInput = document.getElementById('user-name');
    var phoneInput = document.getElementById('user-phone');
    var emailInput = document.getElementById('user-email');
    var sizeInput = document.getElementById('storage-size');
    var submitBtn = document.getElementById('quoteSubmitBtn') || (form ? form.querySelector('button[type="submit"]') : null);

    var nameVal = nameInput ? nameInput.value.trim() : '';
    var phoneVal = phoneInput ? phoneInput.value.trim() : '';
    var emailVal = emailInput ? emailInput.value.trim() : '';
    var sizeVal = sizeInput ? sizeInput.value : '';
    var countrySelect = document.getElementById('country-code');
    var countryCode = countrySelect ? countrySelect.value : '+91';

    if (!nameVal) {
        alert('Please enter your full name.');
        if (nameInput) nameInput.focus();
        return;
    }

    var rawDigits = phoneVal.replace(/\D/g, '');
    if (!phoneVal || rawDigits.length < 8) {
        alert('Please enter a valid mobile number.');
        if (phoneInput) phoneInput.focus();
        return;
    }

    if (!emailVal || emailVal.indexOf('@') === -1 || emailVal.indexOf('.') === -1) {
        alert('Please enter a valid email address.');
        if (emailInput) emailInput.focus();
        return;
    }

    var formattedPhone = countryCode + ' ' + rawDigits;

    var originalBtnText = submitBtn ? submitBtn.innerText : 'Request Callback';
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Connecting with Advisor...';
    }

    var returnUrl = getThankYouUrl();
    var urlParams = new URLSearchParams(window.location.search);
    var utmSource   = urlParams.get('utm_source') || (window.sessionStorage ? window.sessionStorage.getItem('lf_utm_source') : '') || '';
    var utmMedium   = urlParams.get('utm_medium') || (window.sessionStorage ? window.sessionStorage.getItem('lf_utm_medium') : '') || '';
    var utmCampaign = urlParams.get('utm_campaign') || (window.sessionStorage ? window.sessionStorage.getItem('lf_utm_campaign') : '') || '';
    var utmTerm     = urlParams.get('utm_term') || (window.sessionStorage ? window.sessionStorage.getItem('lf_utm_term') : '') || '';
    var utmContent  = urlParams.get('utm_content') || (window.sessionStorage ? window.sessionStorage.getItem('lf_utm_content') : '') || '';
    var gclidVal    = urlParams.get('gclid') || (window.sessionStorage ? window.sessionStorage.getItem('lf_gclid') : '') || '';
    var fclidVal    = urlParams.get('fclid') || (window.sessionStorage ? window.sessionStorage.getItem('lf_fclid') : '') || '';

    var descParts = [
        'Selected Space/Location: ' + sizeVal,
        'Landing Page: ' + window.location.pathname,
        'Referrer: ' + (document.referrer || 'Direct')
    ];
    if (utmSource)   descParts.push('UTM Source: ' + utmSource);
    if (utmMedium)   descParts.push('UTM Medium: ' + utmMedium);
    if (utmCampaign) descParts.push('UTM Campaign: ' + utmCampaign);
    if (utmTerm)     descParts.push('UTM Term: ' + utmTerm);
    if (utmContent)  descParts.push('UTM Content: ' + utmContent);
    if (gclidVal)    descParts.push('GCLID: ' + gclidVal);
    if (fclidVal)    descParts.push('FCLID: ' + fclidVal);

    var formData = new FormData();
    formData.append('xnQsjsdp', ZOHO_WEB_TO_LEAD.xnQsjsdp);
    formData.append('xmIwtLD', ZOHO_WEB_TO_LEAD.xmIwtLD);
    formData.append('actionType', ZOHO_WEB_TO_LEAD.actionType);
    formData.append('returnURL', returnUrl);
    
    formData.append('aG9uZXlwb3Q', '');
    formData.append('zc_gad', gclidVal || '');
    formData.append('ldeskuid', '');
    formData.append('LDTuvid', (window.$zoho && window.$zoho.salesiq && window.$zoho.salesiq.visitor) ? window.$zoho.salesiq.visitor.uniqueid() : '');
    formData.append('Last Name', nameVal);
    formData.append('Phone', formattedPhone);
    formData.append('Email', emailVal);
    formData.append('Description', descParts.join(' | '));

    if (utmSource)   formData.append('utm_source', utmSource);
    if (utmMedium)   formData.append('utm_medium', utmMedium);
    if (utmCampaign) formData.append('utm_campaign', utmCampaign);
    if (utmTerm)     formData.append('utm_term', utmTerm);
    if (utmContent)  formData.append('utm_content', utmContent);
    if (gclidVal)    formData.append('gclid', gclidVal);
    if (fclidVal)    formData.append('fclid', fclidVal);

    try {
        await fetch(ZOHO_WEB_TO_LEAD.action, {
            method: 'POST',
            body: formData,
            cache: 'no-cache'
        });

        // Also fire custom tracking event
        window.dispatchEvent(new CustomEvent('quote_lead_submitted', {
            detail: { 
                name: nameVal, 
                phone: phoneVal, 
                email: emailVal, 
                size: sizeVal,
                utm_source: utmSource,
                utm_medium: utmMedium,
                utm_campaign: utmCampaign,
                utm_term: utmTerm,
                utm_content: utmContent,
                gclid: gclidVal
            }
        }));

        closeQuoteModal();
        showToastNotification();

        setTimeout(function() {
            window.location.href = returnUrl;
        }, 500);
    } catch (err) {
        console.warn('Direct fetch to Zoho CRM had an issue, falling back to standard form submission...', err);
        if (form && typeof form.submit === 'function') {
            var retInput = document.getElementById('zoho_return_url');
            if (retInput) retInput.value = returnUrl;
            form.submit();
        } else {
            closeQuoteModal();
            window.location.href = returnUrl;
        }
    }
}

// 5. Connect Ananya Storage Advisor Widget to Zoho CRM
window.sendAdvisorData = async function(payload) {
    if (!payload) return;
    var returnUrl = getThankYouUrl();
    var formData = new FormData();
    formData.append('xnQsjsdp', ZOHO_WEB_TO_LEAD.xnQsjsdp);
    formData.append('xmIwtLD', ZOHO_WEB_TO_LEAD.xmIwtLD);
    formData.append('actionType', ZOHO_WEB_TO_LEAD.actionType);
    formData.append('returnURL', returnUrl);
    
    formData.append('aG9uZXlwb3Q', '');
    formData.append('zc_gad', payload.gclid || '');
    formData.append('ldeskuid', '');
    formData.append('LDTuvid', (window.$zoho && window.$zoho.salesiq && window.$zoho.salesiq.visitor) ? window.$zoho.salesiq.visitor.uniqueid() : '');
    formData.append('Last Name', payload.name || 'Website Visitor');
    formData.append('Phone', payload.phone || '');
    formData.append('Email', payload.email || '');
    formData.append('Description', 'Source: Ananya Advisor Widget | ' + (payload.page_title || '') + ' | ' + (payload.source_url || ''));

    try {
        await fetch(ZOHO_WEB_TO_LEAD.action, {
            method: 'POST',
            body: formData,
            cache: 'no-cache'
        });
    } catch(err) {
        console.warn('Advisor Zoho lead sync fallback:', err);
    }
};

// 6. Toast Success Message
function showToastNotification() {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 4000);
}

/* ==========================================================================
   SELF STORAGE INDIA — SECTION 2: STORAGE CALCULATOR INTERACTIVE LOGIC
   ========================================================================== */

const calcQty = {
    bed_king: 0,
    bed_single: 0,
    sofa_3: 0,
    sofa_single: 0,
    table: 0,
    chair: 0,
    wardrobe: 0,
    boxes: 0,
    luggage: 0,
    tv: 0,
    fridge: 0,
    washing: 0,
    ac: 0,
    desk: 0,
    folder: 0,
    bicycle: 0,
    inventory: 0,
    // Legacy keys for backwards compatibility
    sofa: 0,
    bed: 0,
    appliances: 0
};

const calcVolumes = {
    bed_king: 20,
    bed_single: 10,
    sofa_3: 15,
    sofa_single: 6,
    table: 10,
    chair: 3,
    wardrobe: 15,
    boxes: 2,
    luggage: 3,
    tv: 4,
    fridge: 10,
    washing: 8,
    ac: 6,
    desk: 12,
    folder: 1.5,
    bicycle: 8,
    inventory: 20,
    // Legacy keys
    sofa: 15,
    bed: 20,
    appliances: 10
};

const calcLabels = {
    bed_king: 'King / Double Bed',
    bed_single: 'Single Bed',
    sofa_3: '3-Seater Sofa',
    sofa_single: 'Armchair / Recliner',
    table: 'Dining Table',
    chair: 'Chair',
    wardrobe: 'Wardrobe / Almirah',
    boxes: 'Standard Box',
    luggage: 'Suitcase / Bag',
    tv: 'TV & Console',
    fridge: 'Refrigerator',
    washing: 'Washing Machine',
    ac: 'AC / Air Cooler',
    desk: 'Office Desk',
    folder: 'Document Carton',
    bicycle: 'Bicycle / Bike',
    inventory: 'Business Stock / Pallet',
    sofa: 'Sofa',
    bed: 'Bed',
    appliances: 'Appliances'
};

const calcPresets = {
    '1bhk': {
        bed_king: 1,
        sofa_3: 1,
        table: 1,
        chair: 4,
        wardrobe: 1,
        boxes: 10,
        tv: 1,
        fridge: 1,
        washing: 1
    },
    '2bhk': {
        bed_king: 2,
        sofa_3: 1,
        sofa_single: 2,
        table: 1,
        chair: 6,
        wardrobe: 2,
        boxes: 20,
        tv: 2,
        fridge: 1,
        washing: 1,
        ac: 1
    },
    '3bhk': {
        bed_king: 2,
        bed_single: 1,
        sofa_3: 2,
        sofa_single: 2,
        table: 1,
        chair: 6,
        wardrobe: 3,
        boxes: 30,
        tv: 2,
        fridge: 1,
        washing: 1,
        ac: 2
    },
    'luggage': {
        luggage: 4,
        boxes: 8,
        chair: 1,
        bicycle: 1
    },
    'office': {
        desk: 3,
        chair: 6,
        folder: 25,
        inventory: 2
    },
    'reset': {}
};

function updateItemQty(itemKey, change) {
    if (typeof calcQty[itemKey] === 'undefined') {
        calcQty[itemKey] = 0;
    }
    const newQty = Math.max(0, calcQty[itemKey] + change);
    calcQty[itemKey] = newQty;
    
    // Update individual display text if element exists
    const qtyEl = document.getElementById(`qty-${itemKey}`);
    if (qtyEl) qtyEl.innerText = newQty;

    // Toggle card visual active state
    const cardEl = document.querySelector(`.calc-item-card[data-item="${itemKey}"]`);
    if (cardEl) {
        if (newQty > 0) cardEl.classList.add('has-qty');
        else cardEl.classList.remove('has-qty');
    }

    renderCalculatorTotals();
}

function setItemQtyDirect(itemKey, qty) {
    calcQty[itemKey] = Math.max(0, qty);
    const qtyEl = document.getElementById(`qty-${itemKey}`);
    if (qtyEl) qtyEl.innerText = calcQty[itemKey];

    const cardEl = document.querySelector(`.calc-item-card[data-item="${itemKey}"]`);
    if (cardEl) {
        if (calcQty[itemKey] > 0) cardEl.classList.add('has-qty');
        else cardEl.classList.remove('has-qty');
    }
}

function applyCalcPreset(presetKey, btn) {
    // 1. Update preset button active styling
    if (btn) {
        document.querySelectorAll('.calc-preset-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }

    // 2. Clear all quantities first
    for (const key in calcQty) {
        setItemQtyDirect(key, 0);
    }

    // 3. Apply preset values
    const targetPreset = calcPresets[presetKey] || {};
    for (const key in targetPreset) {
        setItemQtyDirect(key, targetPreset[key]);
    }

    renderCalculatorTotals();
}

function filterCalcCategory(category, btn) {
    if (btn) {
        document.querySelectorAll('.calc-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }

    const cards = document.querySelectorAll('.calc-item-card');
    cards.forEach(card => {
        const itemCat = card.getAttribute('data-category');
        if (category === 'all' || itemCat === category) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

function removeCalcItem(itemKey) {
    setItemQtyDirect(itemKey, 0);
    renderCalculatorTotals();
}

function getCalculatorTier(sqFt) {
    if (sqFt === 0) {
        return {
            name: 'Select Items',
            tier: 'None',
            ideal: 'Select items or choose a 1-click home preset above',
            price: 'Starting from ₹1,200/mo',
            dimensions: 'Custom modular sizes available',
            clearance: '9.5 ft ceiling vertical clearance'
        };
    } else if (sqFt <= 40) {
        return {
            name: 'Personal Locker',
            tier: '20 – 40 sq. ft.',
            ideal: 'Ideal for luggage, study books, documents & 10–15 boxes',
            price: 'Starting from ₹1,200/mo',
            dimensions: 'approx. 5 ft × 6 ft × 9.5 ft ceiling',
            clearance: '9.5 ft ceiling (full height utilization)'
        };
    } else if (sqFt <= 75) {
        return {
            name: 'Small Private Room',
            tier: '50 – 75 sq. ft.',
            ideal: 'Ideal for 1 BHK apartment, double bed, sofa & 15+ cartons',
            price: 'Starting from ₹4,500/mo',
            dimensions: 'approx. 7.5 ft × 10 ft × 9.5 ft ceiling',
            clearance: '9.5 ft ceiling (stacking allowance included)'
        };
    } else if (sqFt <= 149) {
        return {
            name: 'Mid-Sized Private Room',
            tier: '76 – 149 sq. ft.',
            ideal: 'Ideal for 2 BHK home, 2 beds, living room & 25+ cartons',
            price: 'Starting from ₹7,500/mo',
            dimensions: 'approx. 10 ft × 12 ft × 9.5 ft ceiling',
            clearance: '9.5 ft ceiling (walkway & aisle clearance included)'
        };
    } else if (sqFt <= 199) {
        return {
            name: 'Large Private Room',
            tier: '150 – 199 sq. ft.',
            ideal: 'Ideal for 3 BHK home, multiple appliances & 40+ cartons',
            price: 'Starting from ₹12,000/mo',
            dimensions: 'approx. 12 ft × 15 ft × 9.5 ft ceiling',
            clearance: '9.5 ft ceiling (full household capacity)'
        };
    } else {
        return {
            name: 'Extra Large Commercial Suite',
            tier: '200 – 300+ sq. ft.',
            ideal: 'Ideal for large villas, corporate archives & business pallets',
            price: 'Starting from ₹16,000/mo',
            dimensions: 'approx. 15 ft × 20 ft × 10 ft ceiling',
            clearance: '10 ft ceiling (heavy industrial pallet capacity)'
        };
    }
}

function renderCalculatorTotals() {
    let totalVolumeSqFt = 0;
    let totalItemsCount = 0;
    const activeItems = [];

    for (const key in calcQty) {
        const qty = calcQty[key] || 0;
        if (qty > 0) {
            const vol = calcVolumes[key] || 0;
            totalVolumeSqFt += qty * vol;
            totalItemsCount += qty;
            activeItems.push({
                key: key,
                label: calcLabels[key] || key,
                qty: qty
            });
        }
    }

    const tierInfo = getCalculatorTier(totalVolumeSqFt);

    // 1. Update Visual storage unit fill
    const maxCapacity = 200;
    const fillPercent = Math.min(100, Math.round((totalVolumeSqFt / maxCapacity) * 100));
    
    const fillBar = document.getElementById('unit-fill');
    const fillPercentText = document.getElementById('unit-fill-percent');
    if (fillBar) fillBar.style.height = `${fillPercent}%`;
    if (fillPercentText) fillPercentText.innerText = `${fillPercent}% Filled`;

    // 2. Update Virtual Unit Grid Items (mini icons)
    const itemGrid = document.getElementById('unit-items-display');
    if (itemGrid) {
        itemGrid.innerHTML = '';
        activeItems.forEach(item => {
            let iconName = 'inventory_2';
            if (item.key.includes('bed')) iconName = 'bed';
            else if (item.key.includes('sofa')) iconName = 'weekend';
            else if (item.key === 'table') iconName = 'table_restaurant';
            else if (item.key === 'chair') iconName = 'chair';
            else if (item.key === 'wardrobe') iconName = 'dresser';
            else if (item.key === 'luggage') iconName = 'luggage';
            else if (item.key === 'tv') iconName = 'tv';
            else if (item.key === 'fridge') iconName = 'kitchen';
            else if (item.key === 'washing') iconName = 'local_laundry_service';
            else if (item.key === 'ac') iconName = 'mode_fan';
            else if (item.key === 'desk') iconName = 'desk';
            else if (item.key === 'folder') iconName = 'folder';
            else if (item.key === 'bicycle') iconName = 'pedal_bike';
            else if (item.key === 'inventory') iconName = 'warehouse';

            for (let i = 0; i < Math.min(item.qty, 4); i++) {
                const miniIcon = document.createElement('span');
                miniIcon.className = 'material-symbols-rounded mini-item-visual';
                miniIcon.innerText = iconName;
                itemGrid.appendChild(miniIcon);
            }
        });
    }

    // 3. Render Selected Items Chips List
    const chipsContainer = document.getElementById('calc-selected-chips');
    if (chipsContainer) {
        if (activeItems.length === 0) {
            chipsContainer.innerHTML = '<span class="no-items-label">No items selected yet. Tap + or choose a preset.</span>';
        } else {
            chipsContainer.innerHTML = activeItems.map(item => `
                <span class="calc-item-chip">
                    ${item.qty}× ${item.label}
                    <button type="button" onclick="removeCalcItem('${item.key}')" aria-label="Remove ${item.label}">&times;</button>
                </span>
            `).join('');
        }
    }

    // 4. Update Result Card
    const resultSize = document.getElementById('calc-result-size');
    const resultDesc = document.getElementById('calc-result-desc');
    const resultPrice = document.getElementById('calc-result-price');
    const resultTier = document.getElementById('calc-result-tier');
    const resultDim = document.getElementById('calc-result-dimensions');
    const ctaBtnText = document.getElementById('calc-cta-text');

    if (resultSize) resultSize.innerText = `${totalVolumeSqFt} sq ft`;
    if (resultDesc) resultDesc.innerText = tierInfo.ideal;
    if (resultPrice) resultPrice.innerText = `Est. Plan: ${tierInfo.price}`;
    if (resultTier) resultTier.innerText = tierInfo.name;
    if (resultDim) resultDim.innerText = tierInfo.dimensions;

    if (ctaBtnText) {
        if (totalVolumeSqFt > 0) {
            ctaBtnText.innerText = `Get Instant Quote for ${totalVolumeSqFt} sq ft (${tierInfo.name})`;
        } else {
            ctaBtnText.innerText = 'Select Items to Estimate Quote';
        }
    }

    // 5. Update Mobile Sticky Floating Bar
    const mobileBar = document.getElementById('calc-mobile-bar');
    const mobileSqFt = document.getElementById('calc-mobile-sqft');
    const mobileTier = document.getElementById('calc-mobile-tier');
    if (mobileBar) {
        if (totalVolumeSqFt > 0) {
            mobileBar.classList.add('visible');
            if (mobileSqFt) mobileSqFt.innerText = `${totalVolumeSqFt} sq ft`;
            if (mobileTier) mobileTier.innerText = tierInfo.name;
        } else {
            mobileBar.classList.remove('visible');
        }
    }
}

function handleCalculatorQuote() {
    let totalVolumeSqFt = 0;
    const selectedItems = [];

    for (const key in calcQty) {
        const qty = calcQty[key] || 0;
        if (qty > 0) {
            const vol = calcVolumes[key] || 0;
            totalVolumeSqFt += qty * vol;
            selectedItems.push(`${qty}x ${calcLabels[key] || key}`);
        }
    }

    const tierInfo = getCalculatorTier(totalVolumeSqFt);
    const planName = totalVolumeSqFt > 0
        ? `${totalVolumeSqFt} sq ft (${tierInfo.name})`
        : 'Storage Calculator Inquiry';

    const prefDescription = totalVolumeSqFt > 0
        ? `Storage Calculator: ${planName} | Items: ${selectedItems.join(', ')}`
        : 'Storage Calculator Inquiry';

    // 1. Update hidden Description field
    const sizeInput = document.getElementById('storage-size');
    if (sizeInput) sizeInput.value = prefDescription;

    // 2. Open quote modal
    openQuoteModal(prefDescription);

    // 3. Customize modal heading for maximum relevance
    const headingEl = document.getElementById('lfMainHeading');
    const subHeadingEl = document.getElementById('lfSubHeading');
    if (headingEl && totalVolumeSqFt > 0) {
        headingEl.textContent = `Get Free Quote for ${planName}`;
    }
    if (subHeadingEl && totalVolumeSqFt > 0) {
        const itemSummary = selectedItems.slice(0, 3).join(', ') + (selectedItems.length > 3 ? '...' : '');
        subHeadingEl.textContent = `We have reserved space recommendations ready for your items (${itemSummary}).`;
    }
}

/* ==========================================================================
   SELF STORAGE INDIA — SECTION 3: INTERACTIVE FACILITY MAP LOGIC
   ========================================================================== */

function focusLocCard(locKey) {
    const card = document.getElementById(`loc-card-${locKey}`);
    if (card) {
        card.classList.add('highlighted');
        card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

function blurLocCard(locKey) {
    const card = document.getElementById(`loc-card-${locKey}`);
    if (card) {
        card.classList.remove('highlighted');
    }
}

/* ==========================================================================
   SELF STORAGE INDIA — SECTION 4: ACCORDION FAQ LOGIC
   ========================================================================== */

function toggleFaq(trigger) {
    const item = trigger.parentElement;
    const content = trigger.nextElementSibling;

    // Close other items
    const allItems = document.querySelectorAll('.faq-accordion-item, .faq-item');
    allItems.forEach(otherItem => {
        if (otherItem !== item && otherItem.classList.contains('active')) {
            otherItem.classList.remove('active');
            const otherContent = otherItem.querySelector('.faq-content-box, .faq-answer');
            if (otherContent) otherContent.style.maxHeight = null;
        }
    });

    // Toggle current item
    const isActive = item.classList.contains('active');
    if (isActive) {
        item.classList.remove('active');
        if (content) content.style.maxHeight = null;
    } else {
        item.classList.add('active');
        if (content) content.style.maxHeight = content.scrollHeight + "px";
    }
}

// 6. Scroll Reveal Observer & Mobile Nav Link Auto-Close
document.addEventListener('DOMContentLoaded', () => {
    // Auto-close mobile menu when clicking nav links
    const navLinks = document.getElementById('navLinks');
    if (navLinks) {
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 900) {
                    closeMobileMenu();
                }
            });
        });
    }

    const revealOptions = {
        root: null,
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
    };

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
    const targetElements = document.querySelectorAll('.reveal-element');
    
    targetElements.forEach(element => {
        revealObserver.observe(element);
    });
});

// 7. Back-To-Top Button Logic
const backToTopBtn = document.getElementById('backToTopBtn');
if (backToTopBtn) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    }, { passive: true });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Smooth scrolling for header anchor links
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.navbar a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const hash = this.getAttribute('href');
            if (hash && hash !== '#') {
                const target = document.querySelector(hash);
                if (target) {
                    e.preventDefault();
                    closeMobileMenu();
                    setTimeout(() => {
                        const nav = document.querySelector('.navbar');
                        const navHeight = nav ? nav.offsetHeight : 76;
                        const top = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 12;
                        window.scrollTo({
                            top: Math.max(0, top),
                            behavior: 'smooth'
                        });
                        if (history.pushState) {
                            history.pushState(null, null, hash);
                        }
                    }, 50);
                }
            }
        });
    });
});


// Delegate whole card clicks to primary link within card
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.location-card:not(a), .offering-card:not(a)').forEach(card => {
        const link = card.querySelector('a');
        if (link) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', (e) => {
                if (e.target.closest('a') || e.target.closest('button')) return;
                link.click();
            });
        }
    });
});

// GitHub Pages subpath routing compatibility
if (window.location.pathname.startsWith('/ss')) {
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('a[href^="/"]').forEach(a => {
            const href = a.getAttribute('href');
            if (href && !href.startsWith('/ss') && !href.startsWith('//')) {
                a.setAttribute('href', '/ss' + (href === '/' ? '' : href));
            }
        });
    });
}

// 8. Storage Advisor Widget Integration ("Abha" Pattern)
(function() {
    if (window.location.pathname.indexOf('/thank-you') !== -1) return;
    
    var isGh = window.location.pathname.startsWith('/ss');
    var root = isGh ? '/ss/' : '/';
    if (window.location.protocol === 'file:') {
        var scriptTag = document.querySelector('script[src*="app"]');
        root = '';
        if (scriptTag && scriptTag.getAttribute('src')) {
            var src = scriptTag.getAttribute('src');
            var idx = src.lastIndexOf('app');
            if (idx !== -1) root = src.substring(0, idx);
        }
    }

    // Pre-inject stylesheet immediately into head so styles are ready before JS parses
    if (!document.getElementById('advisorStyles') && !document.querySelector('link[href*="storage-advisor"]')) {
        var link = document.createElement('link');
        link.id = 'advisorStyles';
        link.rel = 'stylesheet';
        link.href = root + 'storage-advisor.min.css?v=5.5';
        (document.head || document.documentElement).appendChild(link);
    }

    if (!document.querySelector('script[src*="storage-advisor"]')) {
        var s = document.createElement('script');
        s.src = root + 'storage-advisor.min.js?v=5.6';
        s.defer = true;
        (document.body || document.head || document.documentElement).appendChild(s);
    }
})();


// Prevent transition jerk on load
window.addEventListener('load', function() {
    setTimeout(function() {
        document.body.classList.remove('preload');
    }, 50);
});
