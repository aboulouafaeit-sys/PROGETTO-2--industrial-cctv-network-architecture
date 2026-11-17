# Network Segmentation, VLAN & IP Addressing Plan
## Piano di Segmentazione di Rete, VLAN e Indirizzamento IP

---

### 1. Architectural Overview / Panoramica Architetturale

*EN:* In accordance with zero-trust network principles and industrial cybersecurity guidelines (IEC 62443-3-3), the camera and physical security infrastructure is strictly segregated into dedicated logical segments (VLANs) isolated by Layer-3 routing boundaries and Next-Generation Firewall (NGFW) policy enforcement. No direct east-west communications are permitted between camera access segments and external or corporate enterprise networks.

*IT:* In conformità ai principi di rete zero-trust e alle linee guida di sicurezza informatica industriale (IEC 62443-3-3), l'infrastruttura di videosorveglianza e sicurezza fisica è rigorosamente segregata in segmenti logici dedicati (VLAN) isolati da confini di routing Layer-3 e dall'applicazione di policy da parte del Next-Generation Firewall (NGFW). Non è consentita alcuna comunicazione diretta est-ovest tra i segmenti di accesso delle telecamere e le reti aziendali o esterne.

---

### 2. VLAN Allocation Schema / Schema di Assegnazione delle VLAN

| VLAN ID | Name / Nome VLAN | Subnet (CIDR) | Default Gateway | Purpose & Scope (EN) | Scopo e Ambito (IT) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **10** | `OOBM-MGMT` | `10.240.10.0/24` | `10.240.10.1` | Out-of-band management for switches, UPS, PDU, iDRAC | Gestione out-of-band per switch, UPS, PDU, iDRAC |
| **20** | `CCTV-PERIMETER` | `10.240.20.0/24` | `10.240.20.1` | 8x Perimeter & Outdoor AI 4K cameras (IDF-1) | 8x Telecamere AI 4K perimetrali ed esterne (IDF-1) |
| **21** | `CCTV-FACTORY` | `10.240.21.0/24` | `10.240.21.1` | 10x Industrial High-Speed Domes 60fps (IDF-2) | 10x Dome industriali alta velocità 60fps (IDF-2) |
| **22** | `CCTV-ANPR-GATE` | `10.240.22.0/24` | `10.240.22.1` | 2x Automatic Number Plate Recognition (IDF-3) | 2x Telecamere lettura targhe e varchi (IDF-3) |
| **30** | `VMS-AI-CORE` | `10.240.30.0/28` | `10.240.30.1` | Dell PowerEdge VMS & AI Inference Nodes | Server VMS ed elaborazione AI Dell PowerEdge |
| **40** | `STORAGE-SAN-A` | `10.240.40.0/28` | Non-routed (L2) | Dedicated iSCSI Subnet A (Controller A / Fabric 1) | Sottorete iSCSI A dedicata (Controller A / Fabric 1) |
| **41** | `STORAGE-SAN-B` | `10.240.41.0/28` | Non-routed (L2) | Dedicated iSCSI Subnet B (Controller B / Fabric 2) | Sottorete iSCSI B dedicata (Controller B / Fabric 2) |
| **50** | `SOC-CLIENTS` | `10.240.50.0/26` | `10.240.50.1` | Security Operation Center viewing workstations | Postazioni operatore e visualizzazione del SOC |
| **99** | `CORE-FW-TRANSIT`| `10.240.99.0/29` | `10.240.99.1` | Routed transit link between Core Stack & NGFW HA | Collegamento di transito instradato tra Core e NGFW |
| **666** | `QUARANTINE` | `192.0.2.0/24` | `192.0.2.1` | Blackhole & 802.1X unauthorized device isolation | Blackhole e isolamento dispositivi 802.1X non autorizzati |

---

### 3. Comprehensive Device Inventory & Port Mapping (20 Cameras)
#### Inventario Completo dei Dispositivi e Mappatura Porte (20 Telecamere)

| Cam ID | Hostname | Model | Switch ID | Switch Port | Patch ID | Location / Field Zone | IP Address | MAC Address (OUI: Axis) | PoE Class | Wattage | VLAN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CAM-01** | `CAM-PRM-N01` | Axis Q1715 | IDF-1 | Gi1/0/1 | PP1-P01 | North Perimeter - Sector A | `10.240.20.11` | `00:40:8C:E1:20:01` | PoE+ (Cl.4) | 25.5 W | 20 |
| **CAM-02** | `CAM-PRM-N02` | Axis Q1715 | IDF-1 | Gi1/0/2 | PP1-P02 | North Perimeter - Sector B | `10.240.20.12` | `00:40:8C:E1:20:02` | PoE+ (Cl.4) | 25.5 W | 20 |
| **CAM-03** | `CAM-PRM-E01` | Axis P1468-LE | IDF-1 | Gi1/0/3 | PP1-P03 | East Perimeter - Fence | `10.240.20.13` | `00:40:8C:E1:20:03` | PoE+ (Cl.4) | 22.0 W | 20 |
| **CAM-04** | `CAM-PRM-E02` | Axis P1468-LE | IDF-1 | Gi1/0/4 | PP1-P04 | East Perimeter - Substation | `10.240.20.14` | `00:40:8C:E1:20:04` | PoE+ (Cl.4) | 22.0 W | 20 |
| **CAM-05** | `CAM-PRM-S01` | Axis Q1715 | IDF-1 | Gi1/0/5 | PP1-P05 | South Perimeter - Sector A | `10.240.20.15` | `00:40:8C:E1:20:05` | PoE+ (Cl.4) | 25.5 W | 20 |
| **CAM-06** | `CAM-PRM-S02` | Axis Q1715 | IDF-1 | Gi1/0/6 | PP1-P06 | South Perimeter - Sector B | `10.240.20.16` | `00:40:8C:E1:20:06` | PoE+ (Cl.4) | 25.5 W | 20 |
| **CAM-07** | `CAM-PRM-W01` | Axis P1468-LE | IDF-1 | Gi1/0/7 | PP1-P07 | West Perimeter - Loading Bay | `10.240.20.17` | `00:40:8C:E1:20:07` | PoE+ (Cl.4) | 22.0 W | 20 |
| **CAM-08** | `CAM-PRM-W02` | Axis P1468-LE | IDF-1 | Gi1/0/8 | PP1-P08 | West Perimeter - Waste Area | `10.240.20.18` | `00:40:8C:E1:20:08` | PoE+ (Cl.4) | 22.0 W | 20 |
| **CAM-09** | `CAM-IND-L01` | Axis P3265-LV | IDF-2 | Gi1/0/1 | PP2-P01 | Production Line 1 - Feeding | `10.240.21.11` | `00:40:8C:E1:21:01` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-10** | `CAM-IND-L02` | Axis P3265-LV | IDF-2 | Gi1/0/2 | PP2-P02 | Production Line 1 - Stamping | `10.240.21.12` | `00:40:8C:E1:21:02` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-11** | `CAM-IND-L03` | Axis P3265-LV | IDF-2 | Gi1/0/3 | PP2-P03 | Production Line 1 - Assembly | `10.240.21.13` | `00:40:8C:E1:21:03` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-12** | `CAM-IND-L04` | Axis P3265-LV | IDF-2 | Gi1/0/4 | PP2-P04 | Production Line 2 - Robot Cell | `10.240.21.14` | `00:40:8C:E1:21:04` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-13** | `CAM-IND-L05` | Axis P3265-LV | IDF-2 | Gi1/0/5 | PP2-P05 | Production Line 2 - Welding | `10.240.21.15` | `00:40:8C:E1:21:05` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-14** | `CAM-IND-L06` | Axis P3265-LV | IDF-2 | Gi1/0/6 | PP2-P06 | Production Line 2 - Quality Check | `10.240.21.16` | `00:40:8C:E1:21:06` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-15** | `CAM-IND-WR1` | Axis P3265-LV | IDF-2 | Gi1/0/7 | PP2-P07 | Warehouse Aisle 1 (Forklifts) | `10.240.21.17` | `00:40:8C:E1:21:07` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-16** | `CAM-IND-WR2` | Axis P3265-LV | IDF-2 | Gi1/0/8 | PP2-P08 | Warehouse Aisle 2 (High Bay) | `10.240.21.18` | `00:40:8C:E1:21:08` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-17** | `CAM-IND-WR3` | Axis P3265-LV | IDF-3 | Gi1/0/1 | PP3-P01 | Logistics Shipping Dock 1 | `10.240.21.19` | `00:40:8C:E1:21:09` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-18** | `CAM-IND-WR4` | Axis P3265-LV | IDF-3 | Gi1/0/2 | PP3-P02 | Logistics Shipping Dock 2 | `10.240.21.20` | `00:40:8C:E1:21:10` | PoE (Cl.3) | 12.9 W | 21 |
| **CAM-19** | `CAM-LPR-G01` | Axis Q1700-LE | IDF-3 | Gi1/0/3 | PP3-P03 | Main Gate Entry ANPR/LPR | `10.240.22.11` | `00:40:8C:E1:22:01` | PoE+ (Cl.4) | 25.5 W | 22 |
| **CAM-20** | `CAM-LPR-G02` | Axis Q1700-LE | IDF-3 | Gi1/0/4 | PP3-P04 | Main Gate Exit ANPR/LPR | `10.240.22.12` | `00:40:8C:E1:22:02` | PoE+ (Cl.4) | 25.5 W | 22 |

---

### 4. Infrastructure & Server Node Addressing
#### Indirizzamento dei Nodi Server e di Infrastruttura

| Device Name / Hostname | Hardware Model | IP Address | Subnet Mask | Default Gateway | Function / Description (EN/IT) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `SW-CORE-STK-01` | Cisco C9300-24S (Sw1) | `10.240.10.2` | `255.255.255.0` | `10.240.10.1` | Core Stack Master OOBM Interface |
| `SW-CORE-STK-02` | Cisco C9300-24S (Sw2) | `10.240.10.3` | `255.255.255.0` | `10.240.10.1` | Core Stack Standby OOBM Interface |
| `SW-ACC-IDF1` | Cisco IE3400-8P4S | `10.240.10.11` | `255.255.255.0` | `10.240.10.1` | Industrial Switch IDF-1 OOBM Interface |
| `SW-ACC-IDF2` | Cisco IE3400-8P4S | `10.240.10.12` | `255.255.255.0` | `10.240.10.1` | Industrial Switch IDF-2 OOBM Interface |
| `SW-ACC-IDF3` | Cisco IE3400-8P4S | `10.240.10.13` | `255.255.255.0` | `10.240.10.1` | Industrial Switch IDF-3 OOBM Interface |
| `SRV-VMS-AI-01` | Dell PowerEdge R750xa | `10.240.30.10` | `255.255.255.240`| `10.240.30.1` | Primary VMS & Hardware AI Inference Engine |
| `SRV-VMS-AI-01-IDRAC` | Dell iDRAC9 Enterprise| `10.240.10.30` | `255.255.255.0` | `10.240.10.1` | Server Out-of-band Remote Console |
| `SAN-VAULT-CTRL-A` | Dell PowerVault ME5012 | `10.240.40.10` | `255.255.255.240`| Non-routed | Storage Controller A - 10G iSCSI Path 1 |
| `SAN-VAULT-CTRL-B` | Dell PowerVault ME5012 | `10.240.41.10` | `255.255.255.240`| Non-routed | Storage Controller B - 10G iSCSI Path 2 |
| `SAN-VAULT-MGMT` | Dell ME5012 Management | `10.240.10.40` | `255.255.255.0` | `10.240.10.1` | Storage Chassis Out-of-band Web GUI / CLI |
| `UPS-MDF-APC5000` | APC Smart-UPS SRT 5kVA | `10.240.10.50` | `255.255.255.0` | `10.240.10.1` | MDF Rack Central UPS SNMP/Modbus card |
| `FW-FG100F-PRI` | Fortinet FortiGate 100F| `10.240.99.1` | `255.255.255.248`| ISP Next-Hop | Primary Active Firewall HA Node |
| `FW-FG100F-SEC` | Fortinet FortiGate 100F| `10.240.99.2` | `255.255.255.248`| ISP Next-Hop | Secondary Passive Firewall HA Node |

---

### 5. IP Routing & Gateway Architecture / Architettura di Routing e Gateway

*EN:* Inter-VLAN routing for video surveillance streams and management traffic is centralized on the **Cisco Catalyst 9300 Stack** using VRF-Lite (`VRF_CCTV_OT`).
The default route (`0.0.0.0/0`) inside `VRF_CCTV_OT` points to the FortiGate HA Cluster VIP (`10.240.99.1`). Storage subnets (`VLAN 40` & `VLAN 41`) are completely non-routable: no SVI (Switched Virtual Interface) exists on the switch or firewall, preventing external exposure and enforcing strict iSCSI layer-2 encapsulation.

*IT:* L'instradamento inter-VLAN per i flussi di videosorveglianza e il traffico di gestione è centralizzato sullo stack **Cisco Catalyst 9300** tramite VRF-Lite (`VRF_CCTV_OT`).
La route di default (`0.0.0.0/0`) all'interno della `VRF_CCTV_OT` punta al VIP del cluster FortiGate HA (`10.240.99.1`). Le sottoreti di storage (`VLAN 40` e `VLAN 41`) sono rigorosamente non instradabili: nessuna SVI (Switched Virtual Interface) è configurata sullo switch o sul firewall, prevenendo qualsiasi esposizione esterna e imponendo l'incapsulamento puro a Layer-2 per iSCSI.
