import streamlit as st
import nmap
import pandas as pd
from datetime import datetime

# =====================================================
# SESSION STATE
# =====================================================
if "devices" not in st.session_state:
    st.session_state.devices = pd.DataFrame()

# =====================================================
# NETWORK SCAN (NMAP)
# =====================================================
def scan_network(network_range):
    nm = nmap.PortScanner()
    nm.scan(
        hosts=network_range,
        arguments="-sn"
    )

    devices = []
    for host in nm.all_hosts():
        devices.append({
            "IP Address": host,
            "Hostname": nm[host].hostname() or "Unknown",
            "MAC Address": nm[host]["addresses"].get("mac", "Unknown"),
            "Status": nm[host].state(),
            "Last Seen": datetime.now().strftime("%H:%M:%S")
        })

    return pd.DataFrame(devices)

# =====================================================
# UI
# =====================================================
st.title("📶 WiFi / Network Device Monitor")

st.sidebar.header("⚙️ Network Settings")

network_range = st.sidebar.text_input(
    "Network Range",
    "192.168.1.0/24"
)

st.sidebar.info(
    "Aplikasi ini hanya menampilkan device "
    "yang aktif di jaringan (LAN & WiFi)."
)

# =====================================================
# SCAN BUTTON
# =====================================================
if st.button("🔍 Scan Devices"):
    with st.spinner("Scanning network..."):
        st.session_state.devices = scan_network(network_range)

# =====================================================
# DISPLAY RESULT
# =====================================================
st.header("🖥️ Connected Devices")

if st.session_state.devices.empty:
    st.info("Belum ada data. Klik **Scan Devices**.")
else:
    st.dataframe(
        st.session_state.devices,
        use_container_width=True
    )
    st.success(
        f"Total device terdeteksi: {len(st.session_state.devices)}"
    )
