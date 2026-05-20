import streamlit as st
import time
import random

# Konfigurimi i faqes së aplikacionit
st.set_page_config(page_title="Tava & Dhe - Delivery App", page_icon="🍲", layout="centered")

# Stilimi i aplikacionit me dizajn modern dhe ngjyra të ngrohta
st.markdown("""
 ~~~~~~~~~~~^^^^
        <style>
        ^^^^^^^
    ...<17 lines>...
        </style>
        ^^^^^^^^
    """True)
    .main background-color: #fcfaf7; }
    h1, h2, h3 { color: #8B4513; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { 
        background-color: #8B4513; 
        color: white; 
        border-radius: 20px; 
        ^
        border: none;
        padding: 10px 24px;
    }
    .stButton>button:hover { background-color: #A0522D; color: white; }
    .box { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_index=True)

# Titulli i Aplikacionit
st.title("🍲 Tava & Dhe")
st.subheader("Tradita e Tavës së Dheut, direkt në shtëpinë tuaj!")
st.write("---")

# Menaxhimi i hapave të aplikacionit (State)
if 'page' not in st.session_state:
    st.session_state.page = 'menu'
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- HAPI 1: MENUJA DHE SELEKSIONIMI ---
if st.session_state.page == 'menu':
    st.markdown("### 📋 Menuja Jonë Autentike")
    st.write("Zgjidhni tavën tuaj të preferuar të gatuar në enë dheu:")
    
    # Produktet sipas prezantimit të Vajzës së Dytë
    menu_items = {
        "Tavë Dheu Tradicionale e Tiranës": {"përbërësit": "Mish viçi, gjizë fshati, hudhra, domate, erëza lokale", "çmimi": 650},
        "Tavë Dheu me Mish Qengji": {"përbërësit": "Mish qengji i butë, salcë kosi, tave e pjekur në furrë druri", "çmimi": 800},
        "Tavë Dheu Vegjetariane": {"përbërësit": "Perime të pjekura stine, djathë kaçkavall i shkrirë, salcë shtëpie", "çmimi": 500}
    }
    
    for item, info in menu_items.items():
        st.markdown(f"""
        <div class="box">
            <h4>{item} — {info['çmimi']} ALL</h4>
            <p style='color: grey; font-size: 14px;'>{info['përbërësit']}</p>
        </div>
        """, unsafe_allow_index=True)
        
        # Butoni për të shtuar në shportë
        if st.button(f"Shto në Shportë: {item}", key=item):
            st.session_state.cart[item] = st.session_state.cart.get(item, 0) + 1
            st.success(f"U shtua: {item}!")
            
    st.write("---")
    
    # Shfaqja e Shportës
    if st.session_state.cart:
        st.markdown("### 🛒 Shporta Juaj")
        total = 0
        for item, qty in st.session_state.cart.items():
            subtotal = qty * menu_items[item]['çmimi']
            total += subtotal
            st.write(f"• {item} x{qty} — {subtotal} ALL")
        
        st.markdown(f"*Totali për të paguar: {total} ALL*")
        
        if st.button("Vazhdo te Pagesa & Delivery ➔"):
            st.session_state.page = 'checkout'
            st.rerun()

# --- HAPI 2: CHECKOUT & PAGESA ---
elif st.session_state.page == 'checkout':
    st.markdown("### 📍 Detajet e Porosisë & Pagesa")
    
    with st.form("delivery_form"):
        emri = st.text_input("Emri dhe Mbiemri", placeholder="Psh. Filan Fisteku")
        Adresa = st.text_input("Adresa e Dorëzimit (Tiranë)", placeholder="Psh. Rruga Sami Frashëri, Ndërtesa 5, Kati 3")
        telefoni = st.text_input("Numri i Telefonit", placeholder="06X XX XX XXX")
        
        metoda_pageses = st.radio(
            "Zgjidhni mënyrën e pagesës:",
            ('Kesh në dorë (Cash on Delivery)', 'Kartë Krediti/Debiti (In-App Payment)')
        )
        
        if metoda_pageses == 'Kartë Krediti/Debiti (In-App Payment)':
            st.text_input("Numri i Kartës", placeholder="XXXX XXXX XXXX XXXX")
            
        st.write("🎁 Programi i Pikëve: Kjo porosi ju shton 1 pikë në aplikacion!")
        
        submit_order = st.form_submit_button("Konfirmo dhe Dërgo Porosinë 🚀")
        
        if submit_order:
            if not emri or not Adresa or not telefoni:
                st.error("Ju lutem plotësoni të gjitha fushat e nevojshme!")
            else:
                st.session_state.page = 'tracking'
                st.rerun()

# --- HAPI 3: LIVE TRACKING (Simulimi i Vajzës së Tretë) ---
elif st.session_state.page == 'tracking':
    st.markdown("### 🛵 Ndjekja e Porosisë në Kohë Reale")
    st.info("Faleminderit! Porosia juaj u pranua dhe po përgatitet në furrë.")
    
    # Hapat e dorëzimit me kohëmatës (simulim)
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Hapësirë për të simuluar lëvizjen e korrierit elektrik
    status_steps = [
        {"përparimi": 25, "mesazhi": "👨‍🍳 Kuzhinierët po përgatisin tavën tuaj në enën e dheut..."},
        {"përparimi": 50, "mesazhi": "🔥 Tava doli nga furra dhe po paketohet në çantën termike..."},
        {"përparimi": 75, "mesazhi": "🛵 Korrieri ynë elektrik sapo u nis drejt adresës suaj..."},
        {"përparimi": 100, "mesazhi": "🎉 Korrieri ka mbërritur! Ju bëftë mirë Tava e Dheut! 🍲"}
    ]
    
    for step in status_steps:
        status_text.markdown(f"*Statusi aktual:* {step['mesazhi']}")
        progress_bar.progress(step['përparimi'])
        time.sleep(3) # Simulon vonesën mes etapave (mund ta ulni për prezantim më të shpejtë)
        
    st.balloons()
    
    if st.button("Kthehu te Menuja Kryesore"):
        st.session_state.cart = {}
        st.session_state.page = 'menu'
        st.rerun()
