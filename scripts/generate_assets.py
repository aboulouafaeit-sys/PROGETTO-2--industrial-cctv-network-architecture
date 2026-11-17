#!/usr/bin/env python3
"""
Industrial Asset & Screenshot Generator for PROGETTO 2
Generates 100% XML-valid SVGs AND high-resolution PNG screenshots.
"""

import os
import glob
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape as xml_escape
from PIL import Image, ImageDraw, ImageFont

FONT_MONO = "C:/Windows/Fonts/consola.ttf" if os.path.exists("C:/Windows/Fonts/consola.ttf") else None
FONT_MONO_BOLD = "C:/Windows/Fonts/consolab.ttf" if os.path.exists("C:/Windows/Fonts/consolab.ttf") else FONT_MONO
FONT_SANS = "C:/Windows/Fonts/segoeui.ttf" if os.path.exists("C:/Windows/Fonts/segoeui.ttf") else None
FONT_SANS_BOLD = "C:/Windows/Fonts/segoeuib.ttf" if os.path.exists("C:/Windows/Fonts/segoeuib.ttf") else FONT_SANS

def get_font(path, size):
    if path and os.path.exists(path):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def generate_topology_svg(output_path):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" width="100%" height="100%" style="background:#0b0f19; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,sans-serif;">
  <defs>
    <linearGradient id="bgGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="firewallGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <linearGradient id="storageGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/>
    </filter>
    <filter id="glowGreen" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="0" y="0" width="1400" height="900" fill="url(#bgGlow)"/>
  <rect x="40" y="30" width="1320" height="70" rx="12" fill="#111827" stroke="#1f2937" stroke-width="1.5" filter="url(#shadow)"/>
  <circle cx="75" cy="65" r="18" fill="#0284c7" />
  <path d="M68 65 L73 70 L83 60" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
  <text x="110" y="58" fill="#f8fafc" font-size="20" font-weight="700">INDUSTRIAL CCTV &amp; HIGH-AVAILABILITY NETWORK ARCHITECTURE</text>
  <text x="110" y="80" fill="#94a3b8" font-size="13">20-Camera Zero-Trust Factory Infrastructure | IEC 62443-3-3 SL-2 &amp; NIS2 Compliant</text>
  <rect x="1170" y="47" width="165" height="34" rx="6" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1"/>
  <text x="1185" y="69" fill="#38bdf8" font-size="12" font-weight="600">PRODUCTION READY</text>

  <!-- FIELD ACCESS LAYER (LEFT) -->
  <rect x="40" y="130" width="360" height="730" rx="14" fill="#0b1329" stroke="#1e293b" stroke-width="2"/>
  <text x="65" y="165" fill="#38bdf8" font-size="16" font-weight="700">FIELD INDUSTRIAL ACCESS (IDFs)</text>
  <text x="65" y="185" fill="#64748b" font-size="12">Category 6A S/FTP | IP66 Cabinets | Dual 24V DC-UPS</text>

  <!-- IDF-1 Card -->
  <g filter="url(#shadow)">
    <rect x="60" y="210" width="320" height="190" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="85" cy="235" r="8" fill="#10b981" filter="url(#glowGreen)"/>
    <text x="105" y="240" fill="#f1f5f9" font-size="14" font-weight="700">IDF-1: SW-ACC-IDF1 (IE3400)</text>
    <text x="85" y="265" fill="#94a3b8" font-size="11">Role: 8x Perimeter AI 4K Cameras (CAM-01..08)</text>
    <text x="85" y="285" fill="#94a3b8" font-size="11">VLAN: 20 (CCTV-PERIMETER) | 10.240.20.0/24</text>
    <text x="85" y="305" fill="#94a3b8" font-size="11">PoE Load: 190.0W / 480W (39.58%) | 802.3bt</text>
    <text x="85" y="325" fill="#94a3b8" font-size="11">Cabling: Cat6A S/FTP Shielded (Single Ground)</text>
    <rect x="85" y="345" width="270" height="35" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="98" y="367" fill="#38bdf8" font-size="11" font-weight="600">Dual 10G SFP+ Uplink LACP (Po1)</text>
  </g>

  <!-- IDF-2 Card -->
  <g filter="url(#shadow)">
    <rect x="60" y="425" width="320" height="190" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="85" cy="450" r="8" fill="#10b981" filter="url(#glowGreen)"/>
    <text x="105" y="455" fill="#f1f5f9" font-size="14" font-weight="700">IDF-2: SW-ACC-IDF2 (IE3400)</text>
    <text x="85" y="480" fill="#94a3b8" font-size="11">Role: 8x Factory High-Speed 60fps (CAM-09..16)</text>
    <text x="85" y="500" fill="#94a3b8" font-size="11">VLAN: 21 (CCTV-FACTORY) | 10.240.21.0/24</text>
    <text x="85" y="520" fill="#94a3b8" font-size="11">PoE Load: 103.2W / 480W (21.50%) | M12 X-Code</text>
    <text x="85" y="540" fill="#94a3b8" font-size="11">EMI Mitigation: High VFD &amp; Arc Weld Shielding</text>
    <rect x="85" y="560" width="270" height="35" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="98" y="582" fill="#38bdf8" font-size="11" font-weight="600">Dual 10G SFP+ Uplink LACP (Po2)</text>
  </g>

  <!-- IDF-3 Card -->
  <g filter="url(#shadow)">
    <rect x="60" y="640" width="320" height="200" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="85" cy="665" r="8" fill="#10b981" filter="url(#glowGreen)"/>
    <text x="105" y="670" fill="#f1f5f9" font-size="14" font-weight="700">IDF-3: SW-ACC-IDF3 (IE3400)</text>
    <text x="85" y="695" fill="#94a3b8" font-size="11">Role: 2x Docks (CAM-17..18) + 2x ANPR (CAM-19..20)</text>
    <text x="85" y="715" fill="#94a3b8" font-size="11">VLAN: 21 &amp; 22 (ANPR-GATE) | 10.240.22.0/24</text>
    <text x="85" y="735" fill="#94a3b8" font-size="11">PoE Load: 76.8W / 480W (16.00%)</text>
    <text x="85" y="755" fill="#94a3b8" font-size="11">Security: Dedicated ANPR Shutter &amp; IR Trigger</text>
    <rect x="85" y="780" width="270" height="35" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="98" y="802" fill="#38bdf8" font-size="11" font-weight="600">Dual 10G SFP+ Uplink LACP (Po3)</text>
  </g>

  <!-- FIBER BACKBONE CONNECTIONS (TRUNKS) -->
  <path d="M380 305 C 440 305, 450 350, 520 350" stroke="#0ea5e9" stroke-width="3" fill="none" stroke-dasharray="6,4"/>
  <path d="M380 520 C 440 520, 450 400, 520 400" stroke="#0ea5e9" stroke-width="3" fill="none" stroke-dasharray="6,4"/>
  <path d="M380 740 C 440 740, 450 450, 520 450" stroke="#0ea5e9" stroke-width="3" fill="none" stroke-dasharray="6,4"/>
  
  <text x="405" y="325" fill="#38bdf8" font-size="11" font-weight="600">10G OM4/OS2</text>
  <text x="405" y="445" fill="#38bdf8" font-size="11" font-weight="600">MACsec-256</text>
  <text x="405" y="615" fill="#38bdf8" font-size="11" font-weight="600">Armored Dual Path</text>

  <!-- MDF CORE LAYER (MIDDLE) -->
  <rect x="520" y="130" width="450" height="730" rx="14" fill="#091429" stroke="#1e3a8a" stroke-width="2"/>
  <text x="545" y="165" fill="#60a5fa" font-size="16" font-weight="700">MDF CORE &amp; FABRIC LAYER (42U RACK)</text>
  <text x="545" y="185" fill="#64748b" font-size="12">StackWise-480 SSO | VRF Microsegmentation | Non-Routed iSCSI</text>

  <!-- Core Switch Stack Box -->
  <g filter="url(#shadow)">
    <rect x="545" y="210" width="400" height="280" rx="10" fill="url(#cardGrad)" stroke="#2563eb" stroke-width="2"/>
    <rect x="560" y="225" width="370" height="50" rx="6" fill="url(#coreGrad)"/>
    <text x="575" y="255" fill="#fff" font-size="15" font-weight="700">SW-CORE-STK (Cisco C9300-24S Stack)</text>
    
    <text x="565" y="300" fill="#93c5fd" font-size="12" font-weight="600">Active / Standby Hot Stateful Switchover (SSO)</text>
    <text x="565" y="320" fill="#94a3b8" font-size="11">• StackWise-480 Ring Interconnect @ 480 Gbps</text>
    <text x="565" y="340" fill="#94a3b8" font-size="11">• VRF-Lite: VRF_CCTV_OT (L3 Boundaries &amp; SVI Gateways)</text>
    <text x="565" y="360" fill="#94a3b8" font-size="11">• Security: DHCP Snooping, Dynamic ARP Inspection (DAI)</text>
    <text x="565" y="380" fill="#94a3b8" font-size="11">• QoS Engine: MQC Strict Priority (EF) &amp; AF41 Video (70%)</text>
    <text x="565" y="400" fill="#94a3b8" font-size="11">• Routing: OSPFv2 Area 0 peering to FortiGate HA Cluster</text>
    
    <rect x="565" y="420" width="370" height="55" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="580" y="442" fill="#38bdf8" font-size="11" font-weight="600">Ports: 24x 10G SFP+ | Jumbo Frames MTU 9198</text>
    <text x="580" y="460" fill="#a5f3fc" font-size="10">Sub-second Failover NSF/SSO Deterministic &lt;50ms</text>
  </g>

  <!-- Dell PowerEdge VMS Card -->
  <g filter="url(#shadow)">
    <rect x="545" y="510" width="400" height="155" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="570" cy="535" r="8" fill="#10b981" filter="url(#glowGreen)"/>
    <text x="590" y="540" fill="#f1f5f9" font-size="14" font-weight="700">Dell PowerEdge R750xa (VMS &amp; AI Node)</text>
    <text x="565" y="565" fill="#94a3b8" font-size="11">GPU: NVIDIA RTX 6000 Ada (48GB GDDR6 ECC) / TensorRT</text>
    <text x="565" y="585" fill="#94a3b8" font-size="11">Dual Xeon Gold 6338 (64T) | 128GB ECC | Dual 10G LACP</text>
    <text x="565" y="605" fill="#94a3b8" font-size="11">IP: 10.240.30.10 (VLAN 30) | Milestone / Genetec Server</text>
    <text x="565" y="625" fill="#94a3b8" font-size="11">AI Workload: 20 Streams Secondary Inferencing &lt;12ms</text>
    <text x="565" y="645" fill="#10b981" font-size="11" font-weight="600">Storage Connectivity: Dual 10G iSCSI MPIO Round-Robin</text>
  </g>

  <!-- Storage Vault SAN Card -->
  <g filter="url(#shadow)">
    <rect x="545" y="685" width="400" height="155" rx="10" fill="url(#cardGrad)" stroke="#059669" stroke-width="1.5"/>
    <rect x="560" y="700" width="370" height="35" rx="6" fill="url(#storageGrad)"/>
    <text x="575" y="723" fill="#fff" font-size="13" font-weight="700">Dell PowerVault ME5012 SAN (Isolated Fabric)</text>
    <text x="565" y="755" fill="#a7f3d0" font-size="11" font-weight="600">RAID-6: 12x 16TB SAS (9 Data + 2 Parity + 1 Global Spare)</text>
    <text x="565" y="775" fill="#94a3b8" font-size="11">Net Usable: 117.87 TiB | Ingestion: 1.073 TiB/day</text>
    <text x="565" y="795" fill="#34d399" font-size="11" font-weight="700">Calculated Retention: 109.9 DAYS (Target: &gt;=30 Days)</text>
    <text x="565" y="815" fill="#94a3b8" font-size="11">VLAN 40 (Subnet A) &amp; VLAN 41 (Subnet B) Non-Routed L2</text>
  </g>

  <!-- FIREWALL & SOC LAYER (RIGHT) -->
  <rect x="1000" y="130" width="360" height="730" rx="14" fill="#130a17" stroke="#4c1d95" stroke-width="2"/>
  <text x="1025" y="165" fill="#c084fc" font-size="16" font-weight="700">ZERO-TRUST SECURITY &amp; SOC</text>
  <text x="1025" y="185" fill="#64748b" font-size="12">Next-Gen Inspection | Airgap | SOC Workstations</text>

  <!-- FortiGate HA Card -->
  <g filter="url(#shadow)">
    <rect x="1020" y="210" width="320" height="240" rx="10" fill="url(#cardGrad)" stroke="#b91c1c" stroke-width="2"/>
    <rect x="1035" y="225" width="290" height="40" rx="6" fill="url(#firewallGrad)"/>
    <text x="1050" y="250" fill="#fff" font-size="14" font-weight="700">FortiGate 100F HA Cluster</text>
    <text x="1035" y="285" fill="#fca5a5" font-size="11" font-weight="600">Active-Passive FGCP Heartbeat (ha1 / ha2)</text>
    <text x="1035" y="305" fill="#94a3b8" font-size="11">• Layer-7 Deep Packet Inspection (DPI)</text>
    <text x="1035" y="325" fill="#94a3b8" font-size="11">• Protocol Filtering: Strict RTSP (554), ONVIF, RTP</text>
    <text x="1035" y="345" fill="#94a3b8" font-size="11">• Lateral Movement Block: Inter-Camera Deny</text>
    <text x="1035" y="365" fill="#94a3b8" font-size="11">• Airgap Enforcement: Internet Outbound Blocked</text>
    <text x="1035" y="385" fill="#94a3b8" font-size="11">• IPS Throughput &gt; 2.6 Gbps | State Sync &lt;1s</text>
    <rect x="1035" y="405" width="290" height="30" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="1045" y="425" fill="#f87171" font-size="11" font-weight="600">VIP: 10.240.99.1 (VLAN 99 Transit)</text>
  </g>

  <!-- SOC Monitoring Card -->
  <g filter="url(#shadow)">
    <rect x="1020" y="480" width="320" height="170" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="1045" cy="505" r="8" fill="#10b981" filter="url(#glowGreen)"/>
    <text x="1065" y="510" fill="#f1f5f9" font-size="14" font-weight="700">SOC Control Room (VLAN 50)</text>
    <text x="1035" y="535" fill="#94a3b8" font-size="11">Subnet: 10.240.50.0/26 | Gateway: 10.240.50.1</text>
    <text x="1035" y="555" fill="#94a3b8" font-size="11">Clients: Multi-Monitor Security Workstations</text>
    <text x="1035" y="575" fill="#94a3b8" font-size="11">Traffic Flow: HTTPS API &amp; RTSPS from VMS</text>
    <text x="1035" y="595" fill="#94a3b8" font-size="11">Security: Direct Camera Access Blocked by NGFW</text>
    <rect x="1035" y="615" width="290" height="25" rx="4" fill="#0f172a"/>
    <text x="1045" y="632" fill="#a855f7" font-size="10" font-weight="600">Zero Direct Edge Exposure Architecture</text>
  </g>

  <!-- Central SIEM / OOBM Card -->
  <g filter="url(#shadow)">
    <rect x="1020" y="675" width="320" height="165" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <circle cx="1045" cy="700" r="8" fill="#38bdf8"/>
    <text x="1065" y="705" fill="#f1f5f9" font-size="14" font-weight="700">Central SIEM &amp; OOBM (VLAN 10)</text>
    <text x="1035" y="730" fill="#94a3b8" font-size="11">Syslog Host: 10.240.10.35 (UDP 514 local7)</text>
    <text x="1035" y="750" fill="#94a3b8" font-size="11">SNMPv3: SHA-256 Auth / AES-256 Priv</text>
    <text x="1035" y="770" fill="#94a3b8" font-size="11">NTP Server: 10.240.10.1 (Precision Clock)</text>
    <text x="1035" y="790" fill="#94a3b8" font-size="11">Telemetry: Environmental &amp; Cabinet Tamper Alarms</text>
    <text x="1035" y="810" fill="#38bdf8" font-size="11" font-weight="600">24/7 Security Event Auditing Active</text>
  </g>

  <!-- Inter-cluster connecting lines -->
  <path d="M945 350 L 1020 330" stroke="#f87171" stroke-width="3" stroke-dasharray="6,4"/>
  <path d="M1020 540 C 970 540, 970 580, 945 580" stroke="#c084fc" stroke-width="2.5" stroke-dasharray="4,4"/>
  <path d="M945 610 L 945 685" stroke="#10b981" stroke-width="3"/>
  <text x="955" y="650" fill="#10b981" font-size="10" font-weight="700">Dual 10G iSCSI</text>
</svg>
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def generate_rack_elevation_svg(output_path):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 950" width="100%" height="100%" style="background:#090d16; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,Helvetica,sans-serif;">
  <defs>
    <linearGradient id="rackGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="2%" stop-color="#0f172a"/>
      <stop offset="98%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="unitGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="ciscoGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#075985"/>
    </linearGradient>
    <linearGradient id="fortiGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
    <linearGradient id="dellGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f766e"/>
      <stop offset="100%" stop-color="#115e59"/>
    </linearGradient>
    <filter id="rackShadow" x="-10%" y="-5%" width="120%" height="110%">
      <feDropShadow dx="0" dy="12" stdDeviation="8" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Header -->
  <text x="50" y="50" fill="#f8fafc" font-size="22" font-weight="700">MDF &amp; IDF PHYSICAL RACK ELEVATIONS</text>
  <text x="50" y="75" fill="#94a3b8" font-size="13">Structured Cabling, Dual Redundant Power Distribution &amp; Environmental Protection</text>

  <!-- LEFT: MDF 42U SERVER RACK -->
  <g transform="translate(60, 110)" filter="url(#rackShadow)">
    <rect x="0" y="0" width="580" height="800" rx="8" fill="url(#rackGrad)" stroke="#475569" stroke-width="3"/>
    <text x="20" y="-15" fill="#38bdf8" font-size="16" font-weight="700">MDF 42U ENTERPRISE SERVER RACK (APC NetShelter SX 1000mm)</text>
    
    <rect x="15" y="15" width="25" height="770" fill="#020617" rx="3"/>
    <text x="20" y="45" fill="#64748b" font-size="10">42U</text>
    <text x="20" y="160" fill="#64748b" font-size="10">36U</text>
    <text x="20" y="320" fill="#64748b" font-size="10">28U</text>
    <text x="20" y="480" fill="#64748b" font-size="10">20U</text>
    <text x="20" y="640" fill="#64748b" font-size="10">10U</text>
    <text x="20" y="775" fill="#64748b" font-size="10">01U</text>

    <!-- Top Cable & Fiber Ingress -->
    <rect x="45" y="20" width="515" height="35" fill="#1e293b" stroke="#334155" rx="4"/>
    <text x="60" y="42" fill="#94a3b8" font-size="11" font-weight="600">Top Overhead Fiber Cable Entry Duct &amp; Grounding Bar (TMGB)</text>

    <!-- 40U-41U: Dual Fiber Patch Panels -->
    <rect x="45" y="65" width="515" height="40" fill="url(#unitGrad)" stroke="#38bdf8" rx="4"/>
    <circle cx="65" cy="85" r="4" fill="#38bdf8"/>
    <circle cx="80" cy="85" r="4" fill="#38bdf8"/>
    <text x="100" y="89" fill="#f8fafc" font-size="12" font-weight="600">41U-40U: 2x 1U LC-Duplex 24-Port Fiber Patch Panels (Trunks from IDF 1-3)</text>

    <!-- 38U-39U: Cisco Catalyst 9300 Core Stack -->
    <rect x="45" y="115" width="515" height="60" fill="url(#ciscoGrad)" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
    <text x="60" y="140" fill="#fff" font-size="12" font-weight="700">39U: Cisco Catalyst 9300-24S (Core Switch 1 - Stack Master)</text>
    <text x="60" y="162" fill="#bfdbfe" font-size="11">24x 10G SFP+ | Dual Redundant AC PSU (Feed A + Feed B) | StackWise-480</text>

    <rect x="45" y="180" width="515" height="60" fill="url(#ciscoGrad)" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
    <text x="60" y="205" fill="#fff" font-size="12" font-weight="700">38U: Cisco Catalyst 9300-24S (Core Switch 2 - Stack Standby)</text>
    <text x="60" y="227" fill="#bfdbfe" font-size="11">24x 10G SFP+ | Hardware SSO Failover &lt;50ms | Line-Rate MACsec-256</text>

    <!-- 36U-37U: FortiGate 100F HA Pair -->
    <rect x="45" y="250" width="515" height="40" fill="url(#fortiGrad)" stroke="#f87171" rx="4"/>
    <text x="60" y="275" fill="#fff" font-size="12" font-weight="700">37U: FortiGate 100F Next-Gen Firewall (Unit 1 - Active Master)</text>

    <rect x="45" y="295" width="515" height="40" fill="url(#fortiGrad)" stroke="#f87171" rx="4"/>
    <text x="60" y="320" fill="#fff" font-size="12" font-weight="700">36U: FortiGate 100F Next-Gen Firewall (Unit 2 - Passive Standby)</text>

    <!-- 30U-32U: Dell PowerEdge R750xa (VMS & AI) -->
    <rect x="45" y="350" width="515" height="75" fill="url(#unitGrad)" stroke="#10b981" stroke-width="1.5" rx="4"/>
    <text x="60" y="380" fill="#f8fafc" font-size="13" font-weight="700">32U-31U: Dell PowerEdge R750xa (VMS Server &amp; AI Engine)</text>
    <text x="60" y="402" fill="#94a3b8" font-size="11">Dual Intel Xeon Gold 6338 | NVIDIA RTX 6000 Ada (48GB) | Dual 10G LACP</text>
    <circle cx="530" cy="380" r="5" fill="#10b981"/>

    <!-- 26U-28U: Dell PowerVault ME5012 SAN -->
    <rect x="45" y="435" width="515" height="85" fill="url(#dellGrad)" stroke="#34d399" stroke-width="2" rx="4"/>
    <text x="60" y="465" fill="#fff" font-size="13" font-weight="700">28U-27U: Dell PowerVault ME5012 Storage SAN (12-Bay 2U)</text>
    <text x="60" y="488" fill="#a7f3d0" font-size="11">12x 16TB SAS 12G in RAID-6 + Hot Spare | 117.87 TiB Usable | 109.9 Days</text>
    <text x="60" y="508" fill="#d1fae5" font-size="10">Dual Active-Active Controllers A &amp; B | 4x 10G iSCSI MPIO (VLAN 40 &amp; 41)</text>

    <!-- 20U-25U: Cable Organizers & Vent Blanks -->
    <rect x="45" y="530" width="515" height="60" fill="#111827" stroke="#1f2937" rx="4"/>
    <text x="180" y="565" fill="#475569" font-size="11">Horizontal 2U Cable Organizers &amp; Vented Blanking Panels</text>

    <!-- 01U-06U: APC Smart-UPS SRT 5000VA RM + Battery Module -->
    <rect x="45" y="600" width="515" height="90" fill="#1e1e2e" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
    <text x="60" y="635" fill="#fbbf24" font-size="13" font-weight="700">06U-04U: APC Smart-UPS SRT 5000VA RM (5kVA / 4.5kW)</text>
    <text x="60" y="658" fill="#94a3b8" font-size="11">Online Double Conversion | Dual AC Infeed | Zero Transfer Time</text>
    <text x="60" y="678" fill="#cbd5e1" font-size="10">SNMPv3 Network Management Card (AP9641) | Battery Runtime: 45 min</text>

    <rect x="45" y="700" width="515" height="80" fill="#1e1e2e" stroke="#d97706" rx="4"/>
    <text x="60" y="740" fill="#fbbf24" font-size="12" font-weight="700">03U-01U: APC SRT192RMBP2 Extended External Battery Pack</text>
  </g>

  <!-- RIGHT: INDUSTRIAL IDF CABINET -->
  <g transform="translate(740, 110)" filter="url(#rackShadow)">
    <rect x="0" y="0" width="580" height="800" rx="14" fill="#0f172a" stroke="#0284c7" stroke-width="3"/>
    <text x="20" y="-15" fill="#38bdf8" font-size="16" font-weight="700">INDUSTRIAL IDF FIELD CABINET (IP66 / NEMA 4 Rittal AX)</text>

    <!-- Peltier Thermoelectric Unit at Top -->
    <rect x="35" y="25" width="510" height="90" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="60" y="60" fill="#38bdf8" font-size="14" font-weight="700">Closed-Loop Thermoelectric Peltier Cooler (IP66 Air-to-Air)</text>
    <text x="60" y="85" fill="#94a3b8" font-size="11">No outside air exchange: 100% sealed against dust, oil mists, and humidity</text>
    <circle cx="500" cy="70" r="15" fill="#0284c7" fill-opacity="0.2"/>
    <text x="495" y="74" fill="#38bdf8" font-size="12">❄</text>

    <!-- 1U Shielded Cat6A Patch Panel -->
    <rect x="35" y="130" width="510" height="65" fill="#111827" stroke="#475569" rx="6"/>
    <text x="55" y="160" fill="#f8fafc" font-size="12" font-weight="700">1U 24-Port Category 6A S/FTP Shielded Patch Panel</text>
    <text x="55" y="180" fill="#38bdf8" font-size="11">Bonded directly to TGB via 16mm² copper braid (Single-Point Ground)</text>

    <!-- 1U Optical Breakout Drawer -->
    <rect x="35" y="205" width="510" height="55" fill="#111827" stroke="#475569" rx="6"/>
    <text x="55" y="235" fill="#f8fafc" font-size="12" font-weight="700">1U Optical Fiber Breakout Drawer (12x LC-Duplex OS2 / OM4)</text>

    <!-- Cisco IE3400 Industrial Heavy Duty Switch -->
    <rect x="35" y="275" width="510" height="150" fill="url(#unitGrad)" stroke="#0ea5e9" stroke-width="2" rx="8"/>
    <rect x="50" y="290" width="480" height="40" rx="4" fill="url(#ciscoGrad)"/>
    <text x="65" y="315" fill="#fff" font-size="13" font-weight="700">Cisco Catalyst IE3400 Heavy Duty (IE-3400-8P4S)</text>
    <text x="55" y="355" fill="#94a3b8" font-size="11">• 8x Gigabit PoE++ Ports (90W 802.3bt) | Operating Temp: -40°C to +75°C</text>
    <text x="55" y="375" fill="#94a3b8" font-size="11">• 4x 10G SFP+ Uplinks | Dual DC Inputs | IEEE 1588 PTP Hardware Timing</text>
    <text x="55" y="395" fill="#94a3b8" font-size="11">• Industrial Alarm Relays: Door Tamper Switch &amp; Cabinet Over-Temp Probe</text>
    <circle cx="500" cy="355" r="5" fill="#10b981"/>

    <!-- Phoenix Contact QUINT4 DC-UPS -->
    <rect x="35" y="440" width="510" height="130" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="55" y="470" fill="#34d399" font-size="13" font-weight="700">Phoenix Contact QUINT4-UPS 24V DC / 20A Power Supply</text>
    <text x="55" y="495" fill="#94a3b8" font-size="11">• IQ Technology Battery Monitoring &amp; State of Charge (SoC) Telemetry</text>
    <text x="55" y="515" fill="#94a3b8" font-size="11">• Redundant Dual Feed Power Inputs with Class I Div 2 Surge Suppressor</text>
    <text x="55" y="535" fill="#a7f3d0" font-size="11">Li-Ion Battery Pack Buffer: 45 min runtime at maximum PoE load</text>

    <!-- Grounding Busbar (TGB) -->
    <rect x="35" y="585" width="510" height="60" fill="#854d0e" stroke="#eab308" stroke-width="1.5" rx="6"/>
    <text x="55" y="615" fill="#fef08a" font-size="12" font-weight="700">Telecommunications Grounding Busbar (TGB) - ANSI/TIA-607-B</text>
    <text x="55" y="633" fill="#fef9c3" font-size="10">Solid Electrolytic Copper Bar 50x6mm | Resistance to TMGB &lt; 1.0 Ohm</text>

    <!-- Industrial Enclosure Specs -->
    <rect x="35" y="660" width="510" height="110" fill="#0b1329" stroke="#1e293b" rx="6"/>
    <text x="55" y="690" fill="#38bdf8" font-size="12" font-weight="700">Enclosure Physical Hardening (IEC 60529 / IK10)</text>
    <text x="55" y="710" fill="#94a3b8" font-size="11">• Double-bit Key Cam Lock with Microswitch Tamper Contact</text>
    <text x="55" y="730" fill="#94a3b8" font-size="11">• Foamed-in PU Gasket resisting hydraulic oils &amp; aggressive solvents</text>
    <text x="55" y="750" fill="#94a3b8" font-size="11">• IP66 / NEMA 4 certified against pressurized factory washdown water</text>
  </g>
</svg>
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def generate_terminal_svg(output_path, title, commands_and_output):
    safe_title = xml_escape(title)
    lines_svg = []
    y = 75
    for item in commands_and_output:
        raw_text = item["text"]
        safe_text = xml_escape(raw_text)
        if item["type"] == "cmd":
            lines_svg.append(f'<text x="25" y="{y}" fill="#38bdf8" font-weight="700" font-size="13">{safe_text}</text>')
            y += 20
        elif item["type"] == "out":
            lines_svg.append(f'<text x="25" y="{y}" fill="#cbd5e1" font-size="12">{safe_text}</text>')
            y += 18
        elif item["type"] == "success":
            lines_svg.append(f'<text x="25" y="{y}" fill="#34d399" font-weight="600" font-size="12">{safe_text}</text>')
            y += 18
        elif item["type"] == "warning":
            lines_svg.append(f'<text x="25" y="{y}" fill="#fbbf24" font-weight="600" font-size="12">{safe_text}</text>')
            y += 18
        elif item["type"] == "dim":
            lines_svg.append(f'<text x="25" y="{y}" fill="#64748b" font-size="11">{safe_text}</text>')
            y += 18
        elif item["type"] == "space":
            y += 10

    total_height = y + 25

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 {total_height}" width="100%" height="100%" style="background:#090d16; font-family:'Cascadia Code','Fira Code','Courier New',monospace;">
  <defs>
    <filter id="termShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect x="5" y="5" width="940" height="{total_height - 10}" rx="8" fill="#0d1117" stroke="#30363d" stroke-width="1.5" filter="url(#termShadow)"/>
  
  <!-- Terminal Title Bar -->
  <rect x="5" y="5" width="940" height="36" rx="8" fill="#161b22"/>
  <circle cx="25" cy="23" r="6" fill="#f85149"/>
  <circle cx="45" cy="23" r="6" fill="#f0883e"/>
  <circle cx="65" cy="23" r="6" fill="#2ea043"/>
  <text x="100" y="27" fill="#8b949e" font-size="12" font-family="'Segoe UI',sans-serif" font-weight="600">{safe_title}</text>

  <!-- Output Lines -->
  {''.join(lines_svg)}
</svg>
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def render_terminal_png(output_path, title, commands_and_output):
    """Renders a pixel-perfect dark theme PNG screenshot of a terminal session."""
    font_mono = get_font(FONT_MONO, 14)
    font_mono_bold = get_font(FONT_MONO_BOLD, 14)
    font_title = get_font(FONT_SANS_BOLD, 13)

    line_height = 20
    calc_y = 60
    for item in commands_and_output:
        if item["type"] == "space":
            calc_y += 10
        else:
            calc_y += line_height

    width = 960
    height = calc_y + 20

    img = Image.new("RGB", (width, height), "#090d16")
    draw = ImageDraw.Draw(img)

    # Window frame
    draw.rounded_rectangle([(10, 10), (width - 10, height - 10)], radius=8, fill="#0d1117", outline="#30363d", width=1)
    
    # Title bar
    draw.rounded_rectangle([(10, 10), (width - 10, 46)], radius=8, fill="#161b22")
    draw.rectangle([(10, 36), (width - 10, 46)], fill="#161b22")
    draw.line([(10, 46), (width - 10, 46)], fill="#30363d", width=1)

    # Window buttons
    draw.ellipse([(25, 22), (37, 34)], fill="#f85149")
    draw.ellipse([(45, 22), (57, 34)], fill="#f0883e")
    draw.ellipse([(65, 22), (77, 34)], fill="#2ea043")

    # Title text
    draw.text((95, 20), title, fill="#8b949e", font=font_title)

    # Content
    y = 60
    for item in commands_and_output:
        t = item["text"]
        itype = item["type"]

        if itype == "cmd":
            draw.text((25, y), t, fill="#38bdf8", font=font_mono_bold)
            y += line_height
        elif itype == "out":
            draw.text((25, y), t, fill="#cbd5e1", font=font_mono)
            y += line_height
        elif itype == "success":
            draw.text((25, y), t, fill="#34d399", font=font_mono_bold)
            y += line_height
        elif itype == "warning":
            draw.text((25, y), t, fill="#fbbf24", font=font_mono_bold)
            y += line_height
        elif itype == "dim":
            draw.text((25, y), t, fill="#64748b", font=font_mono)
            y += line_height
        elif itype == "space":
            y += 10

    img.save(output_path, "PNG")

def generate_vms_dashboard_svg(output_path):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1300 850" width="100%" height="100%" style="background:#06080e; font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e1e2f"/>
      <stop offset="100%" stop-color="#0f111a"/>
    </linearGradient>
    <linearGradient id="camBox" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#151922"/>
      <stop offset="100%" stop-color="#0d1017"/>
    </linearGradient>
    <filter id="dashShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- App Header -->
  <rect x="20" y="15" width="1260" height="60" rx="8" fill="url(#headerGrad)" stroke="#272b38"/>
  <circle cx="50" cy="45" r="14" fill="#3b82f6"/>
  <text x="43" y="50" fill="#fff" font-weight="900" font-size="14">V</text>
  <text x="75" y="42" fill="#f8fafc" font-size="16" font-weight="700">VMS &amp; AI SMART INFERENCE CONSOLE — FACTORY MATRIX (20 CHANNELS)</text>
  <text x="75" y="60" fill="#94a3b8" font-size="11">Milestone Corporate / NVIDIA RTX 6000 Ada Acceleration | Continuous Recording Mode</text>
  
  <rect x="1100" y="27" width="160" height="34" rx="4" fill="#047857" fill-opacity="0.3" stroke="#10b981"/>
  <circle cx="1120" cy="44" r="5" fill="#10b981"/>
  <text x="1135" y="48" fill="#34d399" font-size="11" font-weight="700">ALL 20 FEEDS LIVE</text>

  <!-- KPI Cards Row -->
  <g transform="translate(20, 90)">
    <rect x="0" y="0" width="300" height="75" rx="6" fill="#111622" stroke="#1f293d" filter="url(#dashShadow)"/>
    <text x="15" y="25" fill="#94a3b8" font-size="11">TOTAL VIDEO INGESTION</text>
    <text x="15" y="55" fill="#38bdf8" font-size="22" font-weight="700">104.00 Mbps</text>
    <text x="180" y="53" fill="#10b981" font-size="11">0.56% 10G Bus Load</text>

    <rect x="320" y="0" width="300" height="75" rx="6" fill="#111622" stroke="#1f293d" filter="url(#dashShadow)"/>
    <text x="335" y="25" fill="#94a3b8" font-size="11">GPU INFERENCE SPEED</text>
    <text x="335" y="55" fill="#a855f7" font-size="22" font-weight="700">11.2 ms / frame</text>
    <text x="480" y="53" fill="#c084fc" font-size="11">TensorRT FP16</text>

    <rect x="640" y="0" width="300" height="75" rx="6" fill="#111622" stroke="#1f293d" filter="url(#dashShadow)"/>
    <text x="655" y="25" fill="#94a3b8" font-size="11">STORAGE AUTONOMY (RAID-6)</text>
    <text x="655" y="55" fill="#34d399" font-size="22" font-weight="700">109.9 Days</text>
    <text x="810" y="53" fill="#10b981" font-size="11">117.87 TiB Usable</text>

    <rect x="960" y="0" width="300" height="75" rx="6" fill="#111622" stroke="#1f293d" filter="url(#dashShadow)"/>
    <text x="975" y="25" fill="#94a3b8" font-size="11">NETWORK PACKET LOSS</text>
    <text x="975" y="55" fill="#10b981" font-size="22" font-weight="700">0.000 %</text>
    <text x="1150" y="53" fill="#34d399" font-size="11">Jitter &lt; 0.2ms</text>
  </g>

  <!-- Video Wall Grid -->
  <g transform="translate(20, 185)">
'''
    cols = 5
    tile_w = 240
    tile_h = 145
    gap_x = 15
    gap_y = 15

    cameras_data = [
        ("CAM-01", "Perimeter N-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-02", "Perimeter N-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-03", "Perimeter E-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-04", "Perimeter E-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-05", "Perimeter S-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-06", "Perimeter S-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-07", "Perimeter W-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-08", "Perimeter W-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-09", "Factory Line 1-Feed", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-10", "Factory Line 1-Stamp", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-11", "Factory Line 1-Assem", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-12", "Factory Line 2-Robot", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-13", "Factory Line 2-Weld", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-14", "Factory Line 2-QC", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-15", "High-Bay Aisle 1", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-16", "High-Bay Aisle 2", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-17", "Logistics Dock 1", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-18", "Logistics Dock 2", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-19", "Main Gate Entry LPR", "1080p 60fps", "ANPR", "5.5 Mbps", "VLAN 22", "#ec4899"),
        ("CAM-20", "Main Gate Exit LPR", "1080p 60fps", "ANPR", "5.5 Mbps", "VLAN 22", "#ec4899"),
    ]

    tile_elements = []
    for idx, data in enumerate(cameras_data):
        r = idx // cols
        c = idx % cols
        x = c * (tile_w + gap_x)
        y = r * (tile_h + gap_y)
        cam_id, name, res, codec, bw, vlan, color = data

        tile_elements.append(f'''
    <g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{tile_w}" height="{tile_h}" rx="6" fill="url(#camBox)" stroke="#222838"/>
      <rect x="0" y="0" width="{tile_w}" height="24" rx="6" fill="#1a202c"/>
      <circle cx="12" cy="12" r="4" fill="#10b981"/>
      <text x="24" y="16" fill="#f8fafc" font-size="11" font-weight="700">{cam_id} - {name}</text>
      <rect x="8" y="28" width="{tile_w - 16}" height="85" fill="#090c13" rx="4"/>
      <rect x="40" y="40" width="70" height="60" fill="none" stroke="{color}" stroke-width="1.5" stroke-dasharray="3,2"/>
      <rect x="40" y="32" width="60" height="12" fill="{color}" rx="2"/>
      <text x="44" y="41" fill="#fff" font-size="8" font-weight="700">TARGET: 98%</text>
      <text x="12" y="130" fill="#94a3b8" font-size="10">{res} | {codec} | {bw}</text>
      <rect x="180" y="118" width="50" height="16" rx="3" fill="#1e293b"/>
      <text x="185" y="130" fill="{color}" font-size="9" font-weight="700">{vlan}</text>
    </g>''')

    svg += ''.join(tile_elements)
    svg += '''
  </g>
</svg>'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def render_vms_dashboard_png(output_path):
    """Renders a pixel-perfect dark theme PNG of the VMS video wall."""
    width, height = 1300, 850
    img = Image.new("RGB", (width, height), "#06080e")
    draw = ImageDraw.Draw(img)

    font_title = get_font(FONT_SANS_BOLD, 16)
    font_sub = get_font(FONT_SANS, 11)
    font_kpi_val = get_font(FONT_SANS_BOLD, 22)
    font_kpi_lbl = get_font(FONT_SANS, 11)
    font_cam_title = get_font(FONT_SANS_BOLD, 11)
    font_cam_sub = get_font(FONT_MONO, 10)
    font_badge = get_font(FONT_SANS_BOLD, 9)

    draw.rounded_rectangle([(20, 15), (1280, 75)], radius=8, fill="#151924", outline="#272b38")
    draw.ellipse([(36, 31), (64, 59)], fill="#3b82f6")
    draw.text((45, 34), "V", fill="#ffffff", font=font_title)
    draw.text((75, 27), "VMS & AI SMART INFERENCE CONSOLE — FACTORY MATRIX (20 CHANNELS)", fill="#f8fafc", font=font_title)
    draw.text((75, 49), "Milestone Corporate / NVIDIA RTX 6000 Ada Acceleration | Continuous Recording Mode", fill="#94a3b8", font=font_sub)

    draw.rounded_rectangle([(1100, 27), (1260, 61)], radius=4, fill="#064e3b", outline="#10b981")
    draw.ellipse([(1115, 39), (1125, 49)], fill="#10b981")
    draw.text((1135, 37), "ALL 20 FEEDS LIVE", fill="#34d399", font=font_cam_title)

    kpis = [
        ("TOTAL VIDEO INGESTION", "104.00 Mbps", "0.56% 10G Bus Load", "#38bdf8"),
        ("GPU INFERENCE SPEED", "11.2 ms / frame", "TensorRT FP16", "#a855f7"),
        ("STORAGE AUTONOMY (RAID-6)", "109.9 Days", "117.87 TiB Usable", "#34d399"),
        ("NETWORK PACKET LOSS", "0.000 %", "Jitter < 0.2ms", "#10b981"),
    ]
    for idx, (label, val, note, col) in enumerate(kpis):
        x = 20 + idx * 320
        draw.rounded_rectangle([(x, 90), (x + 300, 165)], radius=6, fill="#111622", outline="#1f293d")
        draw.text((x + 15, 105), label, fill="#94a3b8", font=font_kpi_lbl)
        draw.text((x + 15, 125), val, fill=col, font=font_kpi_val)
        draw.text((x + 180, 133), note, fill="#10b981" if idx == 0 else ("#c084fc" if idx == 1 else "#34d399"), font=font_sub)

    cols = 5
    tile_w = 240
    tile_h = 145
    gap_x = 15
    gap_y = 15

    cameras_data = [
        ("CAM-01", "Perimeter N-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-02", "Perimeter N-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-03", "Perimeter E-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-04", "Perimeter E-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-05", "Perimeter S-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-06", "Perimeter S-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-07", "Perimeter W-01", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-08", "Perimeter W-02", "4K 25fps", "H.265", "6.0 Mbps", "VLAN 20", "#38bdf8"),
        ("CAM-09", "Factory Line 1-Feed", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-10", "Factory Line 1-Stamp", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-11", "Factory Line 1-Assem", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-12", "Factory Line 2-Robot", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-13", "Factory Line 2-Weld", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-14", "Factory Line 2-QC", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-15", "High-Bay Aisle 1", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-16", "High-Bay Aisle 2", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-17", "Logistics Dock 1", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-18", "Logistics Dock 2", "1080p 60fps", "H.265", "4.5 Mbps", "VLAN 21", "#f59e0b"),
        ("CAM-19", "Main Gate Entry LPR", "1080p 60fps", "ANPR", "5.5 Mbps", "VLAN 22", "#ec4899"),
        ("CAM-20", "Main Gate Exit LPR", "1080p 60fps", "ANPR", "5.5 Mbps", "VLAN 22", "#ec4899"),
    ]

    for idx, (cid, cname, res, codec, bw, vlan, col) in enumerate(cameras_data):
        r = idx // cols
        c = idx % cols
        x = 20 + c * (tile_w + gap_x)
        y = 185 + r * (tile_h + gap_y)

        draw.rounded_rectangle([(x, y), (x + tile_w, y + tile_h)], radius=6, fill="#0f131c", outline="#222838")
        draw.rounded_rectangle([(x, y), (x + tile_w, y + 24)], radius=6, fill="#1a202c")
        draw.ellipse([(x + 8, y + 8), (x + 16, y + 16)], fill="#10b981")
        draw.text((x + 22, y + 5), f"{cid} - {cname}", fill="#f8fafc", font=font_cam_title)

        draw.rounded_rectangle([(x + 8, y + 28), (x + tile_w - 8, y + 115)], radius=4, fill="#080a10")
        draw.rectangle([(x + 35, y + 42), (x + 110, y + 102)], outline=col, width=2)
        draw.rounded_rectangle([(x + 35, y + 32), (x + 95, y + 44)], radius=2, fill=col)
        draw.text((x + 38, y + 33), "TARGET: 98%", fill="#ffffff", font=font_badge)

        draw.text((x + 10, y + 124), f"{res} | {codec} | {bw}", fill="#94a3b8", font=font_cam_sub)
        draw.rounded_rectangle([(x + tile_w - 58, y + 120), (x + tile_w - 10, y + 138)], radius=3, fill="#1e293b")
        draw.text((x + tile_w - 53, y + 123), vlan, fill=col, font=font_badge)

    img.save(output_path, "PNG")

def main():
    os.makedirs("assets", exist_ok=True)
    print("Generating High-Resolution SVG Diagrams & PNG Screenshots...")

    # 1. Topology Diagrams
    generate_topology_svg("assets/topology-high-availability.svg")
    print(" -> Generated assets/topology-high-availability.svg (SVG)")

    # 2. Rack Elevation
    generate_rack_elevation_svg("assets/rack-elevation-mdf-idf.svg")
    print(" -> Generated assets/rack-elevation-mdf-idf.svg (SVG)")

    # 3. CLI Terminal Captures Data
    cisco_core_cli = [
        {"type": "cmd", "text": "SW-CORE-STK# show redundancy"},
        {"type": "out", "text": "Redundant System Information :"},
        {"type": "out", "text": "------------------------------"},
        {"type": "out", "text": "       Current Processor = Slot 1 (Active)"},
        {"type": "out", "text": "      Peer Processor     = Slot 2 (Standby Hot)"},
        {"type": "out", "text": "Redundancy Mode Current  = sso (Stateful Switchover)"},
        {"type": "out", "text": "Operating Mode Current   = sso"},
        {"type": "success", "text": "Communications Current   = Definite (Full Sync Completed)"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "SW-CORE-STK# show etherchannel summary"},
        {"type": "out", "text": "Group  Port-channel  Protocol    Ports"},
        {"type": "out", "text": "------+-------------+-----------+-----------------------------------------------"},
        {"type": "success", "text": "1      Po1(SU)        LACP        Te1/0/1(P)   Te2/0/1(P)   [IDF-1 Trunk Uplink]"},
        {"type": "success", "text": "2      Po2(SU)        LACP        Te1/0/2(P)   Te2/0/2(P)   [IDF-2 Trunk Uplink]"},
        {"type": "success", "text": "3      Po3(SU)        LACP        Te1/0/3(P)   Te2/0/3(P)   [IDF-3 Trunk Uplink]"},
        {"type": "success", "text": "10     Po10(SU)       LACP        Te1/0/10(P)  Te2/0/10(P)  [Dell PowerEdge R750xa]"},
        {"type": "success", "text": "50     Po50(SU)       LACP        Te1/0/24(P)  Te2/0/24(P)  [FortiGate 100F HA]"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "SW-CORE-STK# show ip route vrf VRF_CCTV_OT ospf"},
        {"type": "out", "text": "Routing Table: VRF_CCTV_OT"},
        {"type": "success", "text": "O*E2  0.0.0.0/0 [110/10] via 10.240.99.1, 4d18h, Vlan99"},
        {"type": "out", "text": "      10.0.0.0/8 is variably subnetted, 8 subnets, 4 masks"},
        {"type": "out", "text": "C        10.240.20.0/24 is directly connected, Vlan20 (Perimeter)"},
        {"type": "out", "text": "C        10.240.21.0/24 is directly connected, Vlan21 (Factory)"},
        {"type": "out", "text": "C        10.240.22.0/24 is directly connected, Vlan22 (ANPR)"},
        {"type": "out", "text": "C        10.240.30.0/28 is directly connected, Vlan30 (VMS-AI)"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "SW-CORE-STK# show ip arp inspection statistics vlan 20-22"},
        {"type": "out", "text": "Vlan 20: Forwarded: 142095, Dropped: 0, DHCP Drops: 0"},
        {"type": "out", "text": "Vlan 21: Forwarded: 298410, Dropped: 0, DHCP Drops: 0"},
        {"type": "success", "text": "Vlan 22: Forwarded:  48120, Dropped: 0, DHCP Drops: 0 (ZERO MITM ANOMALIES)"}
    ]

    cisco_ie_cli = [
        {"type": "cmd", "text": "SW-ACC-IDF1# show power inline"},
        {"type": "out", "text": "Available: 480.0(w)  Used: 190.0(w)  Remaining: 290.0(w)"},
        {"type": "out", "text": "Interface Admin  Oper       Power(Watts) Device              Class"},
        {"type": "out", "text": "--------- ------ ---------- ------------ ------------------- -----"},
        {"type": "success", "text": "Gi1/1     auto   on         25.5         Axis Q1715          4"},
        {"type": "success", "text": "Gi1/2     auto   on         25.5         Axis Q1715          4"},
        {"type": "success", "text": "Gi1/3     auto   on         22.0         Axis P1468-LE       4"},
        {"type": "success", "text": "Gi1/4     auto   on         22.0         Axis P1468-LE       4"},
        {"type": "success", "text": "Gi1/5     auto   on         25.5         Axis Q1715          4"},
        {"type": "success", "text": "Gi1/6     auto   on         25.5         Axis Q1715          4"},
        {"type": "success", "text": "Gi1/7     auto   on         22.0         Axis P1468-LE       4"},
        {"type": "success", "text": "Gi1/8     auto   on         22.0         Axis P1468-LE       4"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "SW-ACC-IDF1# show alarm contact"},
        {"type": "success", "text": "Contact 1: 'IDF-1 Cabinet Door Tamper' - Status: CLOSED (NORMAL)"},
        {"type": "success", "text": "Contact 2: 'Cabinet Over-Temperature Sensor' - Status: OPEN (NORMAL: 24.2C)"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "SW-ACC-IDF1# show mac address-table secure"},
        {"type": "out", "text": "Vlan    Mac Address       Type       Ports   Remaining Age(m)"},
        {"type": "out", "text": "----+-------------------+-----------+-------+-----------------"},
        {"type": "dim", "text": "20   0040.8ce1.2001      SecureSticky Gi1/1         -"},
        {"type": "dim", "text": "20   0040.8ce1.2002      SecureSticky Gi1/2         -"},
        {"type": "dim", "text": "20   0040.8ce1.2003      SecureSticky Gi1/3         -"},
        {"type": "dim", "text": "20   0040.8ce1.2004      SecureSticky Gi1/4         -"},
        {"type": "success", "text": "Total Sticky MAC Addresses: 8 locked (Maximum 1 per port enforced)"}
    ]

    fortigate_cli = [
        {"type": "cmd", "text": "FW-FG100F-HA # get system ha status"},
        {"type": "out", "text": "HA Health Status: OK"},
        {"type": "out", "text": "Model: FortiGate-100F, Mode: a-p (Active-Passive)"},
        {"type": "group", "text": "Group: 50, Name: CCTV-HA-CLUSTER"},
        {"type": "success", "text": "Primary : FW-FG100F-PRI, HA operating index = 0, Priority = 200"},
        {"type": "success", "text": "Secondary: FW-FG100F-SEC, HA operating index = 1, Priority = 100"},
        {"type": "out", "text": "Heartbeat devices:"},
        {"type": "success", "text": "    ha1: link status = UP, sync packets = 1948201"},
        {"type": "success", "text": "    ha2: link status = UP, sync packets = 1948199"},
        {"type": "out", "text": "Session pickup: Enabled (Connectionless pickup active)"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "FW-FG100F-HA # diagnose sys session stat"},
        {"type": "out", "text": "misc info:       session_count=482 setup_rate=12 exp_count=0"},
        {"type": "out", "text": "TCP sessions:    162 (RTSP / ONVIF / Management)"},
        {"type": "out", "text": "UDP sessions:    320 (RTP High-Bitrate Video Payloads)"},
        {"type": "success", "text": "Active IPS Engine Inspection: Running (0 session drops, 0 buffer overflows)"},
        {"type": "space", "text": ""},
        {"type": "cmd", "text": "FW-FG100F-HA # diagnose ips rule status"},
        {"type": "out", "text": "Active IPS Profile: IPS_INDUSTRIAL_CCTV"},
        {"type": "success", "text": "Rule 48924 (RTSP Buffer Overflow Attack): ENFORCED - BLOCK"},
        {"type": "success", "text": "Rule 36712 (ONVIF Authentication Bypass): ENFORCED - BLOCK"},
        {"type": "success", "text": "Zero Inter-Camera Lateral Traffic Detected (Policy 990: DENY)"}
    ]

    # Generate SVGs with XML escaping
    generate_terminal_svg("assets/terminal-cisco-core-verification.svg", "SW-CORE-STK (Cisco Catalyst 9300 StackWise-480) — Verification Console", cisco_core_cli)
    generate_terminal_svg("assets/terminal-ie3400-poe-verification.svg", "SW-ACC-IDF1 (Cisco IE3400-8P4S) — Industrial Access & PoE++ Status", cisco_ie_cli)
    generate_terminal_svg("assets/terminal-fortigate-ha-status.svg", "FW-FG100F-HA (Fortinet FortiGate 100F Cluster) — HA & Zero-Trust Status", fortigate_cli)
    generate_vms_dashboard_svg("assets/vms-ai-matrix-dashboard.svg")

    # Generate PNGs with Pillow
    render_terminal_png("assets/terminal-cisco-core-verification.png", "SW-CORE-STK (Cisco Catalyst 9300 StackWise-480) — Verification Console", cisco_core_cli)
    print(" -> Generated assets/terminal-cisco-core-verification.png (PNG)")

    render_terminal_png("assets/terminal-ie3400-poe-verification.png", "SW-ACC-IDF1 (Cisco IE3400-8P4S) — Industrial Access & PoE++ Status", cisco_ie_cli)
    print(" -> Generated assets/terminal-ie3400-poe-verification.png (PNG)")

    render_terminal_png("assets/terminal-fortigate-ha-status.png", "FW-FG100F-HA (Fortinet FortiGate 100F Cluster) — HA & Zero-Trust Status", fortigate_cli)
    print(" -> Generated assets/terminal-fortigate-ha-status.png (PNG)")

    render_vms_dashboard_png("assets/vms-ai-matrix-dashboard.png")
    print(" -> Generated assets/vms-ai-matrix-dashboard.png (PNG)")

    # Validate all generated SVGs with ElementTree
    print("\nValidating XML syntax of all SVGs...")
    all_valid = True
    for f in glob.glob("assets/*.svg"):
        try:
            ET.parse(f)
            print(f"  [PASS] {f}: Valid XML")
        except Exception as e:
            print(f"  [FAIL] {f}: Invalid XML -> {e}")
            all_valid = False

    if all_valid:
        print("\nALL SVG FILES ARE 100% VALID XML!")
    else:
        raise ValueError("One or more SVGs failed XML validation.")

if __name__ == "__main__":
    main()
