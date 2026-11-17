# Industrial Video Surveillance & High-Availability Network Architecture (20-Camera Factory Deployment)
*Architettura di Rete ad Alta Disponibilità e Videosorveglianza Industriale (Impianto a 20 Telecamere)*

[![Compliance: IEC 62443-3-3](https://img.shields.io/badge/IEC%2062443--3--3-Security%20Level%202%2B-blue.svg)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series)
[![Directive: NIS2](https://img.shields.io/badge/EU%20NIS2-Compliant-darkgreen.svg)](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)
[![Network Core: Cisco C9300 StackWise-480](https://img.shields.io/badge/Cisco%20Core-StackWise--480%20%7C%2010G-005073.svg)](https://www.cisco.com)
[![Access Layer: Cisco IE3400 Heavy Duty](https://img.shields.io/badge/Cisco%20IE3400-PoE%2B%2B%20%7C%20IP67%2FDIN-orange.svg)](https://www.cisco.com)
[![Firewall: Fortinet FortiGate 100F HA](https://img.shields.io/badge/FortiGate-100F%20Active--Passive%20HA-red.svg)](https://www.fortinet.com)
[![Languages: English & Italiano](https://img.shields.io/badge/Docs-Bilingual%20(EN%2FIT)-brightgreen.svg)](#)

---

## 1. Executive Summary & Architectural Philosophy / Riepilogo Esecutivo e Filosofia Architetturale

* **EN:** This project specifies an enterprise-grade, zero-trust, high-availability (HA) physical security and network infrastructure for a mission-critical 20-camera industrial manufacturing plant. Engineered for severe operational environments (intense electromagnetic interference from Variable Frequency Drives, airborne conductive dust, thermal fluctuations, and mechanical vibration), the architecture eliminates single points of failure (SPOF) through dual-homed 10G fiber uplinks, Layer-3 core switch clustering (StackWise-480), dedicated VRF micro-segmentation, non-routed storage fabrics, and deep hardware-accelerated AI video analytics. The design fully aligns with the **IEC 62443-3-3 (Security Level 2+)** industrial cybersecurity framework and the European **NIS2 Directive**.
* **IT:** Il presente progetto definisce un'infrastruttura di rete e videosorveglianza enterprise, zero-trust e ad alta disponibilità (HA) per uno stabilimento industriale manifatturiero a 20 telecamere. Progettata per resistere a condizioni ambientali estreme (interferenze elettromagnetiche generate da inverter VFD, polveri conduttive, escursioni termiche e vibrazioni meccaniche), l'architettura elimina ogni singolo punto di guasto (SPOF) grazie a uplink ridondati in fibra ottica 10G, clustering Layer-3 dello switch core (StackWise-480), micro-segmentazione VRF, storage SAN non instradabile ed elaborazione AI con accelerazione hardware. Il progetto è pienamente conforme allo standard di sicurezza **IEC 62443-3-3 (Security Level 2+)** e alla Direttiva Europea **NIS2**.

---

## 2. Physical Layer & Industrial Cabling / Livello Fisico e Cablaggio Industriale

```text
[ Camera Head (Floating/Isolated Ground) ]
                   │
  Cat6A S/FTP (Braided Braid + Foil Shielded Pairs, LSZH, max 90m)
                   │
[ IDF Shielded Patch Panel ] ─── 16mm² Copper Strap ───> [ Telecommunications Grounding Busbar (TGB) ]
                   │
[ Cisco Catalyst IE3400 (PoE++) ]
                   ║
  Dual Armored 12-Core OS2 / OM4 Fiber Trunks (Diverse Physical Conduits)
                   ║
[ MDF: Cisco Catalyst 9300 Core Stack ]
```

### 2.1 Field Connectivity & EMI Mitigation / Connettività sul Campo e Mitigazione EMI
* **EN:**
  * **Cabling Standard:** Industrial-grade **Cat6A S/FTP** (Screened/Foiled Twisted Pair), 23 AWG solid copper conductors with LSZH jacket rated for UV, oil, and flame resistance (IEC 60811-2-1).
  * **Ground Loop Prevention (IEEE 1100 / EN 50310):** Ground loops between factory building structures and IT racks are strictly mitigated by bonding cable shields **exclusively at the IDF patch panel** to the Telecommunications Grounding Busbar (TGB). Camera endpoints maintain an isolated/floating ground using POM/Teflon non-conductive mounting kits.
  * **Vibration Resistance:** High-vibration robotic and stamping cells (CAM-09 to CAM-14) utilize industrial **M12 X-Coded (IEC 61076-2-109)** IP67 connectors to prevent accidental disconnects under $30\text{g}$ mechanical shock.
* **IT:**
  * **Standard Cablaggio:** Cavi industriali **Cat6A S/FTP** (schermati singolarmente su ciascuna coppia e complessivamente con treccia di rame stagnato $\ge 85\%$), conduttori 23 AWG con guaina LSZH resistente a oli, raggi UV e fiamma (IEC 60811-2-1).
  * **Prevenzione Loop di Massa (IEEE 1100 / EN 50310):** La calza di schermatura è messa a terra **esclusivamente lato patch panel nell'armadio IDF** sulla barra equipotenziale TGB. Le telecamere sul campo adottano masse flottanti e supporti isolati in POM/Teflon per impedire correnti circolanti a 50 Hz causate da differenze di potenziale tra carpenteria metallica e sala server.
  * **Resistenza a Vibrazioni:** Le telecamere installate su linee robotizzate e presse (CAM-09 a CAM-14) adottano connettori industriali **M12 Codifica-X (IEC 61076-2-109)** IP67 per garantire tenuta meccanica fino a $30\text{g}$ di shock.

### 2.2 Fiber Optic Backbone / Dorsale in Fibra Ottica
* **EN:** 12-core armored **OS2 Single-Mode (9/125 µm)** and **OM4 Multi-Mode (50/125 µm)** trunks connect IDFs to the MDF. Dual physically diverse pathways (one overhead cable tray, one underground duct) guarantee survivability against mechanical severance. Terminated in 1U sliding patch drawers with ceramic LC-Duplex connectors.
* **IT:** Dorsali armate a 12 fibre **OS2 Monomodale (9/125 µm)** e **OM4 Multimodale (50/125 µm)** collegano ciascun IDF all'MDF. Due percorsi fisicamente separati (una canalina aerea e un cunicolo interrato) proteggono da tranciature accidentali. Terminazione su cassetti ottici 1U estraibili con bussole LC-Duplex in ceramica.

---

## 3. Hardware Bill of Materials (BOM) / Distinta Base Hardware (BOM)

| Layer / Livello | Role / Ruolo | Recommended Enterprise Hardware | Key Specifications / Specifiche Chiave | Qty |
| :--- | :--- | :--- | :--- | :--- |
| **Edge / Campo** | Perimeter & Outdoor AI Cameras | **Axis Q1715 / P1468-LE** | 4K / 8MP @ 25fps, Zipstream H.265, IK10, IP67, Deep Learning NPU (ARTPEC-8) | 8 |
| **Edge / Campo** | Production Line & Indoor Domes | **Axis P3265-LV** | 1080p @ 60fps (High-speed machinery), Starlight, Forensic WDR, IK10, IP66 | 10 |
| **Edge / Campo** | Critical Access / ANPR (Gates) | **Axis Q1700-LE** | Dedicated ANPR/LPR, 60fps high shutter, 850nm IR illuminator, License Plate AI | 2 |
| **Access / Campo**| Industrial DIN-Rail PoE++ Switches | **Cisco Catalyst IE3400-8P4S** | 8x GE PoE++ (90W 802.3bt), 4x 10G SFP+, -40°C to +75°C, Dual DC PSU, REP/ERPS | 3 |
| **Core / Centro** | Layer-3 Core Switch Stack | **Cisco Catalyst 9300-24S Stack** | 2x C9300-24S (StackWise-480 @ 480Gbps), Dual Redundant AC PSU, VRF-Lite, MACsec-256 | 2 |
| **Security** | Next-Gen Firewall (HA Pair) | **Fortinet FortiGate 100F HA** | Active-Passive FGCP Cluster, 10G SFP+ FortiLink, RTSP/ONVIF DPI, IPS > 2.6 Gbps | 2 |
| **Compute / AI** | Local VMS & AI Inference Server | **Dell PowerEdge R750xa** | Dual Intel Xeon Gold 6338, 128GB ECC RAM, NVIDIA RTX 6000 Ada (48GB), RAID-1 NVMe | 1 |
| **Storage** | Enterprise Video SAN Storage | **Dell PowerVault ME5012** | 12x 16TB Enterprise SAS-3 (RAID-6 + Hot Spare), Dual Active-Active Controller, 10G iSCSI | 1 |
| **Power (MDF)** | Online Double-Conversion UPS | **APC Smart-UPS SRT 5000VA RM** | 5kVA / 4.5kW, Online Double Conversion, SNMP/Modbus Network Card, Extended Battery Pack | 1 |
| **Power (IDF)** | Industrial DIN-Rail 24V DC-UPS | **Phoenix Contact QUINT4-UPS** | 24V DC / 20A, IQ Technology, Li-Ion Battery Module, Modbus/TCP Monitoring | 3 |

---

## 4. Network Topology & Redundancy Architecture / Topologia di Rete e Ridondanza

### 4.1 Topology Diagram / Diagramma della Topologia

```mermaid
flowchart TD
    subgraph FIELD_IDF1["IDF-1: Perimeter Enclosure (IP66)"]
        CAM1["CAM-01 to CAM-08<br>(8x Axis 4K AI Cameras)"]
        SW_IDF1["Cisco IE3400-8P4S<br>(IDF-1 Access Switch)"]
        CAM1 -->|Cat6A S/FTP PoE+| SW_IDF1
    end

    subgraph FIELD_IDF2["IDF-2: Factory Floor Enclosure (IP66)"]
        CAM2["CAM-09 to CAM-16<br>(8x Axis 1080p 60fps Domes)"]
        SW_IDF2["Cisco IE3400-8P4S<br>(IDF-2 Access Switch)"]
        CAM2 -->|Cat6A S/FTP / M12 PoE| SW_IDF2
    end

    subgraph FIELD_IDF3["IDF-3: Logistics & Gate Enclosure (IP66)"]
        CAM3["CAM-17 & 18 (Docks)<br>CAM-19 & 20 (ANPR Gates)"]
        SW_IDF3["Cisco IE3400-8P4S<br>(IDF-3 Access Switch)"]
        CAM3 -->|Cat6A S/FTP PoE/PoE+| SW_IDF3
    end

    subgraph MDF_ROOM["MDF Server Room: Core Infrastructure"]
        subgraph CORE_CLUSTER["Core Switching Fabric (StackWise-480)"]
            SW_CORE1["Cisco Catalyst 9300-24S (Master)"]
            SW_CORE2["Cisco Catalyst 9300-24S (Standby)"]
            SW_CORE1 <===>|480 Gbps StackWise Stacking Cables| SW_CORE2
        end

        subgraph STORAGE_VAULT["Isolated Storage Fabric (Non-Routed)"]
            SAN["Dell PowerVault ME5012<br>(12x 16TB SAS, RAID-6 + Spare)"]
        end

        subgraph VMS_SERVER_LAYER["VMS & Hardware AI Inference"]
            VMS["Dell PowerEdge R750xa<br>(NVIDIA RTX 6000 Ada / Milestone XProtect)"]
        end

        subgraph NGFW_CLUSTER["Zero-Trust Security Boundary"]
            FW1["FortiGate 100F (Primary Active)"]
            FW2["FortiGate 100F (Secondary Passive)"]
            FW1 <--->|FGCP Heartbeat (ha1 / ha2)| FW2
        end
    end

    subgraph SOC_ZONE["Security Operations Center (SOC)"]
        SOC_WS["SOC Viewing Workstations<br>(VLAN 50)"]
    end

    %% Fiber Uplinks to Core Stack with Cross-Switch LACP Diversity
    SW_IDF1 ===|10G Fiber Path A| SW_CORE1
    SW_IDF1 ===|10G Fiber Path B| SW_CORE2
    SW_IDF2 ===|10G Fiber Path A| SW_CORE1
    SW_IDF2 ===|10G Fiber Path B| SW_CORE2
    SW_IDF3 ===|10G Fiber Path A| SW_CORE1
    SW_IDF3 ===|10G Fiber Path B| SW_CORE2

    %% Server & Storage Dual Connections
    VMS ===|Dual 10G LACP (VLAN 30, 40, 41)| CORE_CLUSTER
    SAN ===|Dual 10G iSCSI Path A (VLAN 40)| CORE_CLUSTER
    SAN ===|Dual 10G iSCSI Path B (VLAN 41)| CORE_CLUSTER

    %% Firewall Interconnect
    CORE_CLUSTER ===|Dual 10G Transit Port-Channel| NGFW_CLUSTER
    NGFW_CLUSTER <===>|RTSPS / HTTPS API| SOC_ZONE
```

### 4.2 High-Availability Redundancy Mechanisms / Meccanismi di Ridondanza HA
* **Core Switch Layer (StackWise-480):** The two Cisco Catalyst 9300-24S units act as a single logical switch with deterministic sub-50ms Stateful Switchover (SSO) and Non-Stop Forwarding (NSF). In the event of a master switch failure, the standby switch assumes control plane ownership without dropping a single packet.
* **Industrial Access Uplinks (Dual-Homed 10G LACP):** Each IE3400 industrial access switch connects via two 10G SFP+ links: one link to Core Switch 1 and the other to Core Switch 2 in an IEEE 802.3ad LACP Port-Channel. If any fiber run or core switch unit fails, traffic immediately redirects across the surviving link.
* **Firewall Layer (FortiGate Clustering Protocol - FGCP):** Active-Passive HA cluster with dedicated dual heartbeat links (`ha1` and `ha2`). Synchronizes state tables, TCP sessions, and IPS inspection engines in real-time ($< 1\text{ s}$ failover).
* **Storage Multipathing (iSCSI MPIO):** The Dell PowerVault ME5012 active-active dual controllers interface over two isolated non-routed VLANs (40 and 41). The VMS server utilizes Asymmetric Logical Unit Access (ALUA) Round-Robin MPIO to achieve both path redundancy and load balancing.

---

## 5. Bandwidth, Storage & Compute Engineering / Ingegneria di Banda, Archiviazione e Computo

### 5.1 Ingress Bandwidth Calculations / Calcoli della Larghezza di Banda in Ingresso
* **Perimeter 4K Group (8x Axis Q1715):** $8 \times 6.0\text{ Mbps} = \mathbf{48.0\text{ Mbps}}$ sustained (Peak: $80.0\text{ Mbps}$).
* **Factory Floor 60fps Group (10x Axis P3265-LV):** $10 \times 4.5\text{ Mbps} = \mathbf{45.0\text{ Mbps}}$ sustained (Peak: $70.0\text{ Mbps}$).
* **ANPR Gate Group (2x Axis Q1700-LE):** $2 \times 5.5\text{ Mbps} = \mathbf{11.0\text{ Mbps}}$ sustained (Peak: $17.0\text{ Mbps}$).
* **Secondary Substreams (720p @ 10fps for AI grid):** $20 \times 0.9\text{ Mbps} = \mathbf{18.0\text{ Mbps}}$.
* **Total Continuous Network Ingress:** $\mathbf{122.0\text{ Mbps}}$ sustained ($\mathbf{185.0\text{ Mbps}}$ burst peak).
* **Uplink Saturation Analysis:** Over a 10Gbps ($10,000\text{ Mbps}$) backbone, average bus saturation is **$0.48\%$ to $0.56\%$**, providing massive immunity against packet jitter, micro-burst buffer drops, and frame corruption.

### 5.2 Storage Capacity Sizing & RAID-6 Reliability
* **Daily Ingestion Rate ($S_{\text{day}}$):**
  $$\text{Storage Rate} = \frac{104.0\text{ Mbps}}{8} \times 3600\text{ s} \times 24\text{ h} \times 1.05\text{ (metadata)} = \mathbf{1.179\text{ TB / day}}$$
* **Physical SAN Specification:** Dell PowerVault ME5012 with 12x 16 TB SAS Enterprise 7.2K RPM HDDs.
  * Array: RAID-6 (9 Data Disks + 2 Parity Disks + 1 Dedicated Global Hot-Spare).
  * Raw Storage: $9 \times 16\text{ TB} = 144\text{ TB}$.
  * Net Usable Volume (accounting for binary base-2 conversion and 10% snapshot reserve): $\mathbf{117.87\text{ TiB}}$.
* **Retention Autonomy:**
  $$\text{Autonomy} = \frac{117.87\text{ TiB}}{1.073\text{ TiB/day}} = \mathbf{109.9\text{ Days of Continuous 24/7 Recording}}$$
  *Exceeds the 30-day regulatory requirement by $366\%$, providing over 3 months of forensic retention.*

---

## 6. Network Segmentation & IP Addressing Plan / Segmentazione di Rete e Indirizzamento IP

| VLAN ID | Name / Nome | Subnet (CIDR) | Gateway | Role & Scope (EN/IT) |
| :---: | :--- | :--- | :--- | :--- |
| **10** | `OOBM-MGMT` | `10.240.10.0/24` | `10.240.10.1` | Out-of-band management for switches, UPS, PDU, iDRAC / Gestione OOBM |
| **20** | `CCTV-PERIMETER` | `10.240.20.0/24` | `10.240.20.1` | 8x Perimeter 4K AI Cameras on IDF-1 (CAM-01 to CAM-08) |
| **21** | `CCTV-FACTORY` | `10.240.21.0/24` | `10.240.21.1` | 10x Industrial 60fps Domes on IDF-2 & IDF-3 (CAM-09 to CAM-18) |
| **22** | `CCTV-ANPR-GATE` | `10.240.22.0/24` | `10.240.22.1` | 2x Dedicated ANPR/LPR Gate Cameras on IDF-3 (CAM-19 & CAM-20) |
| **30** | `VMS-AI-CORE` | `10.240.30.0/28` | `10.240.30.1` | Dell PowerEdge VMS Server & AI Analytics Engine |
| **40** | `STORAGE-SAN-A` | `10.240.40.0/28` | *Non-Routed* | Dedicated iSCSI Fabric A (ME5012 Controller A - MTU 9000) |
| **41** | `STORAGE-SAN-B` | `10.240.41.0/28` | *Non-Routed* | Dedicated iSCSI Fabric B (ME5012 Controller B - MTU 9000) |
| **50** | `SOC-CLIENTS` | `10.240.50.0/26` | `10.240.50.1` | Security Operations Center Workstations / Postazioni Operatore |
| **99** | `CORE-FW-TRANSIT`| `10.240.99.0/29` | `10.240.99.1` | L3 Routed Transit Link between Core Stack & FortiGate HA |
| **666**| `QUARANTINE` | `192.0.2.0/24` | `192.0.2.1` | Blackhole & 802.1X Unauthorized Isolation VLAN |

*For the complete port-by-port mapping of all 20 cameras, refer to [docs/ip-addressing-and-vlan-plan.md](docs/ip-addressing-and-vlan-plan.md).*

---

## 7. Quality of Service (QoS) & Traffic Engineering / Qualità del Servizio (QoS)

*EN:* Video surveillance streams require guaranteed low jitter and deterministic queue scheduling to prevent video frame drops. The network enforces Modular QoS CLI (MQC) based on Differentiated Services Code Point (DSCP) classification:
1. **Critical Alarms & PTZ Telemetry:** Marked as **DSCP EF (Expedited Forwarding - 46)**. Mapped to the hardware Priority Queue (PQ / Priority Level 1) with Strict Priority scheduling.
2. **Primary RTSP Video Payload:** Marked as **DSCP AF41 (Assured Forwarding - 34)**. Assigned guaranteed Class-Based Weighted Fair Queuing (CBWFQ) receiving $70\%$ of available link bandwidth with Weighted Random Early Detection (WRED).
3. **Secondary Substreams & Remote View:** Marked as **DSCP AF42 (36)**.
4. **Out-of-band Management (SSH, SNMPv3, NTP):** Marked as **DSCP CS2 (16)** with $10\%$ reserved bandwidth.
5. **Best Effort / Quarantine:** Default class mapped to low-priority queue.

*IT:* I flussi di videosorveglianza richiedono jitter minimo e scheduling deterministico per evitare la perdita di frame. La rete applica policy QoS basate sui valori DSCP: priorità assoluta (Strict Priority EF) per allarmi critici e telemetria PTZ, banda garantita al 70% con WRED per i flussi video primari (AF41), e banda dedicata al 10% per il traffico di gestione (CS2).

---

## 8. Layer-2 & Layer-3 Zero-Trust Security / Sicurezza Zero-Trust Layer-2 e Layer-3

```text
[ Camera Port (Gi1/0/1) ]
         │
         ├── 802.1X / MAB (EAP-TLS Certificate Authentication + RADIUS Profiling)
         ├── DHCP Snooping (Untrusted Port -> Validates against DHCP Server IP 10.240.30.10)
         ├── Dynamic ARP Inspection (DAI -> Drops gratuitous ARP / Man-in-the-Middle)
         ├── IP Source Guard (IPSG -> Blocks IP spoofing via MAC-IP Binding Table)
         ├── Port Security (Max MAC: 1, Violation: Restrict / Err-disable)
         └── Storm Control (Broadcast: 0.5%, Multicast: 1.0% -> Auto-shutdown)
```

1. **IEEE 802.1X with MAC Authentication Bypass (MAB):** Cameras authenticate using EAP-TLS client certificates stored inside the camera's hardware cryptographic element (TPM 2.0 / Axis Edge Vault). Unauthenticated devices connecting to any patch point are automatically relegated to Quarantine VLAN 666.
2. **Anti-Spoofing Triad (DHCP Snooping + DAI + IP Source Guard):** Hardware-enforced validation prevents rogue DHCP servers, ARP cache poisoning, and unauthorized static IP hijacking.
3. **MACsec Link Encryption (IEEE 802.1AE):** Inter-switch 10G SFP+ fiber trunks running across the plant floor are encrypted in hardware using **256-bit AES-GCM MACsec**, eliminating eavesdropping or physical optical taps.
4. **Next-Generation Firewall Inspection (FortiGate 100F):**
   * **Conduit 1 (CCTV to VMS):** Permits strictly TCP 554 (RTSP), UDP 16384-32767 (RTP), TCP 80/443 (ONVIF) with Deep Packet Inspection (DPI) and IPS attack signatures.
   * **Conduit 2 (SOC to VMS):** Operators access the VMS web client and streaming API; direct connections from operator workstations to cameras are blocked.
   * **Micro-segmentation Enforcement:** Camera-to-camera lateral movement is completely blocked at both Layer-2 (Private VLAN / Port isolation) and Layer-3 (Firewall policy). Outbound traffic to the Internet is strictly prohibited (air-gapped operation).

---

## 9. Power Architecture & Industrial PoE++ Sizing / Architettura Elettrica e Bilancio PoE

| Location | Switch Device | Connected Cameras | Total PoE Load | Available PoE Budget | Utilization | Backup Power Infrastructure |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IDF-1** | Cisco IE3400-8P4S | 8x Axis Q1715 / P1468-LE | **190.0 W** | 480.0 W | **39.58%** | Phoenix Contact QUINT4 24V DC-UPS (Li-Ion) |
| **IDF-2** | Cisco IE3400-8P4S | 8x Axis P3265-LV | **103.2 W** | 480.0 W | **21.50%** | Phoenix Contact QUINT4 24V DC-UPS (Li-Ion) |
| **IDF-3** | Cisco IE3400-8P4S | 4x Axis P3265-LV & Q1700-LE | **76.8 W** | 480.0 W | **16.00%** | Phoenix Contact QUINT4 24V DC-UPS (Li-Ion) |
| **MDF** | C9300 Stack & Servers | Core, Firewall, VMS, SAN | **1,850.0 W** | 4,500.0 W | **41.11%** | APC Smart-UPS SRT 5000VA RM Double-Conversion |

* **EN:** All industrial switches are supplied with redundant dual 24-54V DC inputs backed by Phoenix Contact QUINT4 DC-UPS modules providing 45 minutes of autonomous battery buffer. The central MDF rack is protected by an Online Double-Conversion APC SRT 5000VA UPS delivering clean, isolated power free of industrial factory surges, brownouts, and harmonics.
* **IT:** Tutti gli switch industriali sono alimentati con ingressi DC 24-54V ridondati supportati da moduli DC-UPS Phoenix Contact QUINT4 con batterie agli ioni di litio per un'autonomia di 45 minuti. L'armadio centrale MDF è protetto da un UPS On-line a Doppia Conversione APC SRT 5000VA che filtra armoniche, sovratensioni e microinterruzioni tipiche degli ambienti industriali.

---

## 10. Standards & Regulatory Compliance Matrix / Matrice di Conformità Normativa

| Standard / Directive | Mandated Requirement | Architectural Implementation in this Project |
| :--- | :--- | :--- |
| **IEC 62443-3-3: SR 1.1** | Human User Identification and Authentication | Centralized RADIUS/TACACS+ with multi-factor authentication (MFA) on FortiGate and VMS. |
| **IEC 62443-3-3: SR 1.2** | Software Process and Device Identification | 802.1X EAP-TLS device authentication with TPM-backed hardware certificates and MAB fallback. |
| **IEC 62443-3-3: SR 3.1** | Communication Integrity & Confidentiality | MACsec-256 on fiber trunks; TLS 1.3 encryption on VMS web/API; SSHv2 with modern ciphers. |
| **IEC 62443-3-3: SR 5.1** | Network Segmentation (Zones and Conduits) | VRF-Lite micro-segmentation, isolated non-routed iSCSI storage, FortiGate 100F HA NGFW conduits. |
| **IEC 62443-3-3: SR 7.6** | Network and Security Configuration Monitoring | SNMPv3 AuthPriv traps, centralized Syslog to SIEM (10.240.10.35), NTP synchronization. |
| **EU NIS2 Directive** | Supply Chain & Infrastructure Resilience | Dual-homed 10G uplinks, StackWise-480 SSO, active-passive NGFW, RAID-6 SAN with hot-spare. |
| **IEEE 1100 / EN 50310** | Telecommunications Grounding & Bonding | Single-point shield grounding at IDF patch panel, floating camera mounts to prevent VFD ground loops. |

---

## 11. Project Repository Structure / Struttura del Repository

```text
PROGETTO-2--industrial-cctv-network-architecture/
├── README.md                                 # Master Architectural Blueprint (EN & IT)
├── docs/
│   ├── ip-addressing-and-vlan-plan.md        # Comprehensive 20-camera IP, subnet & port mapping
│   ├── bandwidth-storage-calculations.md     # Mathematical formulas, bitrates, RAID-6 & retention
│   ├── physical-cabling-and-emi-guide.md     # Industrial Cat6A S/FTP, M12, fiber, grounding guide
│   └── cybersecurity-iec62443-nis2.md        # Zero-trust microsegmentation, IEC 62443 & NIS2 framework
├── configs/
│   ├── cisco-cat9300-core-stack.cfg          # Cisco Catalyst 9300 StackWise-480 production config
│   ├── cisco-ie3400-idf1-perimeter.cfg       # Cisco IE3400-8P4S config (IDF-1: Perimeter AI cameras)
│   ├── cisco-ie3400-idf2-production.cfg      # Cisco IE3400-8P4S config (IDF-2: Factory floor 60fps)
│   ├── cisco-ie3400-idf3-logistics.cfg       # Cisco IE3400-8P4S config (IDF-3: Logistics & ANPR gates)
│   └── fortigate-ha-cluster.conf             # FortiGate 100F FGCP HA, zones, policies, IPS profile
└── scripts/
    └── verify_network.py                     # Python automated verification & sizing test suite
```

---

## 12. Verification & Validation / Verifica e Collaudo

To validate the network sizing, PoE budgets, bandwidth saturation, and storage retention autonomy, run the verification script:

```bash
python scripts/verify_network.py
```

### Expected Output Summary / Riepilogo dell'Output Atteso:
* **Camera Count Audit:** 20/20 Cameras validated across IDF-1, IDF-2, and IDF-3.
* **PoE Utilization:**
  * IDF-1: $190.0\text{ W} / 480.0\text{ W}$ ($39.58\%$) - Status: OPTIMAL.
  * IDF-2: $103.2\text{ W} / 480.0\text{ W}$ ($21.50\%$) - Status: OPTIMAL.
  * IDF-3: $76.8\text{ W} / 480.0\text{ W}$ ($16.00\%$) - Status: OPTIMAL.
* **Backbone Ingress Bandwidth:** $104.0\text{ Mbps}$ sustained ($122.0\text{ Mbps}$ with substreams), resulting in $<0.56\%$ uplink saturation on all 10G links.
* **Storage Autonomy:** Effective usable volume of **117.87 TiB** yields **109.9 Days of continuous 24/7 video recording**, fully surpassing the mandatory 30-day compliance threshold.
