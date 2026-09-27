/**
 * Self Storage India — End-to-End Indian Household Storage Sizing Engine
 * Incorporating Calcumate 3D volumetric logic, 37 SSI facility unit tiers,
 * real-time isometric 3D canvas packing, and Zoho CRM lead integration.
 */

(function () {
  'use strict';

  // =========================================================================
  // 1. DATA: 33 SSI FACILITY UNITS (STARTING FROM TIER 2 - STANDARD 48 SQ FT)
  // =========================================================================
  const SSI_UNITS = [
    // Tier 2: Standard (45–68 sq ft)
    { id: 'u_8x6', name: 'Standard 8 X 6', w: 8, d: 6, h: 8, area: 48, vol: 384, tier: 'Tier 2 - Standard', price: 3800 },
    { id: 'u_7x7', name: 'Standard 7 X 7', w: 7, d: 7, h: 8, area: 49, vol: 392, tier: 'Tier 2 - Standard', price: 3900 },
    { id: 'u_10x5', name: 'Standard 10 X 5', w: 10, d: 5, h: 8, area: 50, vol: 400, tier: 'Tier 2 - Standard', price: 4000 },
    { id: 'u_9x6', name: 'Standard 9 X 6', w: 9, d: 6, h: 8, area: 54, vol: 432, tier: 'Tier 2 - Standard', price: 4300 },
    { id: 'u_11x5', name: 'Standard 11 X 5', w: 11, d: 5, h: 8, area: 55, vol: 440, tier: 'Tier 2 - Standard', price: 4500 },
    { id: 'u_8x7', name: 'Standard 8 X 7', w: 8, d: 7, h: 8, area: 56, vol: 448, tier: 'Tier 2 - Standard', price: 4600 },
    { id: 'u_12x5', name: 'Standard 12 X 5', w: 12, d: 5, h: 8, area: 60, vol: 480, tier: 'Tier 2 - Standard', price: 4900 },
    { id: 'u_10x6', name: 'Standard 10 X 6', w: 10, d: 6, h: 8, area: 60, vol: 480, tier: 'Tier 2 - Standard', price: 4900 },
    { id: 'u_11x6', name: 'Standard 11 X 6', w: 11, d: 6, h: 8, area: 66, vol: 528, tier: 'Tier 2 - Standard', price: 5400 },

    // Tier 3: Large (70–102 sq ft)
    { id: 'u_14x5', name: 'Large 14 X 5', w: 14, d: 5, h: 8, area: 70, vol: 560, tier: 'Tier 3 - Large', price: 5700 },
    { id: 'u_10x7', name: 'Large 10 X 7', w: 10, d: 7, h: 8, area: 70, vol: 560, tier: 'Tier 3 - Large', price: 5700 },
    { id: 'u_9x8', name: 'Large 9 X 8', w: 9, d: 8, h: 8, area: 72, vol: 576, tier: 'Tier 3 - Large', price: 5900 },
    { id: 'u_12x6', name: 'Large 12 X 6', w: 12, d: 6, h: 8, area: 72, vol: 576, tier: 'Tier 3 - Large', price: 5900 },
    { id: 'u_11x7', name: 'Large 11 X 7', w: 11, d: 7, h: 8, area: 77, vol: 616, tier: 'Tier 3 - Large', price: 6300 },
    { id: 'u_13x6', name: 'Large 13 X 6', w: 13, d: 6, h: 8, area: 78, vol: 624, tier: 'Tier 3 - Large', price: 6400 },
    { id: 'u_10x8', name: 'Large 10 X 8', w: 10, d: 8, h: 8, area: 80, vol: 640, tier: 'Tier 3 - Large', price: 6600 },
    { id: 'u_14x6', name: 'Large 14 X 6', w: 14, d: 6, h: 8, area: 84, vol: 672, tier: 'Tier 3 - Large', price: 6900 },
    { id: 'u_11x8', name: 'Large 11 X 8', w: 11, d: 8, h: 8, area: 88, vol: 704, tier: 'Tier 3 - Large', price: 7200 },
    { id: 'u_18x5', name: 'Large 18 X 5', w: 18, d: 5, h: 8, area: 90, vol: 720, tier: 'Tier 3 - Large', price: 7400 },
    { id: 'u_15x6', name: 'Large 15 X 6', w: 15, d: 6, h: 8, area: 90, vol: 720, tier: 'Tier 3 - Large', price: 7400 },
    { id: 'u_23x4', name: 'Large 23 X 4', w: 23, d: 4, h: 8, area: 92, vol: 736, tier: 'Tier 3 - Large', price: 7600 },
    { id: 'u_19x5', name: 'Large 19 X 5', w: 19, d: 5, h: 8, area: 95, vol: 760, tier: 'Tier 3 - Large', price: 7800 },
    { id: 'u_11x9', name: 'Large 11 X 9', w: 11, d: 9, h: 8, area: 99, vol: 792, tier: 'Tier 3 - Large', price: 8200 },

    // Tier 4: Extra Large (110–175 sq ft + custom up to 187 sq ft)
    { id: 'u_18x6', name: 'Extra Large 18 X 6', w: 18, d: 6, h: 8, area: 108, vol: 864, tier: 'Tier 4 - Extra Large', price: 8900 },
    { id: 'u_11x10', name: 'Extra Large 11 X 10', w: 11, d: 10, h: 8, area: 110, vol: 880, tier: 'Tier 4 - Extra Large', price: 9100 },
    { id: 'u_23x5', name: 'Extra Large 23 X 5', w: 23, d: 5, h: 8, area: 115, vol: 920, tier: 'Tier 4 - Extra Large', price: 9500 },
    { id: 'u_18x7', name: 'Extra Large 18 X 7', w: 18, d: 7, h: 8, area: 126, vol: 1008, tier: 'Tier 4 - Extra Large', price: 10400 },
    { id: 'u_14x9', name: 'Extra Large 14 X 9', w: 14, d: 9, h: 8, area: 126, vol: 1008, tier: 'Tier 4 - Extra Large', price: 10400 },
    { id: 'u_13x10', name: 'Extra Large 13 X 10', w: 13, d: 10, h: 8, area: 130, vol: 1040, tier: 'Tier 4 - Extra Large', price: 10700 },
    { id: 'u_13x11', name: 'Extra Large 13 X 11', w: 13, d: 11, h: 8, area: 143, vol: 1144, tier: 'Tier 4 - Extra Large', price: 11800 },
    { id: 'u_19x8', name: 'Extra Large 19 X 8', w: 19, d: 8, h: 8, area: 152, vol: 1216, tier: 'Tier 4 - Extra Large', price: 12500 },
    { id: 'u_19x9', name: 'Extra Large 19 X 9', w: 19, d: 9, h: 8, area: 171, vol: 1368, tier: 'Tier 4 - Extra Large', price: 14000 },
    { id: 'u_17x11', name: 'Extra Large 17 X 11', w: 17, d: 11, h: 8, area: 187, vol: 1496, tier: 'Tier 4 - Extra Large', price: 15400 }
  ];

  // =========================================================================
  // 2. DATA: INDIAN HOUSEHOLD ITEMS CATALOG (47 DETAILED ITEMS WITH BASE FOOTPRINT)
  // =========================================================================
  const INDIAN_ITEMS = [
    // --- LIVING ROOM ---
    { id: 'sofa_3', name: '3-Seater Living Sofa', cat: 'living', icon: 'weekend', cuFt: 50.4, w: 2.1, d: 0.85, h: 0.8, floorFootprint: 7.5, color: '#3b82f6' },
    { id: 'sofa_2', name: '2-Seater Sofa', cat: 'living', icon: 'weekend', cuFt: 36.0, w: 1.5, d: 0.85, h: 0.8, floorFootprint: 5.5, color: '#60a5fa' },
    { id: 'sofa_1', name: 'Recliner / Armchair', cat: 'living', icon: 'armchair', cuFt: 21.7, w: 0.85, d: 0.85, h: 0.85, floorFootprint: 4.0, color: '#93c5fd' },
    { id: 'sofa_l_shape', name: 'L-Shaped Sectional Sofa', cat: 'living', icon: 'weekend', cuFt: 86.8, w: 2.4, d: 1.6, h: 0.8, floorFootprint: 14.0, color: '#2563eb' },
    { id: 'diwan', name: 'Diwan Bed with Storage', cat: 'living', icon: 'bed', cuFt: 29.4, w: 1.85, d: 0.9, h: 0.5, floorFootprint: 8.0, color: '#f59e0b' },
    { id: 'center_table', name: 'Center / Coffee Table', cat: 'living', icon: 'table_restaurant', cuFt: 9.5, w: 1.0, d: 0.6, h: 0.45, floorFootprint: 2.0, color: '#d97706' },
    { id: 'tv_unit', name: 'TV Entertainment Unit', cat: 'living', icon: 'tv', cuFt: 11.9, w: 1.5, d: 0.45, h: 0.5, floorFootprint: 3.5, color: '#78350f' },
    { id: 'led_tv', name: 'LED Smart TV (Boxed)', cat: 'living', icon: 'tv', cuFt: 7.6, w: 1.4, d: 0.18, h: 0.85, floorFootprint: 1.0, color: '#1e293b' },
    { id: 'pooja_mandir', name: 'Pooja Mandir', cat: 'living', icon: 'temple_hindu', cuFt: 11.5, w: 0.6, d: 0.45, h: 1.2, floorFootprint: 2.0, color: '#b45309' },
    { id: 'bookshelf', name: 'Bookshelf / Display Rack', cat: 'living', icon: 'shelves', cuFt: 15.8, w: 0.8, d: 0.35, h: 1.6, floorFootprint: 2.5, color: '#475569' },
    { id: 'shoe_rack', name: 'Shoe Rack Cabinet', cat: 'living', icon: 'steps', cuFt: 8.9, w: 0.8, d: 0.35, h: 0.9, floorFootprint: 1.8, color: '#64748b' },

    // --- BEDROOM (Stored profile: Dismantled/Upright profile clearance) ---
    { id: 'bed_king', name: 'King Bed with Storage', cat: 'bedroom', icon: 'bed', cuFt: 58.8, w: 2.0, d: 0.9, h: 1.2, floorFootprint: 8.0, color: '#10b981' },
    { id: 'bed_queen', name: 'Queen Double Bed', cat: 'bedroom', icon: 'bed', cuFt: 49.3, w: 2.0, d: 0.85, h: 1.1, floorFootprint: 7.0, color: '#059669' },
    { id: 'bed_single', name: 'Single Bed / Diwan Cot', cat: 'bedroom', icon: 'single_bed', cuFt: 25.5, w: 1.9, d: 0.7, h: 0.9, floorFootprint: 4.5, color: '#34d399' },
    { id: 'mattress_double', name: 'King / Queen Mattress', cat: 'bedroom', icon: 'bed', cuFt: 22.6, w: 2.0, d: 0.35, h: 1.6, floorFootprint: 2.5, color: '#a7f3d0' },
    { id: 'almirah_2door', name: '2-Door Wardrobe / Almirah', cat: 'bedroom', icon: 'dresser', cuFt: 34.1, w: 0.9, d: 0.55, h: 1.95, floorFootprint: 5.0, color: '#047857' },
    { id: 'almirah_3door', name: '3-Door Large Wardrobe', cat: 'bedroom', icon: 'dresser', cuFt: 53.0, w: 1.4, d: 0.55, h: 1.95, floorFootprint: 7.5, color: '#065f46' },
    { id: 'dressing_table', name: 'Dressing Table with Mirror', cat: 'bedroom', icon: 'dresser', cuFt: 21.6, w: 0.8, d: 0.45, h: 1.7, floorFootprint: 3.5, color: '#14b8a6' },
    { id: 'bedside_tables', name: 'Bedside Tables (Pair)', cat: 'bedroom', icon: 'table_restaurant', cuFt: 6.4, w: 0.45, d: 0.4, h: 0.5, floorFootprint: 1.2, color: '#0d9488' },
    { id: 'razai_bundles', name: 'Quilt & Bedding Bundle', cat: 'bedroom', icon: 'inventory_2', cuFt: 9.5, w: 0.9, d: 0.6, h: 0.5, floorFootprint: 1.2, color: '#6ee7b7' },

    // --- KITCHEN & DINING ---
    { id: 'fridge_double', name: 'Double Door Refrigerator', cat: 'kitchen', icon: 'kitchen', cuFt: 30.3, w: 0.7, d: 0.7, h: 1.75, floorFootprint: 5.0, color: '#0284c7' },
    { id: 'fridge_single', name: 'Single Door Refrigerator', cat: 'kitchen', icon: 'kitchen', cuFt: 17.9, w: 0.6, d: 0.65, h: 1.3, floorFootprint: 4.0, color: '#38bdf8' },
    { id: 'dining_6', name: '6-Seater Dining Table', cat: 'kitchen', icon: 'table_restaurant', cuFt: 35.8, w: 1.5, d: 0.9, h: 0.75, floorFootprint: 6.0, color: '#e11d48' },
    { id: 'dining_4', name: '4-Seater Dining Table', cat: 'kitchen', icon: 'table_restaurant', cuFt: 23.3, w: 1.1, d: 0.8, h: 0.75, floorFootprint: 4.5, color: '#f43f5e' },
    { id: 'dining_chairs', name: 'Dining Chairs (Set of 4)', cat: 'kitchen', icon: 'chair', cuFt: 18.0, w: 0.5, d: 0.5, h: 0.95, floorFootprint: 2.5, color: '#fda4af' },
    { id: 'microwave', name: 'Microwave Oven / OTG', cat: 'kitchen', icon: 'microwave', cuFt: 3.1, w: 0.55, d: 0.45, h: 0.35, floorFootprint: 0.5, color: '#9f1239' },
    { id: 'gas_stove_cyl', name: 'Gas Stove & Cylinder', cat: 'kitchen', icon: 'propane_tank', cuFt: 5.5, w: 0.6, d: 0.4, h: 0.65, floorFootprint: 1.5, color: '#be123c' },
    { id: 'water_purifier', name: 'RO Water Purifier', cat: 'kitchen', icon: 'water_drop', cuFt: 2.3, w: 0.4, d: 0.3, h: 0.55, floorFootprint: 0.5, color: '#06b6d4' },

    // --- APPLIANCES & UTILITIES ---
    { id: 'washing_front', name: 'Front Load Washer', cat: 'appliances', icon: 'local_laundry_service', cuFt: 10.8, w: 0.6, d: 0.6, h: 0.85, floorFootprint: 3.8, color: '#8b5cf6' },
    { id: 'washing_top', name: 'Top Load Washer', cat: 'appliances', icon: 'local_laundry_service', cuFt: 9.6, w: 0.55, d: 0.55, h: 0.9, floorFootprint: 3.2, color: '#a78bfa' },
    { id: 'split_ac', name: 'Split AC (Indoor & Out)', cat: 'appliances', icon: 'mode_fan', cuFt: 6.7, w: 0.9, d: 0.35, h: 0.6, floorFootprint: 1.0, color: '#7c3aed' },
    { id: 'window_ac', name: 'Window AC Unit', cat: 'appliances', icon: 'mode_fan', cuFt: 6.7, w: 0.65, d: 0.65, h: 0.45, floorFootprint: 1.8, color: '#6d28d9' },
    { id: 'air_cooler', name: 'Desert Air Cooler', cat: 'appliances', icon: 'air', cuFt: 14.5, w: 0.65, d: 0.55, h: 1.15, floorFootprint: 3.5, color: '#c4b5fd' },
    { id: 'inverter_battery', name: 'Inverter & Battery Set', cat: 'appliances', icon: 'battery_charging_full', cuFt: 4.4, w: 0.5, d: 0.45, h: 0.55, floorFootprint: 2.0, color: '#4c1d95' },
    { id: 'geyser', name: 'Geyser / Water Heater', cat: 'appliances', icon: 'water_heater', cuFt: 4.6, w: 0.45, d: 0.45, h: 0.65, floorFootprint: 0.8, color: '#ec4899' },

    // --- BOXES, TRUNKS & LUGGAGE ---
    { id: 'box_large', name: 'Large Moving Carton', cat: 'boxes', icon: 'inventory_2', cuFt: 4.3, w: 0.6, d: 0.45, h: 0.45, floorFootprint: 0.6, color: '#f59e0b' },
    { id: 'box_medium', name: 'Medium Moving Carton', cat: 'boxes', icon: 'inventory_2', cuFt: 2.5, w: 0.45, d: 0.4, h: 0.4, floorFootprint: 0.4, color: '#fbbf24' },
    { id: 'box_small', name: 'Small Moving Carton', cat: 'boxes', icon: 'inventory_2', cuFt: 1.1, w: 0.35, d: 0.3, h: 0.3, floorFootprint: 0.2, color: '#fde68a' },
    { id: 'trunk_steel', name: 'Steel Trunk / Sandook', cat: 'boxes', icon: 'luggage', cuFt: 8.3, w: 0.95, d: 0.55, h: 0.45, floorFootprint: 4.5, color: '#64748b' },
    { id: 'suitcase_large', name: 'Large Trolley Suitcase', cat: 'boxes', icon: 'luggage', cuFt: 4.0, w: 0.75, d: 0.5, h: 0.3, floorFootprint: 0.8, color: '#475569' },
    { id: 'suitcase_cabin', name: 'Cabin Trolley / Duffle', cat: 'boxes', icon: 'luggage', cuFt: 1.7, w: 0.55, d: 0.35, h: 0.25, floorFootprint: 0.4, color: '#94a3b8' },

    // --- OFFICE, VEHICLES & EXTRA ---
    { id: 'two_wheeler', name: 'Two-Wheeler / Scooter', cat: 'office_vehicle', icon: 'two_wheeler', cuFt: 54.0, w: 1.9, d: 0.7, h: 1.15, floorFootprint: 15.0, color: '#dc2626' },
    { id: 'bicycle', name: 'Bicycle (Adult / Kids)', cat: 'office_vehicle', icon: 'pedal_bike', cuFt: 36.0, w: 1.7, d: 0.6, h: 1.0, floorFootprint: 7.0, color: '#ea580c' },
    { id: 'office_desk', name: 'Office Workstation / Desk', cat: 'office_vehicle', icon: 'desk', cuFt: 19.1, w: 1.2, d: 0.6, h: 0.75, floorFootprint: 4.5, color: '#0891b2' },
    { id: 'office_chair', name: 'Ergonomic Office Chair', cat: 'office_vehicle', icon: 'chair', cuFt: 17.2, w: 0.65, d: 0.65, h: 1.15, floorFootprint: 3.5, color: '#0e7490' },
    { id: 'archive_box', name: 'Archival Document Box', cat: 'office_vehicle', icon: 'folder', cuFt: 1.3, w: 0.4, d: 0.32, h: 0.28, floorFootprint: 0.25, color: '#ca8a04' },
    { id: 'fitness_gym', name: 'Treadmill / Gym Cycle', cat: 'office_vehicle', icon: 'fitness_center', cuFt: 55.1, w: 1.6, d: 0.75, h: 1.3, floorFootprint: 12.0, color: '#16a34a' }
  ];

  // =========================================================================
  // 3. PRESETS TAILORED FOR INDIAN APARTMENTS & HOMES
  // =========================================================================
  const INDIAN_PRESETS = {
    '1bhk': {
      label: '1 BHK Home (45–68 sq ft · Tier 2 - Standard)',
      items: {
        bed_queen: 1,
        mattress_double: 1,
        almirah_2door: 1,
        sofa_3: 1,
        center_table: 1,
        tv_unit: 1,
        led_tv: 1,
        fridge_double: 1,
        washing_front: 1,
        microwave: 1,
        box_large: 6,
        box_medium: 6,
        suitcase_large: 2,
        suitcase_cabin: 2
      }
    },
    '2bhk': {
      label: '2 BHK Home (70–102 sq ft · Tier 3 - Large)',
      items: {
        bed_king: 1,
        bed_queen: 1,
        mattress_double: 2,
        almirah_2door: 2,
        sofa_3: 1,
        center_table: 1,
        tv_unit: 1,
        led_tv: 1,
        dining_4: 1,
        dining_chairs: 1,
        fridge_double: 1,
        washing_front: 1,
        microwave: 1,
        split_ac: 2,
        pooja_mandir: 1,
        box_large: 8,
        box_medium: 8,
        suitcase_large: 3,
        suitcase_cabin: 2,
        trunk_steel: 1
      }
    },
    '3bhk': {
      label: '3 BHK Home (110–145 sq ft · Tier 4 - Extra Large)',
      items: {
        bed_king: 2,
        bed_single: 1,
        mattress_double: 2,
        almirah_3door: 1,
        almirah_2door: 2,
        dressing_table: 1,
        sofa_3: 1,
        sofa_2: 1,
        center_table: 1,
        tv_unit: 1,
        led_tv: 1,
        dining_6: 1,
        dining_chairs: 1,
        fridge_double: 1,
        washing_front: 1,
        microwave: 1,
        split_ac: 3,
        pooja_mandir: 1,
        shoe_rack: 1,
        box_large: 12,
        box_medium: 12,
        box_small: 6,
        trunk_steel: 1,
        suitcase_large: 4,
        suitcase_cabin: 3,
        bicycle: 1
      }
    },
    '4bhk': {
      label: '4 BHK / Villa (150–175 sq ft · Tier 4 - Extra Large)',
      items: {
        bed_king: 2,
        bed_queen: 1,
        bed_single: 1,
        mattress_double: 3,
        almirah_3door: 2,
        almirah_2door: 1,
        dressing_table: 1,
        sofa_3: 1,
        sofa_2: 1,
        sofa_1: 1,
        center_table: 1,
        tv_unit: 1,
        led_tv: 2,
        dining_6: 1,
        dining_chairs: 1,
        fridge_double: 1,
        washing_front: 1,
        microwave: 1,
        split_ac: 4,
        inverter_battery: 1,
        pooja_mandir: 1,
        bookshelf: 1,
        shoe_rack: 1,
        office_desk: 1,
        office_chair: 1,
        bicycle: 1,
        box_large: 16,
        box_medium: 16,
        box_small: 8,
        trunk_steel: 2,
        suitcase_large: 5,
        suitcase_cabin: 4,
        razai_bundles: 2
      }
    },
    'office': {
      label: 'Office & Business Storage (~70–100 sq ft · Tier 3 - Large)',
      items: {
        office_desk: 4,
        office_chair: 8,
        archive_box: 40,
        bookshelf: 2,
        box_medium: 15,
        sofa_2: 1,
        center_table: 1
      }
    }
  };

  // =========================================================================
  // 4. STATE MANAGEMENT
  // =========================================================================
  const state = {
    quantities: {}, // item_id -> quantity
    customItems: [], // [{ id, name, cuFt, w, d, h, qty }]
    activeCategory: 'all',
    searchQuery: '',
    viewMode: 'native', // 'native' | 'calcumate'
    angle3D: 'iso' // 'iso' | 'top' | 'front'
  };

  // Populate initial 0 quantities
  INDIAN_ITEMS.forEach(it => { state.quantities[it.id] = 0; });

  // =========================================================================
  // 5. PACKING & UNIT SELECTION ALGORITHM (DUAL CONSTRAINT: VOLUME & FLOOR AREA)
  // =========================================================================
  function calculateTotalInventory() {
    let totalCuFt = 0;
    let totalItems = 0;
    let reqFloorFootprint = 0;
    let maxLen = 0;
    let maxWid = 0;
    const inventoryList = [];

    // Catalog items
    INDIAN_ITEMS.forEach(it => {
      const q = state.quantities[it.id] || 0;
      if (q > 0) {
        totalCuFt += q * it.cuFt;
        reqFloorFootprint += q * (it.floorFootprint || (it.cuFt / 10));
        totalItems += q;
        inventoryList.push({ ...it, qty: q });

        const itLen = Math.max(it.w, it.d) * 3.28084;
        const itWid = Math.min(it.w, it.d) * 3.28084;
        if (itLen > maxLen) maxLen = itLen;
        if (itWid > maxWid) maxWid = itWid;
      }
    });

    // Custom items
    state.customItems.forEach(ci => {
      const q = ci.qty || 1;
      totalCuFt += q * ci.cuFt;
      reqFloorFootprint += q * (ci.w * 3.28084 * ci.d * 3.28084);
      totalItems += q;
      inventoryList.push({ ...ci, qty: q, isCustom: true, icon: 'extension', color: '#ec4899' });

      const ciLen = Math.max(ci.w, ci.d) * 3.28084;
      const ciWid = Math.min(ci.w, ci.d) * 3.28084;
      if (ciLen > maxLen) maxLen = ciLen;
      if (ciWid > maxWid) maxWid = ciWid;
    });

    return { totalCuFt, totalItems, reqFloorFootprint, maxLen, maxWid, inventoryList };
  }

  function getRecommendedUnit(inventoryData) {
    const totalCuFt = inventoryData.totalCuFt || 0;
    const reqFloorFootprint = inventoryData.reqFloorFootprint || 0;
    const maxLen = inventoryData.maxLen || 0;
    const maxWid = inventoryData.maxWid || 0;

    if (totalCuFt <= 0) {
      return {
        unit: null,
        nextUnit: null,
        utilizationPct: 0,
        requiredFloorArea: 0,
        statusText: 'Select items or choose a 1-click home preset above to calculate unit fit.',
        statusCode: 'empty'
      };
    }

    // Practical self-storage packing efficiency: 75% usable cubic volume accounting for voids & walkways
    const PACKING_EFFICIENCY = 0.75;
    const effectiveNeededCuFt = totalCuFt / PACKING_EFFICIENCY;
    // Mixed residential goods floor footprint: average real-world stacking density of 5.8 cu ft per sq ft
    const effectiveFloorArea = Math.max(reqFloorFootprint, totalCuFt / 5.8);

    // Match smallest unit from 33 SSI units (starting at Tier 2 - 48 sq ft)
    let matchedUnit = null;
    let nextUnit = null;

    for (let i = 0; i < SSI_UNITS.length; i++) {
      const u = SSI_UNITS[i];
      // 1. Must satisfy cubic volume requirement
      if (u.vol < effectiveNeededCuFt) continue;
      // 2. Must satisfy physical floor footprint requirement
      if (u.area < effectiveFloorArea) continue;
      // 3. Must fit the bulkiest single item dimensions
      const uMaxDim = Math.max(u.w, u.d);
      const uMinDim = Math.min(u.w, u.d);
      if (uMaxDim < maxLen || uMinDim < maxWid) continue;

      matchedUnit = u;
      nextUnit = SSI_UNITS[i + 1] || null;
      break;
    }

    // If items exceed the largest single unit (187 sq ft / 1496 cu ft)
    if (!matchedUnit) {
      const largest = SSI_UNITS[SSI_UNITS.length - 1];
      const mult = Math.max(
        Math.ceil(effectiveNeededCuFt / largest.vol),
        Math.ceil(effectiveFloorArea / largest.area)
      );
      matchedUnit = {
        id: 'multiple_units',
        name: `${mult}× Extra Large 17 X 11 Suites`,
        w: largest.w,
        d: largest.d,
        h: largest.h,
        mult: mult,
        area: largest.area * mult,
        vol: largest.vol * mult,
        tier: 'Multiple Private Suites',
        price: largest.price * mult,
        isMultiple: true
      };
    }

    // Realistic utilization: item volume as percentage of gross room volume
    const utilizationPct = Math.min(100, Math.round((totalCuFt / matchedUnit.vol) * 100));

    let statusText = 'Comfortable fit with room for access walkways.';
    let statusCode = 'good';
    if (inventoryData.totalItems <= 6 && totalCuFt < 45) {
      statusText = 'Entry private room size (48 sq ft). For smaller personal box or luggage lots, ask us about shared box storage plans!';
      statusCode = 'roomy';
    } else if (utilizationPct > 88) {
      statusText = 'Packed near capacity. Consider next size up for easier item retrieval.';
      statusCode = 'tight';
    } else if (utilizationPct > 78) {
      statusText = 'High density fit; vertical stacking recommended to preserve walkway.';
      statusCode = 'optimal';
    } else if (utilizationPct < 45) {
      statusText = 'Spacious unit with extra buffer for future additions.';
      statusCode = 'roomy';
    }

    return {
      unit: matchedUnit,
      nextUnit,
      utilizationPct,
      requiredFloorArea: Math.round(effectiveFloorArea),
      statusText,
      statusCode
    };
  }

  // =========================================================================
  // 6. 3D ISOMETRIC CANVAS VISUALIZER
  // =========================================================================
  function render3DCanvas(unit, items) {
    const canvas = document.getElementById('calc-3d-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // HiDPI support
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    const width = rect.width || 480;
    const height = rect.height || 300;

    if (canvas.width !== width * dpr || canvas.height !== height * dpr) {
      canvas.width = width * dpr;
      canvas.height = height * dpr;
    }

    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, width, height);

    if (!unit || items.length === 0) {
      // Empty room preview
      drawEmptyRoom(ctx, width, height);
      ctx.restore();
      return;
    }

    // Isometric projection helpers
    const unitW = unit.w || 10;
    const unitD = unit.d || 6;
    const unitH = unit.h || 8;

    const scale = Math.min(width / (unitW + unitD + 4), height / (unitH + unitD + 4)) * 1.5;
    const originX = width / 2;
    const originY = height * 0.72;

    function isoProject(x, y, z) {
      // x: width (right), y: depth (left-up), z: height (up)
      const isoX = originX + (x - y) * Math.cos(Math.PI / 6) * scale;
      const isoY = originY + (x + y) * Math.sin(Math.PI / 6) * scale * 0.6 - z * scale * 0.7;
      return { x: isoX, y: isoY };
    }

    // 1. Draw Unit Floor (Grid)
    ctx.beginPath();
    const p0 = isoProject(0, 0, 0);
    const pX = isoProject(unitW, 0, 0);
    const pXY = isoProject(unitW, unitD, 0);
    const pY = isoProject(0, unitD, 0);

    ctx.moveTo(p0.x, p0.y);
    ctx.lineTo(pX.x, pX.y);
    ctx.lineTo(pXY.x, pXY.y);
    ctx.lineTo(pY.x, pY.y);
    ctx.closePath();
    ctx.fillStyle = '#f8fafc';
    ctx.fill();
    ctx.strokeStyle = '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Floor 1ft grid lines
    ctx.strokeStyle = 'rgba(203, 213, 225, 0.4)';
    for (let gx = 1; gx < unitW; gx++) {
      const g0 = isoProject(gx, 0, 0);
      const g1 = isoProject(gx, unitD, 0);
      ctx.beginPath();
      ctx.moveTo(g0.x, g0.y);
      ctx.lineTo(g1.x, g1.y);
      ctx.stroke();
    }
    for (let gy = 1; gy < unitD; gy++) {
      const g0 = isoProject(0, gy, 0);
      const g1 = isoProject(unitW, gy, 0);
      ctx.beginPath();
      ctx.moveTo(g0.x, g0.y);
      ctx.lineTo(g1.x, g1.y);
      ctx.stroke();
    }

    // 2. Draw Back Walls (Private Room partition panels)
    // Left back wall
    ctx.beginPath();
    const pY_top = isoProject(0, unitD, unitH);
    const pXY_top = isoProject(unitW, unitD, unitH);
    ctx.moveTo(pY.x, pY.y);
    ctx.lineTo(pY_top.x, pY_top.y);
    ctx.lineTo(pXY_top.x, pXY_top.y);
    ctx.lineTo(pXY.x, pXY.y);
    ctx.closePath();
    ctx.fillStyle = '#e2e8f0';
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.stroke();

    // Wall vertical corrugated lines
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.2)';
    for (let wx = 1; wx < unitW; wx++) {
      const b0 = isoProject(wx, unitD, 0);
      const b1 = isoProject(wx, unitD, unitH);
      ctx.beginPath();
      ctx.moveTo(b0.x, b0.y);
      ctx.lineTo(b1.x, b1.y);
      ctx.stroke();
    }

    // 3. Draw Packed Items as 3D Isometric Bounding Boxes
    drawPackedItems(ctx, isoProject, unitW, unitD, unitH, items);

    // 4. Draw Front Unit Dimensions & Shutter Header
    ctx.fillStyle = '#0f172a';
    ctx.font = '600 11px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    const dimWidthPos = isoProject(unitW / 2, 0, 0);
    ctx.fillText(`${unitW} ft Width`, dimWidthPos.x + 10, dimWidthPos.y + 18);

    const dimDepthPos = isoProject(0, unitD / 2, 0);
    ctx.fillText(`${unitD} ft Depth`, dimDepthPos.x - 22, dimDepthPos.y + 12);

    ctx.restore();
  }

  function drawEmptyRoom(ctx, width, height) {
    ctx.textAlign = 'center';
    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 13px "Plus Jakarta Sans", sans-serif';
    ctx.fillText('Virtual 3D Room will render as items are added', width / 2, height / 2 - 10);
    ctx.font = '700 12px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#2563eb';
    ctx.fillText('Select items or tap a 1-click preset below', width / 2, height / 2 + 14);
  }

  function drawPackedItems(ctx, isoProject, maxW, maxD, maxH, items) {
    // Deterministic procedural packing stacker
    let curX = 0.5;
    let curY = 0.5;
    let curZ = 0;
    let rowMaxD = 0;

    items.forEach((item) => {
      for (let i = 0; i < item.qty; i++) {
        const itemW = Math.max(0.8, Math.min(item.w ? item.w * 3.28 : 2.5, 5));
        const itemD = Math.max(0.8, Math.min(item.d ? item.d * 3.28 : 2.0, 4));
        const itemH = Math.max(0.6, Math.min(item.h ? item.h * 3.28 : 2.0, 5));

        // Check if fits in current row
        if (curX + itemW > maxW - 0.5) {
          curX = 0.5;
          curY += rowMaxD + 0.3;
          rowMaxD = 0;
        }

        if (curY + itemD > maxD - 0.5) {
          // Stack on top
          curX = 0.5;
          curY = 0.5;
          curZ = Math.min(maxH - 1, curZ + 1.8);
        }

        rowMaxD = Math.max(rowMaxD, itemD);

        // Render 3D isometric box
        drawIsoBox(ctx, isoProject, curX, curY, curZ, itemW, itemD, itemH, item.color || '#3b82f6');

        curX += itemW + 0.2;
      }
    });
  }

  function drawIsoBox(ctx, isoProject, x, y, z, w, d, h, color) {
    const p0 = isoProject(x, y, z);
    const p1 = isoProject(x + w, y, z);
    const p2 = isoProject(x + w, y + d, z);
    const p3 = isoProject(x, y + d, z);

    const t0 = isoProject(x, y, z + h);
    const t1 = isoProject(x + w, y, z + h);
    const t2 = isoProject(x + w, y + d, z + h);
    const t3 = isoProject(x, y + d, z + h);

    // Top Face (lightest)
    ctx.beginPath();
    ctx.moveTo(t0.x, t0.y);
    ctx.lineTo(t1.x, t1.y);
    ctx.lineTo(t2.x, t2.y);
    ctx.lineTo(t3.x, t3.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, 20);
    ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.15)';
    ctx.stroke();

    // Right / Front Face (medium)
    ctx.beginPath();
    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(t1.x, t1.y);
    ctx.lineTo(t2.x, t2.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, -10);
    ctx.fill();
    ctx.stroke();

    // Left Face (darkest)
    ctx.beginPath();
    ctx.moveTo(p0.x, p0.y);
    ctx.lineTo(t0.x, t0.y);
    ctx.lineTo(t1.x, t1.y);
    ctx.lineTo(p1.x, p1.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, 5);
    ctx.fill();
    ctx.stroke();
  }

  function shadeColor(color, percent) {
    let R = parseInt(color.substring(1, 3), 16);
    let G = parseInt(color.substring(3, 5), 16);
    let B = parseInt(color.substring(5, 7), 16);

    R = parseInt((R * (100 + percent)) / 100);
    G = parseInt((G * (100 + percent)) / 100);
    B = parseInt((B * (100 + percent)) / 100);

    R = R < 255 ? R : 255;
    G = G < 255 ? G : 255;
    B = B < 255 ? B : 255;

    const RR = R.toString(16).length === 1 ? '0' + R.toString(16) : R.toString(16);
    const GG = G.toString(16).length === 1 ? '0' + G.toString(16) : G.toString(16);
    const BB = B.toString(16).length === 1 ? '0' + B.toString(16) : B.toString(16);

    return '#' + RR + GG + BB;
  }

  // =========================================================================
  // 7. UI RENDERER & INTERACTION CONTROLLER
  // =========================================================================
  function renderAll() {
    const invData = calculateTotalInventory();
    const result = getRecommendedUnit(invData);
    const { totalCuFt, totalItems, inventoryList } = invData;

    // 1. Update live result metrics
    const unitNameEl = document.getElementById('calc-unit-name');
    const unitDimEl = document.getElementById('calc-unit-dims');
    const unitAreaEl = document.getElementById('calc-unit-area');
    const unitVolEl = document.getElementById('calc-unit-volume');
    const unitPriceEl = document.getElementById('calc-unit-price');
    const utilBarEl = document.getElementById('calc-util-bar');
    const utilPctEl = document.getElementById('calc-util-percent');
    const statusNoteEl = document.getElementById('calc-status-note');
    const ctaBtnText = document.getElementById('calc-cta-text');
    const tierBadgeEl = document.getElementById('calc-tier-badge');

    if (result.unit) {
      if (tierBadgeEl) tierBadgeEl.innerText = result.unit.tier;
      if (unitNameEl) unitNameEl.innerText = `${result.unit.tier} (${result.unit.name})`;
      if (unitDimEl) {
        if (result.unit.isMultiple) {
          unitDimEl.innerText = `${result.unit.mult} Suites of ${result.unit.w} ft × ${result.unit.d} ft (${result.unit.h} ft Ceiling)`;
        } else {
          unitDimEl.innerText = `${result.unit.w} ft × ${result.unit.d} ft × ${result.unit.h} ft Ceiling`;
        }
      }
      if (unitAreaEl) unitAreaEl.innerText = `${result.unit.area} sq ft`;
      if (unitVolEl) unitVolEl.innerText = `${result.unit.vol} cu ft`;
      if (unitPriceEl) unitPriceEl.innerText = `Starting from ₹${result.unit.price.toLocaleString('en-IN')}/mo`;
      if (utilBarEl) {
        utilBarEl.style.width = `${result.utilizationPct}%`;
        if (result.statusCode === 'tight') {
          utilBarEl.style.background = 'linear-gradient(90deg, #f59e0b, #d97706)';
        } else if (result.statusCode === 'optimal' || result.statusCode === 'good') {
          utilBarEl.style.background = 'linear-gradient(90deg, #10b981, #059669)';
        } else {
          utilBarEl.style.background = 'linear-gradient(90deg, #2563eb, #3b82f6)';
        }
      }
      if (utilPctEl) utilPctEl.innerText = `${result.utilizationPct}% Filled`;
      if (statusNoteEl) statusNoteEl.innerText = result.statusText;
      if (ctaBtnText) ctaBtnText.innerText = `Book ${result.unit.tier} (${result.unit.area} sq ft) →`;
    } else {
      if (tierBadgeEl) tierBadgeEl.innerText = 'Tier 2 - Standard';
      if (unitNameEl) unitNameEl.innerText = 'Select Items or Preset';
      if (unitDimEl) unitDimEl.innerText = 'Standard facility rooms (48–187 sq ft)';
      if (unitAreaEl) unitAreaEl.innerText = '0 sq ft';
      if (unitVolEl) unitVolEl.innerText = '0 cu ft';
      if (unitPriceEl) unitPriceEl.innerText = 'Starting from ₹3,800/mo (Tier 2 Standard)';
      if (utilBarEl) {
        utilBarEl.style.width = '0%';
        utilBarEl.style.background = 'linear-gradient(90deg, #2563eb, #3b82f6)';
      }
      if (utilPctEl) utilPctEl.innerText = '0% Filled';
      if (statusNoteEl) statusNoteEl.innerText = 'Tap + on items or choose a 1-click home/office preset below.';
      if (ctaBtnText) ctaBtnText.innerText = 'Select Items or Request Free Sizing Advice';
    }

    // 2. Render item counter badges on cards
    INDIAN_ITEMS.forEach(it => {
      const q = state.quantities[it.id] || 0;
      const countEl = document.getElementById(`qty-${it.id}`);
      const cardEl = document.getElementById(`item-card-${it.id}`);
      if (countEl) countEl.innerText = q;
      if (cardEl) {
        if (q > 0) cardEl.classList.add('active-item');
        else cardEl.classList.remove('active-item');
      }
    });

    // 3. Render Inventory Summary Drawer / Chips
    const inventoryChipsEl = document.getElementById('calc-inventory-chips');
    const totalItemsCountEl = document.getElementById('calc-total-items-count');
    if (totalItemsCountEl) totalItemsCountEl.innerText = `${totalItems} items`;

    if (inventoryChipsEl) {
      if (inventoryList.length === 0) {
        inventoryChipsEl.innerHTML = '<span class="empty-inv-msg">No items in your storage plan yet.</span>';
      } else {
        inventoryChipsEl.innerHTML = inventoryList.map(it => `
          <div class="inv-chip">
            <span class="inv-chip-name">${it.qty}× ${it.name}</span>
            <button type="button" class="inv-chip-del" onclick="window.SSI_CALCULATOR.setItemQty('${it.id}', 0, ${it.isCustom ? 'true' : 'false'})" aria-label="Remove ${it.name}">&times;</button>
          </div>
        `).join('');
      }
    }

    // 4. Update Sticky Mobile Bar
    const mobileBar = document.getElementById('calc-mobile-bar');
    const mobileSqFt = document.getElementById('calc-mobile-sqft');
    const mobileTier = document.getElementById('calc-mobile-tier');
    if (mobileBar) {
      if (totalCuFt > 0 && result.unit) {
        mobileBar.classList.add('visible');
        if (mobileSqFt) mobileSqFt.innerText = `${result.unit.area} sq ft · ₹${result.unit.price.toLocaleString('en-IN')}/mo`;
        if (mobileTier) mobileTier.innerText = result.unit.name;
      } else {
        mobileBar.classList.remove('visible');
      }
    }

    // 5. Draw 3D Isometric Canvas
    render3DCanvas(result.unit, inventoryList);
  }

  // =========================================================================
  // 8. PUBLIC API & EVENT HANDLERS
  // =========================================================================
  window.SSI_CALCULATOR = {
    updateQty: function (id, delta) {
      state.quantities[id] = Math.max(0, (state.quantities[id] || 0) + delta);
      renderAll();
    },

    setItemQty: function (id, qty, isCustom) {
      if (isCustom) {
        state.customItems = state.customItems.filter(ci => ci.id !== id);
      } else {
        state.quantities[id] = Math.max(0, qty);
      }
      renderAll();
    },

    applyPreset: function (presetKey, btn) {
      if (btn) {
        document.querySelectorAll('.calc-preset-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }

      // Reset first
      INDIAN_ITEMS.forEach(it => { state.quantities[it.id] = 0; });
      state.customItems = [];

      const preset = INDIAN_PRESETS[presetKey];
      if (preset && preset.items) {
        for (const id in preset.items) {
          state.quantities[id] = preset.items[id];
        }
      }
      renderAll();
    },

    resetAll: function () {
      INDIAN_ITEMS.forEach(it => { state.quantities[it.id] = 0; });
      state.customItems = [];
      document.querySelectorAll('.calc-preset-pill').forEach(b => b.classList.remove('active'));
      renderAll();
    },

    filterCategory: function (cat, btn) {
      state.activeCategory = cat;
      if (btn) {
        document.querySelectorAll('.calc-cat-pill').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }

      const cards = document.querySelectorAll('.calc-inv-card');
      cards.forEach(card => {
        const itemCat = card.getAttribute('data-cat');
        const itemName = card.getAttribute('data-name').toLowerCase();
        const matchesCat = (cat === 'all' || itemCat === cat);
        const matchesSearch = (!state.searchQuery || itemName.includes(state.searchQuery));

        if (matchesCat && matchesSearch) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    },

    searchItems: function (query) {
      state.searchQuery = (query || '').toLowerCase().trim();
      const cards = document.querySelectorAll('.calc-inv-card');
      cards.forEach(card => {
        const itemCat = card.getAttribute('data-cat');
        const itemName = card.getAttribute('data-name').toLowerCase();
        const matchesCat = (state.activeCategory === 'all' || itemCat === state.activeCategory);
        const matchesSearch = (!state.searchQuery || itemName.includes(state.searchQuery));

        if (matchesCat && matchesSearch) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    },


    handleQuote: function () {
      const invData = calculateTotalInventory();
      const result = getRecommendedUnit(invData);
      const { totalCuFt, totalItems, inventoryList } = invData;

      if (!result.unit || totalItems === 0) {
        const description = 'Storage Sizing Consultation Request (Self Storage Calculator)';
        const sizeInput = document.getElementById('storage-size');
        if (sizeInput) sizeInput.value = description;

        if (window.openQuoteModal) {
          window.openQuoteModal(description);
        } else if (window.ModalController) {
          window.ModalController.open(description);
        }

        const headingEl = document.getElementById('lfMainHeading');
        const subHeadingEl = document.getElementById('lfSubHeading');
        if (headingEl) headingEl.textContent = 'Get Free Storage Sizing Advice';
        if (subHeadingEl) subHeadingEl.textContent = 'Tell us what you plan to store and our storage experts will calculate the perfect unit size for you.';
        return;
      }

      const itemSummary = inventoryList.map(it => `${it.qty}x ${it.name}`).join(', ');
      const description = `Storage Calculator: ${result.unit.tier} - ${result.unit.name} (${result.unit.area} sq ft, ${result.unit.vol} cu ft) | ${result.utilizationPct}% Utilized | Inventory: ${itemSummary}`;

      // Update hidden storage-size
      const sizeInput = document.getElementById('storage-size');
      if (sizeInput) sizeInput.value = description;

      if (window.openQuoteModal) {
        window.openQuoteModal(description);
      } else if (window.ModalController) {
        window.ModalController.open(description);
      }

      // Contextual title
      const headingEl = document.getElementById('lfMainHeading');
      const subHeadingEl = document.getElementById('lfSubHeading');
      if (headingEl) headingEl.textContent = `Get Free Quote for ${result.unit.tier} (${result.unit.area} sq ft)`;
      if (subHeadingEl) subHeadingEl.textContent = `Unit reserved for your ${totalItems} items. Transparent pricing guaranteed.`;
    },

    toggleViewMode: function () {}
  };

  // Global aliases for legacy/inline button triggers
  window.handleCalculatorQuote = window.SSI_CALCULATOR.handleQuote;
  window.applyCalcPreset = window.SSI_CALCULATOR.applyPreset;
  window.filterCalcCategory = window.SSI_CALCULATOR.filterCategory;
  window.updateItemQty = window.SSI_CALCULATOR.updateQty;

  // =========================================================================
  // 9. DOM INITIALIZATION
  // =========================================================================
  document.addEventListener('DOMContentLoaded', function () {
    // Generate Item Cards HTML
    const gridEl = document.getElementById('calc-items-grid-container');
    if (gridEl) {
      gridEl.innerHTML = INDIAN_ITEMS.map(it => `
        <div class="calc-inv-card" id="item-card-${it.id}" data-id="${it.id}" data-cat="${it.cat}" data-name="${it.name}">
          <div class="inv-card-header">
            <span class="material-symbols-rounded inv-card-icon" style="color: ${it.color};">${it.icon}</span>
            <div class="inv-card-info">
              <span class="inv-card-name" title="${it.name}">${it.name}</span>
            </div>
          </div>
          <div class="inv-card-controls">
            <button type="button" class="inv-btn-dec" onclick="window.SSI_CALCULATOR.updateQty('${it.id}', -1)" aria-label="Decrease ${it.name}">—</button>
            <span class="inv-qty-display" id="qty-${it.id}">0</span>
            <button type="button" class="inv-btn-inc" onclick="window.SSI_CALCULATOR.updateQty('${it.id}', 1)" aria-label="Increase ${it.name}">+</button>
          </div>
        </div>
      `).join('');
    }

    renderAll();
  });

})();
