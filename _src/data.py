"""
=====================================================================
  JANTA — STORE SETTINGS & PRODUCT CATALOGUE
  Edit this file, then run:  python3 _src/build.py
=====================================================================
"""

# ------------------------------------------------------------------ store info
STORE = {
    "name": "Janta",
    "tagline": "Phones & Watches",
    "domain": "https://www.janta.com.np",           # your live website address (no trailing slash)
    "whatsapp": "9779702001382",                    # country code + number, digits only
    "whatsapp_display": "+977 970-2001382",
    "phone_display": "+977 980-0000000",
    "phone_tel": "+9779800000000",
    "email": "info@janta.com.np",
    "street": "New Road",
    "city": "Kathmandu",
    "postcode": "44600",
    "region": "Bagmati Province",
    "country": "Nepal",
    "country_code": "NP",
    "map_query": "New Road, Kathmandu, Nepal",      # what Google Maps should show
    "geo": (27.7041, 85.3107),
    "hours": [
        ("Sunday – Friday", "10:00 AM – 8:00 PM"),
        ("Saturday", "11:00 AM – 6:00 PM"),
    ],
    "hours_schema": ["Su-Fr 10:00-20:00", "Sa 11:00-18:00"],
    "socials": {
        "facebook": "https://facebook.com/",
        "instagram": "https://instagram.com/",
        "tiktok": "https://tiktok.com/",
        "youtube": "https://youtube.com/",
    },
    "currency": "NPR",
}

# ------------------------------------------------------------------ filters
PHONE_BRANDS = [("apple", "Apple"), ("samsung", "Samsung"), ("xiaomi", "Xiaomi"), ("oneplus", "OnePlus"),
                ("vivo", "Vivo"), ("oppo", "Oppo"), ("realme", "Realme")]
WATCH_BRANDS = [("apple-watch", "Apple Watch"), ("galaxy-watch", "Samsung Galaxy Watch"), ("huawei", "Huawei"),
                ("amazfit", "Amazfit"), ("noise", "Noise"), ("boat", "Boat")]
ACCESSORY_TYPES = [("chargers", "Chargers"), ("earphones", "Earphones"), ("cases", "Cases"),
                   ("power-banks", "Power Banks"), ("screen-protectors", "Screen Protectors")]

# ------------------------------------------------------------------ products
# cat: phones | watches | accessories      key: filter key from the lists above
# img: drawing settings for the built-in product illustration (or set "photo": "assets/img/products/xyz.webp")
P = []


def add(**kw):
    kw.setdefault("old_price", None)
    kw.setdefault("badge", None)
    kw.setdefault("featured", False)
    P.append(kw)


# ---------------- Phones
add(slug="iphone-17-pro-max", name="iPhone 17 Pro Max", brand="Apple", cat="phones", key="apple",
    price=219900, old_price=229900, badge="New", featured=True,
    short="6.9\" Super Retina XDR, A19 Pro chip and a pro-grade triple 48MP camera system.",
    desc="Apple's most powerful iPhone yet. A huge 6.9-inch ProMotion display, the blazing A19 Pro chip, all-day battery life and a triple 48MP Fusion camera system for stunning photos and 4K video. Official warranty and genuine accessories included.",
    specs=[("Display", "6.9\" OLED, 120Hz"), ("Chip", "A19 Pro"), ("Storage", "256GB"), ("Camera", "48MP + 48MP + 48MP"), ("Battery", "All-day, MagSafe")],
    img={"type": "phone", "body": "#c8742f", "accent": "#ff8a3d", "cam": "pro"})
add(slug="iphone-16", name="iPhone 16", brand="Apple", cat="phones", key="apple",
    price=124900, old_price=134900, badge="Sale",
    short="6.1\" display, A18 chip, Camera Control and a 48MP Fusion camera.",
    desc="The iPhone 16 brings the A18 chip, the new Camera Control button and a brilliant 48MP Fusion camera in a durable, colour-infused glass design. Fast, smooth and built to last.",
    specs=[("Display", "6.1\" OLED"), ("Chip", "A18"), ("Storage", "128GB"), ("Camera", "48MP + 12MP"), ("Battery", "Up to 22h video")],
    img={"type": "phone", "body": "#6b8fd6", "accent": "#3b5bdb", "cam": "duo"})
add(slug="samsung-galaxy-s25-ultra", name="Galaxy S25 Ultra", brand="Samsung", cat="phones", key="samsung",
    price=184999, badge="Hot", featured=True,
    short="200MP camera, built-in S Pen, Snapdragon 8 Elite and Galaxy AI.",
    desc="The ultimate Galaxy. A titanium frame, a 6.9-inch Dynamic AMOLED 2X display, a 200MP pro-grade camera with 100x Space Zoom and the built-in S Pen, all powered by Snapdragon 8 Elite for Galaxy and Galaxy AI.",
    specs=[("Display", "6.9\" AMOLED, 120Hz"), ("Processor", "Snapdragon 8 Elite"), ("RAM / Storage", "12GB / 256GB"), ("Camera", "200MP Quad"), ("Battery", "5000mAh, 45W")],
    img={"type": "phone", "body": "#4a5466", "accent": "#5b7cfa", "cam": "vertical"})
add(slug="samsung-galaxy-a56", name="Galaxy A56 5G", brand="Samsung", cat="phones", key="samsung",
    price=54999,
    short="6.7\" Super AMOLED, 50MP OIS camera and 6 years of updates.",
    desc="Awesome made easy. The Galaxy A56 5G pairs a bright 6.7-inch Super AMOLED display with a 50MP OIS camera, IP67 water resistance, 45W fast charging and six generations of Android upgrades.",
    specs=[("Display", "6.7\" Super AMOLED"), ("Processor", "Exynos 1580"), ("RAM / Storage", "8GB / 256GB"), ("Camera", "50MP Triple"), ("Battery", "5000mAh, 45W")],
    img={"type": "phone", "body": "#9fb7a8", "accent": "#38b2ac", "cam": "vertical"})
add(slug="xiaomi-15", name="Xiaomi 15", brand="Xiaomi", cat="phones", key="xiaomi",
    price=109999, featured=True,
    short="Leica optics, Snapdragon 8 Elite and a compact 6.36\" display.",
    desc="Compact flagship power. Xiaomi 15 combines Leica Summilux optics with a 50MP triple camera, the Snapdragon 8 Elite chip and a 5400mAh battery with 90W HyperCharge in a pocket-friendly size.",
    specs=[("Display", "6.36\" AMOLED, 120Hz"), ("Processor", "Snapdragon 8 Elite"), ("RAM / Storage", "12GB / 512GB"), ("Camera", "50MP Leica Triple"), ("Battery", "5400mAh, 90W")],
    img={"type": "phone", "body": "#e8e9ec", "accent": "#2f6bff", "cam": "square"})
add(slug="redmi-note-14-pro-plus", name="Redmi Note 14 Pro+ 5G", brand="Xiaomi", cat="phones", key="xiaomi",
    price=49999, old_price=54999, badge="Sale",
    short="200MP camera, 120W HyperCharge and IP68 protection.",
    desc="Flagship features at a mid-range price. A 200MP main camera, a curved 1.5K AMOLED display, IP68 dust and water resistance and 120W HyperCharge that fills the battery in minutes.",
    specs=[("Display", "6.67\" 1.5K AMOLED"), ("Processor", "Snapdragon 7s Gen 3"), ("RAM / Storage", "8GB / 256GB"), ("Camera", "200MP Triple"), ("Battery", "5110mAh, 120W")],
    img={"type": "phone", "body": "#7c5cbf", "accent": "#9f7aea", "cam": "circle"})
add(slug="oneplus-13", name="OnePlus 13", brand="OnePlus", cat="phones", key="oneplus",
    price=119999, badge="New", featured=True,
    short="Hasselblad camera, Snapdragon 8 Elite and a 6000mAh battery.",
    desc="Smooth beyond belief. OnePlus 13 features a Hasselblad-tuned triple 50MP camera, the Snapdragon 8 Elite, a stunning 2K ProXDR display and a massive 6000mAh battery with 100W SUPERVOOC charging.",
    specs=[("Display", "6.82\" 2K AMOLED, 120Hz"), ("Processor", "Snapdragon 8 Elite"), ("RAM / Storage", "12GB / 256GB"), ("Camera", "50MP Hasselblad Triple"), ("Battery", "6000mAh, 100W")],
    img={"type": "phone", "body": "#1f3b73", "accent": "#e53e3e", "cam": "circle"})
add(slug="oneplus-nord-ce4", name="OnePlus Nord CE4 5G", brand="OnePlus", cat="phones", key="oneplus",
    price=39999,
    short="Snapdragon 7 Gen 3, 100W SUPERVOOC and a 120Hz AMOLED display.",
    desc="Fast, fluid and dependable. The Nord CE4 delivers a 120Hz AMOLED display, Snapdragon 7 Gen 3 performance, a 50MP Sony camera with OIS and 100W SUPERVOOC charging.",
    specs=[("Display", "6.7\" AMOLED, 120Hz"), ("Processor", "Snapdragon 7 Gen 3"), ("RAM / Storage", "8GB / 128GB"), ("Camera", "50MP + 8MP"), ("Battery", "5500mAh, 100W")],
    img={"type": "phone", "body": "#3c6e5a", "accent": "#48bb78", "cam": "rect"})
add(slug="vivo-v50", name="Vivo V50 5G", brand="Vivo", cat="phones", key="vivo",
    price=64999,
    short="ZEISS portrait cameras, slim curved design and 6000mAh battery.",
    desc="Portraits that shine. The Vivo V50 brings ZEISS-engineered 50MP front and rear cameras with Aura Light, a slim quad-curved display and a huge 6000mAh battery with 90W FlashCharge.",
    specs=[("Display", "6.77\" AMOLED, 120Hz"), ("Processor", "Snapdragon 7 Gen 3"), ("RAM / Storage", "8GB / 256GB"), ("Camera", "50MP ZEISS Dual"), ("Battery", "6000mAh, 90W")],
    img={"type": "phone", "body": "#d9a5b3", "accent": "#ed64a6", "cam": "rect"})
add(slug="vivo-y29", name="Vivo Y29", brand="Vivo", cat="phones", key="vivo",
    price=24999,
    short="Big 6.68\" display, 5500mAh battery and military-grade durability.",
    desc="Built tough for every day. The Vivo Y29 offers a large 90Hz display, a long-lasting 5500mAh battery with 44W charging, IP64 protection and SGS drop resistance at a friendly price.",
    specs=[("Display", "6.68\" LCD, 90Hz"), ("Processor", "Dimensity 6300"), ("RAM / Storage", "6GB / 128GB"), ("Camera", "50MP AI Dual"), ("Battery", "5500mAh, 44W")],
    img={"type": "phone", "body": "#2b4d8c", "accent": "#4299e1", "cam": "circle"})
add(slug="oppo-reno13", name="Oppo Reno13 5G", brand="Oppo", cat="phones", key="oppo",
    price=69999, badge="New",
    short="AI Livephoto, IP69 waterproof and a sleek aerospace-grade frame.",
    desc="Designed to impress. Oppo Reno13 5G features a 50MP AI camera with underwater photography, IP66/68/69 protection, an aerospace-grade aluminium frame and 80W SUPERVOOC charging.",
    specs=[("Display", "6.59\" AMOLED, 120Hz"), ("Processor", "Dimensity 8350"), ("RAM / Storage", "12GB / 256GB"), ("Camera", "50MP + 8MP + 2MP"), ("Battery", "5600mAh, 80W")],
    img={"type": "phone", "body": "#b9c6e8", "accent": "#667eea", "cam": "rect"})
add(slug="oppo-a3x", name="Oppo A3x", brand="Oppo", cat="phones", key="oppo",
    price=17999,
    short="Durable everyday phone with 120Hz display and 45W SUPERVOOC.",
    desc="Reliable and affordable. The Oppo A3x has a smooth 120Hz display, military-grade shock resistance, IP54 splash protection and 45W SUPERVOOC fast charging.",
    specs=[("Display", "6.67\" LCD, 120Hz"), ("Processor", "Snapdragon 6s Gen 1"), ("RAM / Storage", "4GB / 128GB"), ("Camera", "8MP"), ("Battery", "5100mAh, 45W")],
    img={"type": "phone", "body": "#c53030", "accent": "#fc8181", "cam": "rect"})
add(slug="realme-14-pro-plus", name="Realme 14 Pro+ 5G", brand="Realme", cat="phones", key="realme",
    price=56999, featured=True,
    short="Periscope telephoto, colour-changing design and 80W charging.",
    desc="Shoot like a pro. Realme 14 Pro+ packs a 50MP Sony main camera with a 3x periscope telephoto lens, a quad-curved 120Hz display and a 6000mAh battery with 80W charging.",
    specs=[("Display", "6.83\" AMOLED, 120Hz"), ("Processor", "Snapdragon 7s Gen 3"), ("RAM / Storage", "8GB / 256GB"), ("Camera", "50MP Periscope Triple"), ("Battery", "6000mAh, 80W")],
    img={"type": "phone", "body": "#e2e8f0", "accent": "#319795", "cam": "circle"})
add(slug="realme-c75", name="Realme C75", brand="Realme", cat="phones", key="realme",
    price=21999,
    short="IP69 water resistance, 6000mAh battery and 45W fast charge.",
    desc="Tough and long-lasting. The Realme C75 offers IP68/IP69 protection, a 6000mAh battery with 45W charging, a 50MP AI camera and a smooth 90Hz display.",
    specs=[("Display", "6.72\" LCD, 90Hz"), ("Processor", "Helio G92 Max"), ("RAM / Storage", "8GB / 128GB"), ("Camera", "50MP AI"), ("Battery", "6000mAh, 45W")],
    img={"type": "phone", "body": "#d69e2e", "accent": "#ecc94b", "cam": "square"})

# ---------------- Watches
add(slug="apple-watch-series-11", name="Apple Watch Series 11", brand="Apple", cat="watches", key="apple-watch",
    price=64900, badge="New", featured=True,
    short="Thinnest Apple Watch with advanced health sensors and all-day battery.",
    desc="Your essential health companion. Apple Watch Series 11 brings a bright, wide-angle OLED display, advanced heart and sleep insights, crash detection, workout tracking and all-day battery life.",
    specs=[("Case", "42mm / 46mm Aluminium"), ("Display", "Always-On Retina"), ("Health", "ECG, SpO2, Sleep"), ("Water", "WR50"), ("Battery", "Up to 24h")],
    img={"type": "watch", "case": "#c9ced8", "strap": "#1a3c7a", "accent": "#2f6bff", "shape": "square"})
add(slug="apple-watch-ultra-3", name="Apple Watch Ultra 3", brand="Apple", cat="watches", key="apple-watch",
    price=129900,
    short="Rugged titanium case, precision GPS and up to 42 hours of battery.",
    desc="Built for adventure. Apple Watch Ultra 3 features a 49mm titanium case, the brightest Apple display ever, dual-frequency GPS, a depth gauge for diving and up to 42 hours of battery life.",
    specs=[("Case", "49mm Titanium"), ("Display", "Always-On Retina, 3000 nits"), ("GPS", "Dual-frequency"), ("Water", "WR100, EN13319"), ("Battery", "Up to 42h")],
    img={"type": "watch", "case": "#8a8f98", "strap": "#e86b2c", "accent": "#ff8a3d", "shape": "square"})
add(slug="samsung-galaxy-watch8", name="Galaxy Watch8", brand="Samsung", cat="watches", key="galaxy-watch",
    price=44999, featured=True,
    short="Slim cushion design, Antioxidant Index and Gemini on your wrist.",
    desc="Wellness made smarter. Galaxy Watch8 offers advanced sleep coaching, the new Antioxidant Index, running coach, Gemini voice assistant and a brighter Super AMOLED display in a slimmer design.",
    specs=[("Case", "40mm / 44mm Armor Aluminium"), ("Display", "Super AMOLED, 3000 nits"), ("Health", "BIA, ECG, Sleep"), ("Water", "5ATM + IP68"), ("Battery", "Up to 40h")],
    img={"type": "watch", "case": "#3b4253", "strap": "#2d3748", "accent": "#5b7cfa", "shape": "round"})
add(slug="samsung-galaxy-watch8-classic", name="Galaxy Watch8 Classic", brand="Samsung", cat="watches", key="galaxy-watch",
    price=59999,
    short="Iconic rotating bezel, premium stainless steel and leather strap.",
    desc="Timeless meets smart. The Galaxy Watch8 Classic brings back the rotating bezel with a premium stainless steel case, Quick Button, advanced health tracking and up to 40 hours of battery.",
    specs=[("Case", "46mm Stainless Steel"), ("Display", "Super AMOLED"), ("Bezel", "Rotating"), ("Water", "5ATM + IP68"), ("Battery", "Up to 40h")],
    img={"type": "watch", "case": "#b7bcc6", "strap": "#5a3825", "accent": "#2f6bff", "shape": "round", "sport": False})
add(slug="huawei-watch-gt-5-pro", name="Huawei Watch GT 5 Pro", brand="Huawei", cat="watches", key="huawei",
    price=49999, badge="Hot",
    short="Titanium design, TruSense health system and 14-day battery.",
    desc="Pro looks, pro tracking. Huawei Watch GT 5 Pro has an aerospace titanium case, sapphire glass, the TruSense health system, professional golf and dive modes, and up to 14 days of battery life.",
    specs=[("Case", "46mm Titanium"), ("Display", "1.43\" AMOLED"), ("Glass", "Sapphire"), ("Water", "5ATM, 40m diving"), ("Battery", "Up to 14 days")],
    img={"type": "watch", "case": "#9aa1ad", "strap": "#2b2b2b", "accent": "#f6ad55", "shape": "round"})
add(slug="huawei-watch-fit-4", name="Huawei Watch Fit 4", brand="Huawei", cat="watches", key="huawei",
    price=19999,
    short="Ultra-slim aluminium body, built-in GPS and 10-day battery.",
    desc="Fitness in style. Huawei Watch Fit 4 features a vivid 1.82-inch AMOLED screen, 100+ workout modes, built-in dual-band GPS, health monitoring and up to 10 days of battery in an ultra-thin body.",
    specs=[("Display", "1.82\" AMOLED"), ("GPS", "Dual-band built-in"), ("Workouts", "100+ modes"), ("Water", "5ATM"), ("Battery", "Up to 10 days")],
    img={"type": "watch", "case": "#d5dae2", "strap": "#7f9cf5", "accent": "#5a67d8", "shape": "square"})
add(slug="amazfit-active-2", name="Amazfit Active 2", brand="Amazfit", cat="watches", key="amazfit",
    price=16999, featured=True,
    short="Premium round design, offline maps and 10-day battery life.",
    desc="Stylish, smart and great value. Amazfit Active 2 offers a bright AMOLED display, free offline maps, 160+ sports modes, BioCharge readiness score and up to 10 days of battery.",
    specs=[("Display", "1.32\" AMOLED"), ("Maps", "Free offline maps"), ("Sports", "160+ modes"), ("Water", "5ATM"), ("Battery", "Up to 10 days")],
    img={"type": "watch", "case": "#2d3748", "strap": "#1a202c", "accent": "#48bb78", "shape": "round"})
add(slug="amazfit-gts-4", name="Amazfit GTS 4", brand="Amazfit", cat="watches", key="amazfit",
    price=14999, old_price=17999, badge="Sale",
    short="Sleek square AMOLED, accurate GPS and Bluetooth calling.",
    desc="Ultra-thin and feature-packed. Amazfit GTS 4 delivers a 1.75-inch HD AMOLED display, industry-leading dual-band GPS, Bluetooth calling, 150+ sports modes and Alexa built in.",
    specs=[("Display", "1.75\" AMOLED"), ("GPS", "Dual-band"), ("Calling", "Bluetooth"), ("Water", "5ATM"), ("Battery", "Up to 8 days")],
    img={"type": "watch", "case": "#e2c9a6", "strap": "#f7f3ee", "accent": "#d69e2e", "shape": "square"})
add(slug="noisefit-halo-2", name="NoiseFit Halo 2", brand="Noise", cat="watches", key="noise",
    price=7999,
    short="Premium metal build, AMOLED display and Bluetooth calling.",
    desc="Luxury looks for less. NoiseFit Halo 2 features a 1.43-inch AMOLED always-on display, a premium metallic build, Bluetooth calling, 100+ sports modes and up to 7 days of battery.",
    specs=[("Display", "1.43\" AMOLED"), ("Calling", "Bluetooth"), ("Sports", "100+ modes"), ("Water", "IP68"), ("Battery", "Up to 7 days")],
    img={"type": "watch", "case": "#a0aec0", "strap": "#4a5568", "accent": "#ed8936", "shape": "round", "sport": False})
add(slug="noise-colorfit-pro-6", name="Noise ColorFit Pro 6", brand="Noise", cat="watches", key="noise",
    price=9999,
    short="AI-powered smartwatch with 1.96\" AMOLED and Noise Health Suite.",
    desc="Smart, simple, stylish. ColorFit Pro 6 brings a large 1.96-inch AMOLED display, AI companion features, Noise Health Suite, Bluetooth calling and a sleek metal finish.",
    specs=[("Display", "1.96\" AMOLED"), ("Calling", "Bluetooth"), ("Health", "HR, SpO2, Sleep"), ("Water", "IP68"), ("Battery", "Up to 7 days")],
    img={"type": "watch", "case": "#1a202c", "strap": "#2c5282", "accent": "#4299e1", "shape": "square"})
add(slug="boat-wave-sigma-3", name="boAt Wave Sigma 3", brand="boAt", cat="watches", key="boat",
    price=4499, badge="Hot",
    short="Big 2.01\" display, Bluetooth calling and 700+ active modes.",
    desc="Big screen, small price. boAt Wave Sigma 3 features a 2.01-inch HD display, Bluetooth calling with dial pad, Crest app health ecosystem, 700+ active modes and up to 7 days of battery.",
    specs=[("Display", "2.01\" HD"), ("Calling", "Bluetooth, Dial pad"), ("Modes", "700+ active"), ("Water", "IP67"), ("Battery", "Up to 7 days")],
    img={"type": "watch", "case": "#2d3748", "strap": "#e53e3e", "accent": "#fc8181", "shape": "square"})
add(slug="boat-lunar-discovery", name="boAt Lunar Discovery", brand="boAt", cat="watches", key="boat",
    price=5499,
    short="Round 1.39\" HD display, functional crown and BT calling.",
    desc="Classic round style with smart features. boAt Lunar Discovery has a 1.39-inch HD display, a functional crown, Bluetooth calling, heart-rate and SpO2 monitoring and 100+ sports modes.",
    specs=[("Display", "1.39\" HD"), ("Calling", "Bluetooth"), ("Health", "HR, SpO2"), ("Water", "IP68"), ("Battery", "Up to 7 days")],
    img={"type": "watch", "case": "#4a5568", "strap": "#1a365d", "accent": "#63b3ed", "shape": "round"})

# ---------------- Accessories
add(slug="apple-20w-usb-c-power-adapter", name="Apple 20W USB-C Power Adapter", brand="Apple", cat="accessories", key="chargers",
    price=3200,
    short="Original fast charger for iPhone, iPad and AirPods.",
    desc="Genuine Apple 20W USB-C Power Adapter for fast, efficient charging at home, in the office or on the go. Charges iPhone up to 50% in around 30 minutes.",
    specs=[("Output", "20W USB-C PD"), ("Compatible", "iPhone, iPad, AirPods"), ("Cable", "Sold separately"), ("Warranty", "1 Year")],
    img={"type": "charger", "color": "#f4f6fa", "cable": "#ffffff"})
add(slug="samsung-25w-super-fast-charger", name="Samsung 25W Super Fast Charger", brand="Samsung", cat="accessories", key="chargers",
    price=2499, featured=True,
    short="Super Fast Charging adapter with USB-C to C cable included.",
    desc="Original Samsung 25W travel adapter with Super Fast Charging and a USB-C to USB-C cable. Safe, efficient and compatible with Galaxy phones and most USB-C devices.",
    specs=[("Output", "25W PD 3.0 PPS"), ("Cable", "USB-C to C, 1m"), ("Compatible", "Galaxy & USB-C"), ("Warranty", "6 Months")],
    img={"type": "charger", "color": "#2d3748", "cable": "#4a5568"})
add(slug="apple-airpods-4", name="Apple AirPods 4", brand="Apple", cat="accessories", key="earphones",
    price=21900, badge="New",
    short="Redesigned comfort, Personalised Spatial Audio and USB-C case.",
    desc="Apple AirPods 4 deliver a redesigned, more comfortable fit, the H2 chip for richer sound, Personalised Spatial Audio, voice isolation for clear calls and a compact USB-C charging case.",
    specs=[("Chip", "Apple H2"), ("Audio", "Spatial Audio"), ("Battery", "Up to 30h with case"), ("Charging", "USB-C"), ("Water", "IP54")],
    img={"type": "earbuds", "color": "#ffffff", "accent": "#48bb78", "stem": True})
add(slug="boat-airdopes-141", name="boAt Airdopes 141", brand="boAt", cat="accessories", key="earphones",
    price=2999, old_price=3999, badge="Sale",
    short="42 hours playback, ENx noise cancellation and low-latency mode.",
    desc="Best-selling true wireless earbuds with up to 42 hours of total playback, ENx technology for clear calls, BEAST low-latency mode for gaming and ASAP fast charging.",
    specs=[("Playback", "Up to 42h"), ("Calls", "ENx Mic"), ("Gaming", "BEAST Mode 50ms"), ("Bluetooth", "5.3"), ("Water", "IPX4")],
    img={"type": "earbuds", "color": "#2d3748", "accent": "#e53e3e", "stem": False})
add(slug="iphone-17-pro-magsafe-silicone-case", name="iPhone 17 Pro MagSafe Silicone Case", brand="Janta Select", cat="accessories", key="cases",
    price=1999,
    short="Soft-touch silicone with microfibre lining and MagSafe magnets.",
    desc="Premium soft-touch silicone case with a microfibre lining, raised camera and screen edges for protection, and built-in magnets for MagSafe chargers and accessories.",
    specs=[("Fits", "iPhone 17 Pro"), ("Material", "Liquid silicone"), ("MagSafe", "Yes"), ("Colours", "Blue, Navy, Black")],
    img={"type": "case", "color": "#2f6bff", "second": "#0a1f44"})
add(slug="spigen-ultra-hybrid-clear-case", name="Spigen Ultra Hybrid Clear Case", brand="Spigen", cat="accessories", key="cases",
    price=2499, featured=True,
    short="Crystal-clear back with Air Cushion corners. Galaxy & iPhone models.",
    desc="Show off your phone's design with crystal-clear protection. Ultra Hybrid combines a rigid anti-yellowing back with a flexible TPU bumper and Air Cushion Technology corners.",
    specs=[("Fits", "iPhone & Galaxy models"), ("Material", "PC + TPU"), ("Drop", "Military-grade"), ("Finish", "Anti-yellowing clear")],
    img={"type": "case", "clear": True})
add(slug="xiaomi-20000mah-power-bank", name="Xiaomi 20000mAh Power Bank", brand="Xiaomi", cat="accessories", key="power-banks",
    price=3999, badge="Hot",
    short="22.5W fast charging, dual output and USB-C input.",
    desc="Keep going all day. Xiaomi's 20000mAh power bank charges most phones 4–5 times, supports 22.5W fast charging, and can power two devices at once with smart temperature protection.",
    specs=[("Capacity", "20000mAh"), ("Output", "22.5W max"), ("Ports", "2x USB-A, 1x USB-C"), ("Warranty", "6 Months")],
    img={"type": "powerbank", "color": "#1f2937", "accent": "#2f6bff", "label": "20000mAh"})
add(slug="anker-10000mah-power-bank", name="Anker PowerCore 10000mAh", brand="Anker", cat="accessories", key="power-banks",
    price=3499,
    short="Ultra-compact, PowerIQ fast charging, fits in your pocket.",
    desc="One of the smallest and lightest 10000mAh power banks. Anker PowerIQ and VoltageBoost deliver the fastest possible charge to your phone, earbuds or watch.",
    specs=[("Capacity", "10000mAh"), ("Output", "12W PowerIQ"), ("Size", "Pocket-sized"), ("Warranty", "18 Months")],
    img={"type": "powerbank", "color": "#f1f5f9", "accent": "#00a6ff", "label": "10000mAh"})
add(slug="iphone-tempered-glass-9h", name="iPhone Tempered Glass 9H", brand="Janta Select", cat="accessories", key="screen-protectors",
    price=799,
    short="Edge-to-edge 9H tempered glass with easy installation frame.",
    desc="Protect your iPhone display with edge-to-edge 9H tempered glass. Oleophobic coating resists fingerprints, and the included alignment frame makes bubble-free installation easy.",
    specs=[("Hardness", "9H"), ("Fits", "iPhone 13 – 17 series"), ("Coating", "Oleophobic"), ("Pack", "2 pieces + frame")],
    img={"type": "glass", "tint": "#9cc0ff"})
add(slug="samsung-privacy-screen-protector", name="Galaxy Privacy Screen Protector", brand="Janta Select", cat="accessories", key="screen-protectors",
    price=1299,
    short="Anti-spy privacy glass that keeps your screen private.",
    desc="Keep prying eyes away. This privacy tempered glass darkens the screen from side angles while staying crystal clear head-on. Fingerprint-sensor compatible for Galaxy S and A series.",
    specs=[("Hardness", "9H"), ("Privacy", "30° anti-spy"), ("Fits", "Galaxy S & A series"), ("Sensor", "Fingerprint compatible")],
    img={"type": "glass", "tint": "#334155"})

# ------------------------------------------------------------------ variants
# Options customers choose in the "Buy Now" window.
#   opt("Storage", ("256GB", 0), ("512GB", 35000))   -> text choices; number = extra price in Rs. (0 = same price)
#   colour("body", ("Deep Blue", "#2f3f63"), ...)     -> colour swatches; first colour = default photo.
#       The first word is the part of the product illustration to recolour
#       (phone: body · watch: strap / case · accessories: color). Use colour(None, ...) for real photos.


def opt(name, *vals):
    return {"name": name, "kind": "text", "values": [{"label": v[0], "add": v[1] if len(v) > 1 else 0} for v in vals]}


def colour(param, *vals, name="Colour"):
    return {"name": name, "kind": "colour", "param": param,
            "values": [{"label": v[0], "hex": v[1], "add": v[2] if len(v) > 2 else 0} for v in vals]}


VARIANTS = {
    # ---- Phones
    "iphone-17-pro-max": [opt("Storage", ("256GB", 0), ("512GB", 35000), ("1TB", 70000)),
                          colour("body", ("Cosmic Orange", "#c8742f"), ("Deep Blue", "#2f3f63"), ("Silver", "#d9dde3"))],
    "iphone-16": [opt("Storage", ("128GB", 0), ("256GB", 15000), ("512GB", 40000)),
                  colour("body", ("Ultramarine", "#6b8fd6"), ("Teal", "#8fc1b5"), ("Pink", "#f1b8c8"), ("White", "#eef0f2"), ("Black", "#3a3d42"))],
    "samsung-galaxy-s25-ultra": [opt("Memory", ("12GB / 256GB", 0), ("12GB / 512GB", 20000), ("12GB / 1TB", 50000)),
                                 colour("body", ("Titanium Gray", "#5b6070"), ("Titanium Silverblue", "#8fa3bf"), ("Titanium Black", "#2f3136"), ("Titanium Whitesilver", "#e3e5e8"))],
    "samsung-galaxy-a56": [opt("Memory", ("8GB / 256GB", 0), ("12GB / 256GB", 5000)),
                           colour("body", ("Awesome Olive", "#9fb7a8"), ("Awesome Graphite", "#3d4148"), ("Awesome Lightgray", "#d5d8dc"), ("Awesome Pink", "#e8c4cc"))],
    "xiaomi-15": [opt("Memory", ("12GB / 256GB", -8000), ("12GB / 512GB", 0)),
                  colour("body", ("White", "#e8e9ec"), ("Black", "#2d2f33"), ("Green", "#7c9a86"))],
    "redmi-note-14-pro-plus": [opt("Memory", ("8GB / 256GB", 0), ("12GB / 512GB", 8000)),
                               colour("body", ("Aurora Purple", "#7c5cbf"), ("Midnight Black", "#2d2f33"), ("Frost Blue", "#9cc3e6"))],
    "oneplus-13": [opt("Memory", ("12GB / 256GB", 0), ("16GB / 512GB", 15000)),
                   colour("body", ("Midnight Ocean", "#1f3b73"), ("Black Eclipse", "#25272b"), ("Arctic Dawn", "#e6e2dc"))],
    "oneplus-nord-ce4": [opt("Memory", ("8GB / 128GB", 0), ("8GB / 256GB", 3000)),
                         colour("body", ("Celadon Marble", "#3c6e5a"), ("Dark Chrome", "#3a3d42"))],
    "vivo-v50": [opt("Memory", ("8GB / 256GB", 0), ("12GB / 512GB", 7000)),
                 colour("body", ("Rose Red", "#d9a5b3"), ("Titanium Grey", "#8a8f98"), ("Starry Blue", "#34508c"))],
    "vivo-y29": [opt("Memory", ("6GB / 128GB", 0), ("8GB / 128GB", 2000), ("8GB / 256GB", 5000)),
                 colour("body", ("Glacier Blue", "#2b4d8c"), ("Diamond Black", "#2d2f33"), ("Titanium Gold", "#c9b28d"))],
    "oppo-reno13": [opt("Memory", ("12GB / 256GB", 0), ("12GB / 512GB", 8000)),
                    colour("body", ("Luminous Blue", "#b9c6e8"), ("Plume White", "#eef0f2"), ("Graphite Grey", "#4a4d55"))],
    "oppo-a3x": [opt("Memory", ("4GB / 128GB", 0), ("6GB / 128GB", 2000)),
                 colour("body", ("Nebula Red", "#c53030"), ("Ocean Blue", "#3b6fb6"), ("Starry Purple", "#7b6bb0"))],
    "realme-14-pro-plus": [opt("Memory", ("8GB / 256GB", 0), ("12GB / 512GB", 8000)),
                           colour("body", ("Pearl White", "#e2e8f0"), ("Suede Grey", "#8a8f98"), ("Bikaner Purple", "#7e5aa8"))],
    "realme-c75": [opt("Memory", ("8GB / 128GB", 0), ("8GB / 256GB", 3000)),
                   colour("body", ("Lightning Gold", "#d69e2e"), ("Midnight Lily", "#2d3a55"))],
    # ---- Watches
    "apple-watch-series-11": [opt("Case Size", ("42mm", 0), ("46mm", 4000)),
                              colour("strap", ("Blue Sport Band", "#1a3c7a"), ("Black Sport Band", "#2a2d33"), ("Starlight Sport Band", "#e6dccb"), ("Pink Sport Band", "#e8b4c0"), name="Band")],
    "apple-watch-ultra-3": [opt("Finish", ("Natural Titanium", 0), ("Black Titanium", 0)),
                            colour("strap", ("Orange Alpine Loop", "#e86b2c"), ("Black Trail Loop", "#2a2d33"), ("Blue Ocean Band", "#2e6fd8"), name="Band")],
    "samsung-galaxy-watch8": [opt("Case Size", ("40mm", -4000), ("44mm", 0)), opt("Connectivity", ("Bluetooth", 0), ("LTE", 6000)),
                              colour("case", ("Graphite", "#3b4253"), ("Silver", "#c3c8d0"))],
    "samsung-galaxy-watch8-classic": [opt("Connectivity", ("Bluetooth", 0), ("LTE", 6000)),
                                      colour("case", ("Silver", "#b7bcc6"), ("Black", "#3b4253"))],
    "huawei-watch-gt-5-pro": [opt("Model", ("46mm Titanium", 0), ("42mm Ceramic", 6000)),
                              colour("strap", ("Black Fluoroelastomer", "#2b2b2b"), ("Brown Leather", "#6b4a2f"), ("Titanium Link", "#9aa1ad"), name="Strap")],
    "huawei-watch-fit-4": [colour("strap", ("Blue", "#7f9cf5"), ("Black", "#2a2d33"), ("White", "#e8e8ea"), ("Green", "#7fbf9a"))],
    "amazfit-active-2": [opt("Edition", ("Standard", 0), ("Premium (Sapphire)", 3000)),
                         colour("strap", ("Black Silicone", "#1a202c"), ("Brown Leather", "#7a5236"), name="Strap")],
    "amazfit-gts-4": [colour("strap", ("Misty White", "#f7f3ee"), ("Infinite Black", "#2a2d33"), ("Rosebud Pink", "#e7b7b7"))],
    "noisefit-halo-2": [colour("strap", ("Stone Grey", "#4a5568"), ("Elite Black", "#1f2228"), ("Classic Brown", "#7a5236"), name="Strap")],
    "noise-colorfit-pro-6": [colour("strap", ("Midnight Blue", "#2c5282"), ("Jet Black", "#1f2228"), ("Rose Pink", "#e6a9b5"))],
    "boat-wave-sigma-3": [colour("strap", ("Cherry Red", "#e53e3e"), ("Active Black", "#1f2228"), ("Teal Green", "#2c9c9c"))],
    "boat-lunar-discovery": [colour("strap", ("Deep Blue", "#1a365d"), ("Active Black", "#1f2228"), ("Burgundy", "#6b2737"))],
    # ---- Accessories
    "apple-20w-usb-c-power-adapter": [opt("Bundle", ("Adapter only", 0), ("With USB-C cable (1m)", 1500))],
    "samsung-25w-super-fast-charger": [colour("color", ("Black", "#2d3748"), ("White", "#f4f6fa"))],
    "apple-airpods-4": [opt("Model", ("AirPods 4", 0), ("AirPods 4 with ANC", 6000))],
    "boat-airdopes-141": [colour("color", ("Bold Black", "#2d3748"), ("Pure White", "#f2f3f5"), ("Cider Cyan", "#5cc6c6"))],
    "iphone-17-pro-magsafe-silicone-case": [opt("Model", ("iPhone 17 Pro", 0), ("iPhone 17 Pro Max", 200)),
                                            colour("color", ("Blue", "#2f6bff"), ("Black", "#1f2228"), ("Pink", "#e9a6b8"), ("Green", "#5f8f6f"))],
    "spigen-ultra-hybrid-clear-case": [opt("Model", ("iPhone 17 Pro",), ("iPhone 17 Pro Max",), ("iPhone 16",), ("Galaxy S25 Ultra",), ("Galaxy A56",))],
    "xiaomi-20000mah-power-bank": [colour("color", ("Black", "#1f2937"), ("Blue", "#2b4d8c"))],
    "anker-10000mah-power-bank": [colour("color", ("White", "#f1f5f9"), ("Black", "#1f2937"), ("Blue", "#2f6bff"))],
    "iphone-tempered-glass-9h": [opt("Model", ("iPhone 17 Pro Max",), ("iPhone 17 Pro",), ("iPhone 17",), ("iPhone 16 / 15",), ("iPhone 14 / 13",)),
                                 opt("Pack", ("2 pieces", 0), ("4 pieces", 600))],
    "samsung-privacy-screen-protector": [opt("Model", ("Galaxy S25 Ultra",), ("Galaxy S25",), ("Galaxy A56",), ("Galaxy A36",))],
}

for _p in P:
    _p["options"] = VARIANTS.get(_p["slug"], [])

PRODUCTS = P
