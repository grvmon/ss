/**
 * Self Storage India — End-to-End Indian Household Storage Sizing Engine
 * Incorporating Calcumate 3D volumetric logic, 37 SSI facility unit tiers,
 * real-time isometric 3D canvas packing, and Zoho CRM lead integration.
 */

(function () {
  'use strict';

  // =========================================================================
  // 1. DATA: SSI FACILITY UNITS (TIER 1 THROUGH TIER 4: 24 TO 187 SQ FT)
  // =========================================================================
  const SSI_UNITS = [
    // Tier 1: Personal Locker / Mini Room (15–44 sq ft)
    { id: 'u_6x4', name: 'Mini Locker 6 X 4', w: 6, d: 4, h: 8, area: 24, vol: 192, tier: 'Tier 1 - Personal / Locker', price: 2000 },
    { id: 'u_8x4', name: 'Small Room 8 X 4', w: 8, d: 4, h: 8, area: 32, vol: 256, tier: 'Tier 1 - Personal / Locker', price: 2600 },
    { id: 'u_9x4', name: 'Small Room 9 X 4', w: 9, d: 4, h: 8, area: 36, vol: 288, tier: 'Tier 1 - Personal / Locker', price: 2900 },
    { id: 'u_8x5', name: 'Small Room 8 X 5', w: 8, d: 5, h: 8, area: 40, vol: 320, tier: 'Tier 1 - Personal / Locker', price: 3200 },
    { id: 'u_11x4', name: 'Small Room 11 X 4', w: 11, d: 4, h: 8, area: 44, vol: 352, tier: 'Tier 1 - Personal / Locker', price: 3500 },

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
    { id: 'sofa_1', name: 'Recliner / Armchair', cat: 'living', icon: 'chair', cuFt: 21.7, w: 0.85, d: 0.85, h: 0.85, floorFootprint: 4.0, color: '#93c5fd' },
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

    // --- KITCHEN & APPLIANCES ---
    { id: 'fridge_double', name: 'Double Door Refrigerator', cat: 'kitchen_appliances', icon: 'kitchen', cuFt: 30.3, w: 0.7, d: 0.7, h: 1.75, floorFootprint: 5.0, color: '#0284c7' },
    { id: 'fridge_single', name: 'Single Door Refrigerator', cat: 'kitchen_appliances', icon: 'kitchen', cuFt: 17.9, w: 0.6, d: 0.65, h: 1.3, floorFootprint: 4.0, color: '#38bdf8' },
    { id: 'dining_6', name: '6-Seater Dining Table', cat: 'kitchen_appliances', icon: 'table_restaurant', cuFt: 35.8, w: 1.5, d: 0.9, h: 0.75, floorFootprint: 6.0, color: '#e11d48' },
    { id: 'dining_4', name: '4-Seater Dining Table', cat: 'kitchen_appliances', icon: 'table_restaurant', cuFt: 23.3, w: 1.1, d: 0.8, h: 0.75, floorFootprint: 4.5, color: '#f43f5e' },
    { id: 'dining_chairs', name: 'Dining Chairs (Set of 4)', cat: 'kitchen_appliances', icon: 'chair', cuFt: 18.0, w: 0.5, d: 0.5, h: 0.95, floorFootprint: 2.5, color: '#fda4af' },
    { id: 'microwave', name: 'Microwave Oven / OTG', cat: 'kitchen_appliances', icon: 'microwave', cuFt: 3.1, w: 0.55, d: 0.45, h: 0.35, floorFootprint: 0.5, color: '#9f1239' },
    { id: 'gas_stove_cyl', name: 'Gas Stove & Cylinder', cat: 'kitchen_appliances', icon: 'propane_tank', cuFt: 5.5, w: 0.6, d: 0.4, h: 0.65, floorFootprint: 1.5, color: '#be123c' },
    { id: 'water_purifier', name: 'RO Water Purifier', cat: 'kitchen_appliances', icon: 'water_drop', cuFt: 2.3, w: 0.4, d: 0.3, h: 0.55, floorFootprint: 0.5, color: '#06b6d4' },
    { id: 'washing_front', name: 'Front Load Washer', cat: 'kitchen_appliances', icon: 'local_laundry_service', cuFt: 10.8, w: 0.6, d: 0.6, h: 0.85, floorFootprint: 3.8, color: '#8b5cf6' },
    { id: 'washing_top', name: 'Top Load Washer', cat: 'kitchen_appliances', icon: 'local_laundry_service', cuFt: 9.6, w: 0.55, d: 0.55, h: 0.9, floorFootprint: 3.2, color: '#a78bfa' },
    { id: 'split_ac', name: 'Split AC (Indoor & Out)', cat: 'kitchen_appliances', icon: 'mode_fan', cuFt: 6.7, w: 0.9, d: 0.35, h: 0.6, floorFootprint: 1.0, color: '#7c3aed' },
    { id: 'window_ac', name: 'Window AC Unit', cat: 'kitchen_appliances', icon: 'mode_fan', cuFt: 6.7, w: 0.65, d: 0.65, h: 0.45, floorFootprint: 1.8, color: '#6d28d9' },
    { id: 'air_cooler', name: 'Desert Air Cooler', cat: 'kitchen_appliances', icon: 'air', cuFt: 14.5, w: 0.65, d: 0.55, h: 1.15, floorFootprint: 3.5, color: '#c4b5fd' },
    { id: 'inverter_battery', name: 'Inverter & Battery Set', cat: 'kitchen_appliances', icon: 'battery_charging_full', cuFt: 4.4, w: 0.5, d: 0.45, h: 0.55, floorFootprint: 2.0, color: '#4c1d95' },
    { id: 'geyser', name: 'Geyser / Water Heater', cat: 'kitchen_appliances', icon: 'water_heater', cuFt: 4.6, w: 0.45, d: 0.45, h: 0.65, floorFootprint: 0.8, color: '#ec4899' },

    // --- BOXES & OTHER ITEMS ---
    { id: 'box_large', name: 'Large Moving Carton', cat: 'boxes_other', icon: 'inventory_2', cuFt: 4.3, w: 0.6, d: 0.45, h: 0.45, floorFootprint: 0.6, color: '#f59e0b' },
    { id: 'box_medium', name: 'Medium Moving Carton', cat: 'boxes_other', icon: 'inventory_2', cuFt: 2.5, w: 0.45, d: 0.4, h: 0.4, floorFootprint: 0.4, color: '#fbbf24' },
    { id: 'box_small', name: 'Small Moving Carton', cat: 'boxes_other', icon: 'inventory_2', cuFt: 1.1, w: 0.35, d: 0.3, h: 0.3, floorFootprint: 0.2, color: '#fde68a' },
    { id: 'trunk_steel', name: 'Steel Trunk / Sandook', cat: 'boxes_other', icon: 'luggage', cuFt: 8.3, w: 0.95, d: 0.55, h: 0.45, floorFootprint: 4.5, color: '#64748b' },
    { id: 'suitcase_large', name: 'Large Trolley Suitcase', cat: 'boxes_other', icon: 'luggage', cuFt: 4.0, w: 0.75, d: 0.5, h: 0.3, floorFootprint: 0.8, color: '#475569' },
    { id: 'suitcase_cabin', name: 'Cabin Trolley / Duffle', cat: 'boxes_other', icon: 'luggage', cuFt: 1.7, w: 0.55, d: 0.35, h: 0.25, floorFootprint: 0.4, color: '#94a3b8' },
    { id: 'two_wheeler', name: 'Two-Wheeler / Scooter', cat: 'boxes_other', icon: 'two_wheeler', cuFt: 54.0, w: 1.9, d: 0.7, h: 1.15, floorFootprint: 15.0, color: '#dc2626' },
    { id: 'bicycle', name: 'Bicycle (Adult / Kids)', cat: 'boxes_other', icon: 'pedal_bike', cuFt: 36.0, w: 1.7, d: 0.6, h: 1.0, floorFootprint: 7.0, color: '#ea580c' },
    { id: 'office_desk', name: 'Office Workstation / Desk', cat: 'boxes_other', icon: 'desk', cuFt: 19.1, w: 1.2, d: 0.6, h: 0.75, floorFootprint: 4.5, color: '#0891b2' },
    { id: 'office_chair', name: 'Ergonomic Office Chair', cat: 'boxes_other', icon: 'chair', cuFt: 17.2, w: 0.65, d: 0.65, h: 1.15, floorFootprint: 3.5, color: '#0e7490' },
    { id: 'archive_box', name: 'Archival Document Box', cat: 'boxes_other', icon: 'folder', cuFt: 1.3, w: 0.4, d: 0.32, h: 0.28, floorFootprint: 0.25, color: '#ca8a04' },
    { id: 'fitness_gym', name: 'Treadmill / Gym Cycle', cat: 'boxes_other', icon: 'fitness_center', cuFt: 55.1, w: 1.6, d: 0.75, h: 1.3, floorFootprint: 12.0, color: '#16a34a' }
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
    if (matchedUnit.area <= 44) {
      statusText = 'Ideal for personal boxes, luggage, or studio essentials.';
      statusCode = 'good';
    } else if (utilizationPct > 88) {
      statusText = 'Packed near capacity. Consider next size up for easier item retrieval.';
      statusCode = 'tight';
    } else if (utilizationPct > 75) {
      statusText = 'Optimal fit; vertical stacking recommended to preserve walkway.';
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
  // =========================================================================
  // 6. STORAGE ROOM VISUALIZER (3D ISOMETRIC ROOM & 2D ARCHITECTURAL FLOORPLAN)
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
    const height = rect.height || 280;

    if (canvas.width !== width * dpr || canvas.height !== height * dpr) {
      canvas.width = width * dpr;
      canvas.height = height * dpr;
    }

    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, width, height);

    if (!unit || items.length === 0) {
      drawEmptyRoom(ctx, width, height);
      ctx.restore();
      return;
    }

    if (state.angle3D === 'top') {
      draw2DFloorPlan(ctx, width, height, unit, items);
    } else {
      drawIsometricRoom(ctx, width, height, unit, items);
    }

    ctx.restore();
  }

  function drawEmptyRoom(ctx, width, height) {
    ctx.save();
    const cx = width / 2;
    const cy = height / 2;

    ctx.fillStyle = '#f8fafc';
    ctx.fillRect(0, 0, width, height);

    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = '#94a3b8';
    ctx.font = '700 13px "Plus Jakarta Sans", sans-serif';
    ctx.fillText('Storage Room Visualizer', cx, cy - 12);

    ctx.font = '500 12px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Select furniture or a 1-click home preset below to preview room layout', cx, cy + 12);
    ctx.restore();
  }

  function drawIsometricRoom(ctx, width, height, unit, items) {
    const unitW = unit.w || 10;
    const unitD = unit.d || 6;
    const unitH = unit.h || 8;

    const cos30 = Math.cos(Math.PI / 6); // ~0.866
    const sin30 = Math.sin(Math.PI / 6); // 0.5

    const availW = width - 40;
    const availH = height - 40;
    const scale = Math.min(
      availW / ((unitW + unitD) * cos30),
      availH / ((unitW + unitD) * sin30 * 0.55 + unitH * 0.75)
    ) * 0.92;

    const originX = width / 2;
    const originY = height * 0.44;

    function isoProject(x, y, z) {
      const fwdY = unitD - y;
      const isoX = originX + (x - fwdY) * cos30 * scale;
      const isoY = originY + (x + fwdY) * sin30 * scale * 0.55 - z * scale * 0.75;
      return { x: isoX, y: isoY };
    }

    // 1. Back Walls
    const pBack = isoProject(0, unitD, 0);
    const pLeftFront = isoProject(0, 0, 0);
    const pBackTop = isoProject(0, unitD, unitH);
    const pLeftFrontTop = isoProject(0, 0, unitH);

    // Left Partition Wall
    ctx.beginPath();
    ctx.moveTo(pBack.x, pBack.y);
    ctx.lineTo(pLeftFront.x, pLeftFront.y);
    ctx.lineTo(pLeftFrontTop.x, pLeftFrontTop.y);
    ctx.lineTo(pBackTop.x, pBackTop.y);
    ctx.closePath();
    const leftWallGrad = ctx.createLinearGradient(pBack.x, pBackTop.y, pLeftFront.x, pLeftFront.y);
    leftWallGrad.addColorStop(0, '#e2e8f0');
    leftWallGrad.addColorStop(1, '#f1f5f9');
    ctx.fillStyle = leftWallGrad;
    ctx.fill();
    ctx.strokeStyle = '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Left Wall Corrugated Seams
    ctx.strokeStyle = 'rgba(203, 213, 225, 0.4)';
    for (let gy = 1; gy < unitD; gy++) {
      const b0 = isoProject(0, gy, 0);
      const b1 = isoProject(0, gy, unitH);
      ctx.beginPath();
      ctx.moveTo(b0.x, b0.y);
      ctx.lineTo(b1.x, b1.y);
      ctx.stroke();
    }

    // Right Partition Wall
    const pRightFront = isoProject(unitW, unitD, 0);
    const pRightFrontTop = isoProject(unitW, unitD, unitH);

    ctx.beginPath();
    ctx.moveTo(pBack.x, pBack.y);
    ctx.lineTo(pRightFront.x, pRightFront.y);
    ctx.lineTo(pRightFrontTop.x, pRightFrontTop.y);
    ctx.lineTo(pBackTop.x, pBackTop.y);
    ctx.closePath();
    const rightWallGrad = ctx.createLinearGradient(pBack.x, pBackTop.y, pRightFront.x, pRightFront.y);
    rightWallGrad.addColorStop(0, '#cbd5e1');
    rightWallGrad.addColorStop(1, '#e2e8f0');
    ctx.fillStyle = rightWallGrad;
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.stroke();

    // Right Wall Corrugated Seams
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.4)';
    for (let gx = 1; gx < unitW; gx++) {
      const b0 = isoProject(gx, unitD, 0);
      const b1 = isoProject(gx, unitD, unitH);
      ctx.beginPath();
      ctx.moveTo(b0.x, b0.y);
      ctx.lineTo(b1.x, b1.y);
      ctx.stroke();
    }

    // Top Header Beam (SSI Navy + Orange accent)
    ctx.beginPath();
    ctx.moveTo(pLeftFrontTop.x, pLeftFrontTop.y);
    ctx.lineTo(pBackTop.x, pBackTop.y);
    ctx.lineTo(pRightFrontTop.x, pRightFrontTop.y);
    ctx.strokeStyle = '#002B49';
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(pLeftFrontTop.x, pLeftFrontTop.y + 2);
    ctx.lineTo(pBackTop.x, pBackTop.y + 2);
    ctx.lineTo(pRightFrontTop.x, pRightFrontTop.y + 2);
    ctx.strokeStyle = '#FF9600';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // 2. Epoxy Showroom Floor
    const pFrontCenter = isoProject(unitW, 0, 0);
    ctx.beginPath();
    ctx.moveTo(pBack.x, pBack.y);
    ctx.lineTo(pRightFront.x, pRightFront.y);
    ctx.lineTo(pFrontCenter.x, pFrontCenter.y);
    ctx.lineTo(pLeftFront.x, pLeftFront.y);
    ctx.closePath();
    const floorGrad = ctx.createLinearGradient(pBack.x, pBack.y, pFrontCenter.x, pFrontCenter.y);
    floorGrad.addColorStop(0, '#f8fafc');
    floorGrad.addColorStop(1, '#edf2f7');
    ctx.fillStyle = floorGrad;
    ctx.fill();
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.2;
    ctx.stroke();

    // Floor 1ft grid lines
    ctx.strokeStyle = 'rgba(203, 213, 225, 0.5)';
    ctx.lineWidth = 0.8;
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

    // 3. Generate Clean OrganizedBoxes
    const boxes = generateOrganizedBoxes(unitW, unitD, unitH, items);

    // 4. Ground Contact Shadows
    ctx.fillStyle = 'rgba(15, 23, 42, 0.08)';
    boxes.forEach(b => {
      if (b.z === 0) {
        const s0 = isoProject(b.x + 0.08, b.y - 0.08, 0);
        const s1 = isoProject(b.x + b.w + 0.08, b.y - 0.08, 0);
        const s2 = isoProject(b.x + b.w + 0.08, b.y + b.d + 0.08, 0);
        const s3 = isoProject(b.x + 0.08, b.y + b.d + 0.08, 0);
        ctx.beginPath();
        ctx.moveTo(s0.x, s0.y);
        ctx.lineTo(s1.x, s1.y);
        ctx.lineTo(s2.x, s2.y);
        ctx.lineTo(s3.x, s3.y);
        ctx.closePath();
        ctx.fill();
      }
    });

    // 5. Painter's Algorithm Depth-Sorting
    boxes.sort((a, b) => {
      if (Math.abs(b.y - a.y) > 0.05) return b.y - a.y;
      if (Math.abs(a.x - b.x) > 0.05) return a.x - b.x;
      return a.z - b.z;
    });

    // 6. Draw 3D Box Units
    boxes.forEach(b => {
      drawIsoBox(ctx, isoProject, b.x, b.y, b.z, b.w, b.d, b.h, b.color, b.label, b.type);
    });

    // 7. Dimension Tags on Floor Edges (Clean pill badges)
    drawDimensionPill(ctx, isoProject(unitW / 2, 0, 0), `${unitW} ft Width`, 0, 16);
    drawDimensionPill(ctx, isoProject(0, unitD / 2, 0), `${unitD} ft Depth`, -16, 12);
  }

  function drawDimensionPill(ctx, p, text, offsetX, offsetY) {
    ctx.save();
    ctx.font = '700 10px "Plus Jakarta Sans", sans-serif';
    const textWidth = ctx.measureText(text).width;
    const pillW = textWidth + 16;
    const pillH = 18;
    const x = p.x + offsetX - pillW / 2;
    const y = p.y + offsetY - pillH / 2;

    const r = Math.min(pillW, pillH) / 2;
    ctx.roundRect ? ctx.roundRect(x, y, pillW, pillH, r) : ctx.rect(x, y, pillW, pillH);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
    ctx.fill();
    ctx.strokeStyle = '#cbd5e1';
    ctx.lineWidth = 1;
    ctx.stroke();

    ctx.fillStyle = '#0f172a';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, x + pillW / 2, y + pillH / 2);
    ctx.restore();
  }

  function draw2DFloorPlan(ctx, width, height, unit, items) {
    const unitW = unit.w || 10;
    const unitD = unit.d || 6;

    const pad = 36;
    const availW = width - pad * 2;
    const availH = height - pad * 2;
    const scale = Math.min(availW / unitW, availH / unitD);

    const planW = unitW * scale;
    const planH = unitD * scale;
    const startX = (width - planW) / 2;
    const startY = (height - planH) / 2;

    // Background Room Area
    ctx.fillStyle = '#f8fafc';
    ctx.fillRect(startX, startY, planW, planH);

    // 1ft grid
    ctx.strokeStyle = 'rgba(203, 213, 225, 0.4)';
    ctx.lineWidth = 0.8;
    for (let x = 1; x < unitW; x++) {
      ctx.beginPath();
      ctx.moveTo(startX + x * scale, startY);
      ctx.lineTo(startX + x * scale, startY + planH);
      ctx.stroke();
    }
    for (let y = 1; y < unitD; y++) {
      ctx.beginPath();
      ctx.moveTo(startX, startY + y * scale);
      ctx.lineTo(startX + planW, startY + y * scale);
      ctx.stroke();
    }

    // Access Walkway Corridor
    const aisleW = Math.min(1.8, unitW * 0.22) * scale;
    const aisleX = startX + planW / 2 - aisleW / 2;
    ctx.fillStyle = 'rgba(16, 185, 129, 0.1)';
    ctx.fillRect(aisleX, startY, aisleW, planH);
    ctx.strokeStyle = 'rgba(16, 185, 129, 0.4)';
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.strokeRect(aisleX, startY, aisleW, planH);
    ctx.setLineDash([]);

    ctx.fillStyle = '#059669';
    ctx.font = '700 9px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('ACCESS AISLE', aisleX + aisleW / 2, startY + planH / 2);

    // Packed 2D Footprints
    const boxes = generateOrganizedBoxes(unitW, unitD, 8, items);
    boxes.forEach(b => {
      const bx = startX + b.x * scale;
      const by = startY + (unitD - b.y - b.d) * scale;
      const bw = b.w * scale;
      const bh = b.d * scale;

      ctx.fillStyle = b.color;
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = 'rgba(0, 0, 0, 0.15)';
      ctx.lineWidth = 1;
      ctx.strokeRect(bx, by, bw, bh);

      if (bw > 24 && bh > 14) {
        ctx.fillStyle = '#ffffff';
        ctx.font = '700 8.5px "Plus Jakarta Sans", sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(b.label || '', bx + bw / 2, by + bh / 2);
      }
    });

    // Outer Room Walls
    ctx.strokeStyle = '#002B49';
    ctx.lineWidth = 4;
    ctx.strokeRect(startX, startY, planW, planH);

    // Roll-up Shutter Entrance (Front wall)
    const doorW = planW * 0.55;
    const doorX = startX + (planW - doorW) / 2;
    ctx.strokeStyle = '#FF9600';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(doorX, startY + planH);
    ctx.lineTo(doorX + doorW, startY + planH);
    ctx.stroke();

    ctx.fillStyle = '#FF9600';
    ctx.font = '700 9px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('▲ PRIVATE SHUTTER ENTRANCE', startX + planW / 2, startY + planH + 16);

    // Dimension labels
    ctx.fillStyle = '#0f172a';
    ctx.font = '700 11px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(`${unitW} ft Width`, startX + planW / 2, startY - 10);

    ctx.save();
    ctx.translate(startX - 12, startY + planH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText(`${unitD} ft Depth`, 0, 0);
    ctx.restore();
  }

  function generateOrganizedBoxes(unitW, unitD, unitH, items) {
    const boxes = [];
    const furniture = [];
    const appliances = [];
    const boxesAndLuggage = [];

    items.forEach(it => {
      const qty = it.qty || 1;
      for (let i = 0; i < qty; i++) {
        const id = it.id.toLowerCase();
        if (it.cat === 'bedroom' || it.cat === 'living' || id.includes('sofa') || id.includes('bed') || id.includes('table') || id.includes('almirah') || id.includes('desk') || id.includes('chair') || id.includes('diwan') || id.includes('mandir')) {
          furniture.push(it);
        } else if (id.includes('fridge') || id.includes('washing') || id.includes('ac') || id.includes('cooler') || id.includes('geyser') || id.includes('inverter') || id.includes('purifier') || id.includes('microwave') || id.includes('stove')) {
          appliances.push(it);
        } else {
          boxesAndLuggage.push(it);
        }
      }
    });

    const minX = 0.4;
    const maxX = unitW - 0.4;
    const minY = 0.4;
    const maxY = unitD - 0.4;

    // 1. Pack Back Wall Furniture (large vertical pieces)
    let curBackX = minX;
    furniture.forEach((f, idx) => {
      const isLarge = f.id.includes('bed') || f.id.includes('almirah') || f.id.includes('sofa') || f.id.includes('table');
      const w = isLarge ? 2.8 : 1.8;
      const d = 1.3;
      const h = isLarge ? Math.min(unitH - 0.8, 4.6) : Math.min(unitH - 1, 3.2);

      if (curBackX + w <= maxX) {
        boxes.push({
          x: curBackX,
          y: maxY - d,
          z: 0,
          w: w,
          d: d,
          h: h,
          color: f.id.includes('bed') ? '#1e3a8a' : (f.id.includes('sofa') ? '#2563eb' : (f.id.includes('almirah') ? '#0f766e' : '#334155')),
          label: f.name.replace(/\(.*?\)/g, '').split('/')[0].trim().split(' ')[0],
          type: 'furniture'
        });
        curBackX += w + 0.25;
      } else {
        const sideW = 1.4;
        const sideD = 2.4;
        const sideH = Math.min(unitH - 1, 3.2);
        const slotY = minY + ((idx % 3) * (sideD + 0.3));
        if (slotY + sideD <= maxY - 1.2) {
          boxes.push({
            x: minX,
            y: slotY,
            z: 0,
            w: sideW,
            d: sideD,
            h: sideH,
            color: '#3b82f6',
            label: f.name.replace(/\(.*?\)/g, '').split('/')[0].trim().split(' ')[0],
            type: 'furniture'
          });
        }
      }
    });

    // 2. Pack Appliances (clean grouping on right side)
    let appIdx = 0;
    appliances.forEach((app) => {
      const w = 1.7;
      const d = 1.6;
      const h = Math.min(unitH - 0.8, app.id.includes('fridge') ? 4.8 : 3.0);
      const placeX = maxX - w;
      const placeY = Math.max(minY, (maxY - 1.6) - (appIdx * (d + 0.3)));
      if (placeY >= minY && placeX > minX + 1.8) {
        boxes.push({
          x: placeX,
          y: placeY,
          z: 0,
          w: w,
          d: d,
          h: h,
          color: app.id.includes('fridge') ? '#64748b' : (app.id.includes('washing') ? '#475569' : '#94a3b8'),
          label: app.name.split(' ')[0],
          type: 'appliance'
        });
        appIdx++;
      }
    });

    // 3. Pack Boxes & Luggage in tidy pallet stacks
    const boxW = 1.35;
    const boxD = 1.25;
    const boxH = 1.15;
    const maxStackHeight = 3;
    let bIdx = 0;
    const startBoxX = minX + 1.8;
    const startBoxY = minY + 0.4;

    boxesAndLuggage.forEach((b) => {
      const colX = startBoxX + (Math.floor(bIdx / (maxStackHeight * 2)) * (boxW + 0.2));
      const colY = startBoxY + ((Math.floor(bIdx / maxStackHeight) % 2) * (boxD + 0.2));
      const colZ = (bIdx % maxStackHeight) * boxH;

      if (colX + boxW <= maxX - 1.5 && colY + boxD <= maxY - 1.2 && colZ + boxH <= unitH) {
        boxes.push({
          x: colX,
          y: colY,
          z: colZ,
          w: boxW,
          d: boxD,
          h: boxH,
          color: b.id.includes('trunk') ? '#64748b' : (b.id.includes('suitcase') ? '#0284c7' : '#d97706'),
          label: b.id.includes('box') ? 'Box' : (b.id.includes('trunk') ? 'Trunk' : 'Luggage'),
          type: 'box'
        });
        bIdx++;
      }
    });

    return boxes;
  }

  function drawIsoBox(ctx, isoProject, x, y, z, w, d, h, color, label, type) {
    const p0 = isoProject(x, y, z);
    const p1 = isoProject(x + w, y, z);
    const p2 = isoProject(x + w, y + d, z);
    const p3 = isoProject(x, y + d, z);

    const t0 = isoProject(x, y, z + h);
    const t1 = isoProject(x + w, y, z + h);
    const t2 = isoProject(x + w, y + d, z + h);
    const t3 = isoProject(x, y + d, z + h);

    // 1. Top Face (Overhead LED highlight)
    ctx.beginPath();
    ctx.moveTo(t0.x, t0.y);
    ctx.lineTo(t1.x, t1.y);
    ctx.lineTo(t2.x, t2.y);
    ctx.lineTo(t3.x, t3.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, 24);
    ctx.fill();
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.12)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Box tape band for moving cartons
    if (type === 'box') {
      const midT0_1 = { x: (t0.x + t1.x) / 2, y: (t0.y + t1.y) / 2 };
      const midT2_3 = { x: (t2.x + t3.x) / 2, y: (t2.y + t3.y) / 2 };
      ctx.beginPath();
      ctx.moveTo(midT0_1.x, midT0_1.y);
      ctx.lineTo(midT2_3.x, midT2_3.y);
      ctx.strokeStyle = '#92400e';
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Label on Top Face
    if (label && Math.abs(t1.x - t0.x) > 28) {
      const centerT = { x: (t0.x + t2.x) / 2, y: (t0.y + t2.y) / 2 };
      ctx.fillStyle = '#ffffff';
      ctx.font = '700 8.5px "Plus Jakarta Sans", sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(label, centerT.x, centerT.y);
    }

    // 2. Front Face (facing forward)
    ctx.beginPath();
    ctx.moveTo(p0.x, p0.y);
    ctx.lineTo(p1.x, p1.y);
    ctx.lineTo(t1.x, t1.y);
    ctx.lineTo(t0.x, t0.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, -8);
    ctx.fill();
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.12)';
    ctx.stroke();

    // 3. Side Face (facing left)
    ctx.beginPath();
    ctx.moveTo(p0.x, p0.y);
    ctx.lineTo(p3.x, p3.y);
    ctx.lineTo(t3.x, t3.y);
    ctx.lineTo(t0.x, t0.y);
    ctx.closePath();
    ctx.fillStyle = shadeColor(color, 6);
    ctx.fill();
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.12)';
    ctx.stroke();
  }

  function shadeColor(color, percent) {
    let R = parseInt(color.substring(1, 3), 16);
    let G = parseInt(color.substring(3, 5), 16);
    let B = parseInt(color.substring(5, 7), 16);

    R = parseInt((R * (100 + percent)) / 100);
    G = parseInt((G * (100 + percent)) / 100);
    B = parseInt((B * (100 + percent)) / 100);

    R = Math.min(255, Math.max(0, R));
    G = Math.min(255, Math.max(0, G));
    B = Math.min(255, Math.max(0, B));

    const RR = R.toString(16).padStart(2, '0');
    const GG = G.toString(16).padStart(2, '0');
    const BB = B.toString(16).padStart(2, '0');

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
      if (unitVolEl) unitVolEl.innerText = `${result.unit.vol} cu ft room (${Math.round(totalCuFt)} cu ft goods)`;
      if (unitPriceEl) unitPriceEl.innerText = 'Flexible monthly rental · Zero lock-ins';
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
      if (tierBadgeEl) tierBadgeEl.innerText = 'Select Items';
      if (unitNameEl) unitNameEl.innerText = 'Select Items or Preset';
      if (unitDimEl) unitDimEl.innerText = 'Facility units available from 24 to 187+ sq ft';
      if (unitAreaEl) unitAreaEl.innerText = '0 sq ft';
      if (unitVolEl) unitVolEl.innerText = '0 cu ft';
      if (unitPriceEl) unitPriceEl.innerText = 'Flexible monthly rental · Zero lock-ins';
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
        if (mobileSqFt) mobileSqFt.innerText = `${result.unit.area} sq ft · ${result.unit.tier}`;
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

    reset: function () {
      this.resetAll();
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
      if (subHeadingEl) subHeadingEl.textContent = `Unit sized for your ${totalItems} items. Zero obligation quotation.`;
    },

    toggleViewMode: function (mode, btn) {
      if (mode) state.angle3D = mode;
      if (btn) {
        document.querySelectorAll('.calc-view-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }
      renderAll();
    }
  };

  // Global aliases for legacy/inline button triggers
  window.handleCalculatorQuote = window.SSI_CALCULATOR.handleQuote;
  window.applyCalcPreset = window.SSI_CALCULATOR.applyPreset;
  window.filterCalcCategory = window.SSI_CALCULATOR.filterCategory;
  window.updateItemQty = window.SSI_CALCULATOR.updateQty;

  // =========================================================================
  // 9. DOM INITIALIZATION
  // =========================================================================
  function initCalculator() {
    const gridEl = document.getElementById('calc-items-grid-container');
    if (gridEl && (!gridEl.children || gridEl.children.length === 0)) {
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCalculator);
  } else {
    initCalculator();
  }

})();
