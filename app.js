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
    }
}

function closeMobileMenu() {
    const navLinks = document.getElementById('navLinks');
    const overlay = document.getElementById('mobileNavOverlay');
    if (navLinks) navLinks.classList.remove('mobile-open');
    if (overlay) overlay.classList.remove('active');
    document.body.classList.remove('no-scroll');
}

// 2. Quote Modal Toggle Functions
function openQuoteModal() {
    const modal = document.getElementById('quote-modal');
    if (modal) modal.classList.add('open');
    document.body.classList.add('quote-modal-open');
}

function closeQuoteModal(event) {
    const modal = document.getElementById('quote-modal');
    if (!event || event.target === modal) {
        if (modal) modal.classList.remove('open');
        document.body.classList.remove('quote-modal-open');
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
    xnQsjsdp: 'a979ecd831c0e0cc3021561407927e41ccad53ba7f9728c54ff061b222e0eb6c',
    xmIwtLD: '0554b4515d63426b46b3bc2afad2cbd7fb8d66685ba40768b173c282051a2e9df93658768a3fc0ab3706c8f4d36586b4',
    actionType: 'TGVhZHM=',
    wFaTrisJS: 'true'
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
    var formData = new FormData();
    formData.append('xnQsjsdp', ZOHO_WEB_TO_LEAD.xnQsjsdp);
    formData.append('xmIwtLD', ZOHO_WEB_TO_LEAD.xmIwtLD);
    formData.append('actionType', ZOHO_WEB_TO_LEAD.actionType);
    formData.append('returnURL', returnUrl);
    formData.append('wFaTrisJS', ZOHO_WEB_TO_LEAD.wFaTrisJS);
    formData.append('aG9uZXlwb3Q', '');
    formData.append('zc_gad', '');
    formData.append('ldeskuid', '');
    formData.append('LDTuvid', (window.$zoho && window.$zoho.salesiq && window.$zoho.salesiq.visitor) ? window.$zoho.salesiq.visitor.uniqueid() : '');
    formData.append('Last Name', nameVal);
    formData.append('Phone', formattedPhone);
    formData.append('Email', emailVal);
    formData.append('Description', 'Selected Space/Location: ' + sizeVal + ' | Landing Page: ' + window.location.pathname + ' | Referrer: ' + (document.referrer || 'Direct'));

    try {
        await fetch(ZOHO_WEB_TO_LEAD.action, {
            method: 'POST',
            body: formData,
            cache: 'no-cache'
        });

        // Also fire custom tracking event
        window.dispatchEvent(new CustomEvent('quote_lead_submitted', {
            detail: { name: nameVal, phone: phoneVal, email: emailVal, size: sizeVal }
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
    formData.append('wFaTrisJS', ZOHO_WEB_TO_LEAD.wFaTrisJS);
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
    sofa: 0,
    bed: 0,
    table: 0,
    chair: 0,
    wardrobe: 0,
    boxes: 0,
    luggage: 0,
    tv: 0,
    folder: 0,
    appliances: 0,
    bicycle: 0,
    inventory: 0
};

const calcVolumes = {
    sofa: 15,
    bed: 20,
    table: 10,
    chair: 3,
    wardrobe: 15,
    boxes: 2,
    luggage: 3,
    tv: 4,
    folder: 1,
    appliances: 12,
    bicycle: 8,
    inventory: 25
};

function updateItemQty(itemKey, change) {
    // 1. Calculate new quantity
    const newQty = calcQty[itemKey] + change;
    if (newQty < 0) return; // Prevent negative values
    
    // 2. Save state & update display text
    calcQty[itemKey] = newQty;
    document.getElementById(`qty-${itemKey}`).innerText = newQty;
    
    // 3. Calculate total volume needed
    let totalVolumeSqFt = 0;
    let totalItemsCount = 0;
    for (const key in calcQty) {
        totalVolumeSqFt += calcQty[key] * calcVolumes[key];
        totalItemsCount += calcQty[key];
    }
    
    // 4. Update the visual storage unit box
    const maxCapacityVolume = 150; // The threshold where the unit is considered 100% full
    const fillPercent = Math.min(100, Math.round((totalVolumeSqFt / maxCapacityVolume) * 100));
    
    const fillBar = document.getElementById('unit-fill');
    const fillPercentText = document.getElementById('unit-fill-percent');
    
    fillBar.style.height = `${fillPercent}%`;
    fillPercentText.innerText = `${fillPercent}% Full`;
    
    // 5. Visual: Update virtual box items inside the visual grid
    const itemGrid = document.getElementById('unit-items-display');
    itemGrid.innerHTML = ''; // Clear previous items
    
    // Populate miniature icons in the virtual unit based on items added
    for (const key in calcQty) {
        if (calcQty[key] > 0) {
            let materialIconName = 'inventory_2';
            // map keys to icons
            if (key === 'sofa') materialIconName = 'weekend';
            else if (key === 'bed') materialIconName = 'bed';
            else if (key === 'table') materialIconName = 'table_restaurant';
            else if (key === 'chair') materialIconName = 'chair';
            else if (key === 'wardrobe') materialIconName = 'dresser';
            else if (key === 'boxes') materialIconName = 'inventory_2';
            else if (key === 'luggage') materialIconName = 'luggage';
            else if (key === 'tv') materialIconName = 'tv';
            else if (key === 'folder') materialIconName = 'folder';
            else if (key === 'appliances') materialIconName = 'kitchen';
            else if (key === 'bicycle') materialIconName = 'pedal_bike';
            else if (key === 'inventory') materialIconName = 'warehouse';
            
            for (let i = 0; i < Math.min(calcQty[key], 6); i++) {
                const miniIcon = document.createElement('span');
                miniIcon.className = 'material-symbols-rounded mini-item-visual';
                miniIcon.innerText = materialIconName;
                itemGrid.appendChild(miniIcon);
            }
        }
    }
    
    // 6. Update Live Result Card Values
    const resultSize = document.getElementById('calc-result-size');
    const resultDesc = document.getElementById('calc-result-desc');
    const resultPrice = document.getElementById('calc-result-price');
    
    if (totalVolumeSqFt === 0) {
        resultSize.innerText = '0 sq ft';
        resultDesc.innerText = 'Select items to calculate space';
        resultPrice.innerText = 'Estimated Monthly Plan: Starting from ₹1,200';
    } else {
        resultSize.innerText = `${totalVolumeSqFt} sq ft`;
        
        let planDescription = 'Ideal for document storage and luggage';
        let startingPriceVal = 1200 + (totalVolumeSqFt * 75);
        
        if (totalVolumeSqFt <= 15) {
            planDescription = 'Locker (ideal for luggage, documents)';
        } else if (totalVolumeSqFt <= 45) {
            planDescription = 'Small Room (ideal for 1BHK / Studio items)';
        } else if (totalVolumeSqFt <= 90) {
            planDescription = 'Medium Room (ideal for 2BHK furniture)';
        } else {
            planDescription = 'Large Room (ideal for 3BHK+ / Startup inventory)';
        }
        
        resultDesc.innerText = `Ideal for: ${planDescription}`;
        resultPrice.innerText = `Estimated Monthly Plan: Starting from ₹${startingPriceVal.toLocaleString('en-IN')}`;
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
    if (document.querySelector('script[src*="storage-advisor"]')) return;
    var s = document.createElement('script');
    var scriptTag = document.querySelector('script[src*="app"]');
    var basePath = '';
    if (scriptTag && scriptTag.getAttribute('src')) {
        var src = scriptTag.getAttribute('src');
        var idx = src.lastIndexOf('app');
        if (idx !== -1) basePath = src.substring(0, idx);
    }
    s.src = basePath + 'storage-advisor.min.js?v=5.0';
    s.defer = true;
    document.body.appendChild(s);
})();
