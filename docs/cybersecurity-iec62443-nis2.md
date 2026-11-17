# Industrial Cybersecurity, Zero-Trust & IEC 62443 / NIS2 Compliance
## Cybersicurezza Industriale, Zero-Trust e Conformità IEC 62443 / NIS2

---

### 1. Regulatory Framework & Standards Alignment / Quadro Normativo e Standard

*EN:* The physical security and CCTV infrastructure is engineered to comply with the European **NIS2 Directive (EU 2022/2555)** for critical industrial entities and aligns with the **IEC 62443-3-3** standard (Security for industrial automation and control systems — System security requirements and security levels), targeting **Security Level 2 (SL-2)** with SL-3 enhancements for boundary protection.

*IT:* L'infrastruttura di sicurezza fisica e videosorveglianza è progettata per soddisfare i requisiti della Direttiva Europea **NIS2 (UE 2022/2555)** per le entità industriali essenziali ed è allineata allo standard **IEC 62443-3-3** (Sicurezza per i sistemi di automazione e controllo industriale — Requisiti di sicurezza dei sistemi e livelli di sicurezza), con target **Security Level 2 (SL-2)** e potenziamenti SL-3 per la protezione perimetrale.

---

### 2. IEC 62443 Zones and Conduits Architecture / Architettura Zone e Condotti

```mermaid
flowchart TD
    subgraph ZONE_1["Zone 1: CCTV Ingestion Zone (Edge Cameras)"]
        CAM1["8x Perimeter Cameras (VLAN 20)"]
        CAM2["10x Factory Floor Cameras (VLAN 21)"]
        CAM3["2x ANPR Gate Cameras (VLAN 22)"]
    end

    subgraph CONDUIT_1["Conduit A: Layer-2/3 Segregated Uplinks + 802.1X + QoS"]
        IE_SW["Cisco IE3400 Industrial Switches"]
    end

    subgraph ZONE_CORE["Core Infrastructure Zone"]
        CORE["Cisco Catalyst 9300 Stack (VRF_CCTV_OT)"]
    end

    subgraph CONDUIT_2["Conduit B: Next-Gen Firewall (Deep Packet Inspection)"]
        NGFW["FortiGate 100F HA Cluster (RTSP/ONVIF DPI + IPS)"]
    end

    subgraph ZONE_2["Zone 2: VMS & AI Analytics Core"]
        VMS["Dell PowerEdge R750xa (VMS & AI Inference - VLAN 30)"]
    end

    subgraph ZONE_3["Zone 3: Storage Vault (Isolated SAN)"]
        SAN["Dell PowerVault ME5012 (iSCSI MPIO - VLAN 40 & 41)"]
    end

    subgraph ZONE_4["Zone 4: Security Operations Center (SOC)"]
        SOC["SOC Monitoring Workstations (VLAN 50)"]
    end

    ZONE_1 --> CONDUIT_1 --> ZONE_CORE
    ZONE_CORE <--> CONDUIT_2
    CONDUIT_2 <--> ZONE_2
    ZONE_2 <-->|Dual 10G iSCSI (Non-Routable)| ZONE_3
    CONDUIT_2 <--> ZONE_4
```

* **Zone 1 (Field Ingestion):** Untrusted physical plant area where physical tampering with cameras or cables is possible. Ports locked down with 802.1X/MAB, DAI, and DHCP snooping.
* **Zone 2 (VMS & AI Compute):** Trusted server segment hosting the video management system and hardware-accelerated AI video processing.
* **Zone 3 (Storage Vault):** Non-routable Layer-2 SAN network. Access is restricted strictly to the VMS server via dual dedicated iSCSI VLANs.
* **Zone 4 (SOC & Clients):** Operator viewing zone. Workstations can only query the VMS API over HTTPS and stream processed video over RTSPS. Direct access to cameras is blocked.
* **Conduits:** All inter-zone flows traverse the FortiGate 100F HA cluster with full Layer-7 protocol inspection (RTSP, ONVIF, HTTPS) and IPS signatures active.

---

### 3. Layer 2 Access Security & Network Access Control (NAC)
#### Sicurezza di Accesso Layer 2 e Controllo Accessi di Rete (NAC)

#### 3.1 802.1X / MAC Authentication Bypass (MAB)
* Every camera port is configured for IEEE 802.1X port authentication.
* Cameras with hardware TPM / Secure Element (e.g., Axis Edge Vault) authenticate using EAP-TLS and client digital certificates issued by the internal enterprise PKI.
* Devices not supporting EAP-TLS use **MAC Authentication Bypass (MAB)** validated against Cisco ISE / FreeRADIUS, enriched with LLDP and DHCP profiling attributes (OUI check, DHCP option 60 Vendor Class Identifier).
* Unauthorized devices connecting to any camera drop are placed into **Quarantine VLAN 666** with zero network reachability, triggering an immediate SNMPv3 security alert.

#### 3.2 Port Security & Anti-Spoofing Triad
* **DHCP Snooping:** Active on all camera VLANs. All access switch ports facing cameras are configured as untrusted (`no ip dhcp snooping trust`). Switch inspects DHCP messages and builds the DHCP binding database.
* **Dynamic ARP Inspection (DAI):** Uses the DHCP snooping database to validate ARP packets in hardware. Gratuitous ARP poisoning or Man-in-the-Middle (MitM) attempts are dropped.
* **IP Source Guard (IPSG):** Blocks IP spoofing by matching traffic against IP/MAC/Port bindings. Unauthorized static IP injection is blocked at the physical port level.
* **Port Security:** Max MAC count set to `1` per port (`switchport port-security maximum 1`). Violation mode set to `restrict` or `shutdown` (`err-disable`), preventing MAC flooding and rogue switch attachment.

---

### 4. Switch-to-Switch Link Encryption: MACsec (IEEE 802.1AE)
#### Crittografia dei Collegamenti Switch: MACsec (IEEE 802.1AE)

*EN:* To prevent wiretapping or eavesdropping on optical fiber trunks passing through harsh, unmonitored factory plant spaces, all 10G SFP+ links between the Industrial Access Switches (IE3400) and the Core Switch Stack (Catalyst 9300) are protected by line-rate **MACsec (IEEE 802.1AE) with 256-bit AES-GCM encryption**.
MACsec encrypts all Layer-2 frames (including Ethernet headers, 802.1Q tags, and LLDP) with zero performance penalty and microsecond-level latency.

*IT:* Per impedire intercettazioni (wiretapping) o manomissioni sulle dorsali in fibra ottica che attraversano reparti di produzione non presidiati, tutti i collegamenti 10G SFP+ tra gli switch di accesso industriali (IE3400) e il Core Switch Stack (Catalyst 9300) sono protetti da **MACsec (IEEE 802.1AE) con crittografia hardware AES-GCM a 256 bit** a velocità di linea (line-rate).

---

### 5. Next-Generation Firewall (NGFW) Zero-Trust Inspection Policies
#### Politiche Zero-Trust e Ispezione del Firewall Next-Gen (NGFW)

| Policy ID | Source Zone | Destination Zone | Service / Protocol | Action | Security Profiles Applied | Description (EN/IT) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POL-01** | `ZONE_CCTV` | `ZONE_VMS` | `TCP/554` (RTSP), `TCP/80,443` (ONVIF), `UDP/RTP` | **ALLOW** | IPS Industrial, RTSP Deep Inspection, Anti-Botnet | Cameras streaming to VMS / Telecamere inviano flussi al VMS |
| **POL-02** | `ZONE_SOC` | `ZONE_VMS` | `TCP/443` (VMS Web/API), `TCP/7563` (Milestone/Genetec) | **ALLOW** | SSL Deep Inspection, IPS Enterprise, AV | SOC operators accessing VMS / Operatori accedono al VMS |
| **POL-03** | `ZONE_MGMT` | `ALL_ZONES` | `TCP/22` (SSH), `UDP/161` (SNMPv3), `UDP/123` (NTP) | **ALLOW** | Admin Authentication, MFA, Bastion Proxy | Centralized OOBM / Gestione centralizzata out-of-band |
| **POL-04** | `ZONE_CCTV` | `INTERNET` | ANY | **DENY** | Threat Log + Syslog Alert to SIEM | Strict block: Zero internet outbound / Blocco totale verso Internet |
| **POL-05** | `ZONE_CCTV` | `ZONE_CCTV` | ANY | **DENY** | Threat Log | Micro-segmentation: No lateral movement / Nessun movimento laterale |
| **POL-06** | `ANY` | `ZONE_STORAGE` | ANY | **DENY** | Storage is strictly isolated L2 iSCSI / Storage SAN isolato |

---

### 6. Cryptographic Hardening & Key Management
#### Hardening Crittografico e Gestione delle Chiavi

1. **Protocol Hardening:**
   * Disable Telnet, HTTP, FTP, TFTP, and SNMPv1/v2c across all network nodes.
   * Enforce SSHv2 with modern cryptographic ciphers: `chacha20-poly1305@openssh.com`, `aes256-gcm@openssh.com`, and Diffie-Hellman group `curve25519-sha256`.
   * Enforce HTTPS with TLS 1.3 only; disable TLS 1.0, 1.1, and 1.2 with weak CBC ciphers.
   * SNMPv3 configured exclusively with `authPriv` (Authentication: SHA-256; Encryption: AES-256).
2. **Camera Hardware Root of Trust:**
   * Secure Boot cryptographically verifies manufacturer-signed firmware before execution.
   * Private keys for 802.1X certificates and HTTPS are generated inside the on-board cryptographic hardware module (TPM 2.0 / Secure Element) and are non-exportable.
