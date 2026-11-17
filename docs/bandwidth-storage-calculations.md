# Bandwidth, Storage & Compute Engineering Calculations
## Calcoli Ingegneristici di Larghezza di Banda, Storage e Computo

---

### 1. Mathematical Formulas & Methodology / Formule Matematiche e Metodologia

*EN:* The calculation of network transmission bandwidth and physical storage retention for video surveillance streams is governed by the standard video engineering equations:

$$\text{Bitrate per Camera } (R_c) = \text{Resolution} \times \text{FPS} \times \text{Bits per Pixel} \times \text{Compression Efficiency factor} \times \text{Scene Complexity} (\kappa)$$

$$\text{Daily Storage Consumption } (S_{\text{day}}) = \left( \sum_{i=1}^{N} \frac{R_{c,i} \text{ (Mbps)}}{8} \right) \times 3600 \times 24 \times (1 + \mu_{\text{meta}})$$

$$\text{Total Retention Storage } (S_{\text{total}}) = S_{\text{day}} \times D_{\text{retention}} \times (1 + \Omega_{\text{filesystem}})$$

$$\text{Usable RAID-6 Capacity } (C_{\text{RAID-6}}) = (N_{\text{drives}} - N_{\text{parity}} - N_{\text{spare}}) \times \text{Drive Capacity} \times \lambda_{\text{dec-to-bin}}$$

*IT:* Il calcolo della larghezza di banda di trasmissione e della capacità di archiviazione fisica per i flussi di videosorveglianza è regolato dalle equazioni standard di ingegneria video sopra riportate, tenendo conto di un fattore di complessità di scena ($\kappa$), dell'overhead di metadati AI ($\mu_{\text{meta}} = 5\%$) e della formattazione del filesystem ($\Omega_{\text{filesystem}} = 10\%$).

---

### 2. Camera-by-Camera Bitrate Sizing / Dimensionamento Bitrate per Singola Telecamera

| Group / Gruppo | Qty | Model | Resolution | Framerate | Codec | Compression Profile | Motion % | Avg Bitrate / Cam | Peak Burst | Substream (AI/Grid) | Total Ingress (Group) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Perimeter AI** | 8 | Axis Q1715 / P1468 | 3840×2160 (4K) | 25 fps | H.265 | Zipstream High | 30% (Day) / 10% (Night) | 6.0 Mbps | 10.0 Mbps | 1.0 Mbps (720p@10) | **56.0 Mbps** |
| **Factory Floor** | 10 | Axis P3265-LV | 1920×1080 (2MP)| 60 fps | H.265 | Zipstream Medium | 90% (Constant Machinery)| 4.5 Mbps | 7.5 Mbps | 0.8 Mbps (720p@10) | **53.0 Mbps** |
| **Gate / ANPR** | 2 | Axis Q1700-LE | 1920×1080 (2MP)| 60 fps | H.264/H.265 | High Shutter / Low Latency | 40% (Gate traffic) | 5.5 Mbps | 8.5 Mbps | 1.0 Mbps (720p@10) | **13.0 Mbps** |
| **TOTALS** | **20** | - | - | - | - | - | - | - | - | - | **122.0 Mbps** (Sustained) <br> **185.0 Mbps** (Peak) |

---

### 3. Aggregated Network Throughput Analysis
#### Analisi del Throughput di Rete Aggregato

*EN:*
* **IDF-1 Ingress (Perimeter, 8x 4K):** $8 \times 7.0 \text{ Mbps} = 56.0 \text{ Mbps}$. Uplink to Core: 10 Gbps SFP+. Utilization: $\mathbf{0.56\%}$.
* **IDF-2 Ingress (Factory Floor, 8x High-Speed):** $8 \times 5.3 \text{ Mbps} = 42.4 \text{ Mbps}$. Uplink to Core: 10 Gbps SFP+. Utilization: $\mathbf{0.42\%}$.
* **IDF-3 Ingress (Warehouse & ANPR, 4x Cameras):** $(2 \times 5.3) + (2 \times 6.5) = 23.6 \text{ Mbps}$. Uplink to Core: 10 Gbps SFP+. Utilization: $\mathbf{0.24\%}$.
* **Core Switch Interconnect to VMS/AI Node:** Dual 10GbE LACP Link aggregation ($\text{Throughput Capacity} = 20 \text{ Gbps}$). Total video ingestion: $\approx 122 \text{ Mbps} \implies \mathbf{0.61\%}$ bus utilization.
* **VMS Node to SAN/NAS Storage (iSCSI):** Dual dedicated 10GbE non-routed links with MPIO (Round Robin). Total write payload: $122 \text{ Mbps} / 8 = 15.25 \text{ MB/s}$. 10G iSCSI interface capacity: $1,150 \text{ MB/s}$. Bus saturation is under $\mathbf{1.4\%}$.

*IT:* I calcoli dimostrano che l'infrastruttura di dorsale a 10 Gbps garantisce una saturazione media inferiore all'1%, eliminando completamente qualsiasi fenomeno di jitter, accodamento nei buffer o perdita di frame (dropped frames), anche durante picchi improvvisi generati da algoritmi AI o registrazioni ad alto frame-rate (60 fps).

---

### 4. Storage Capacity Sizing & Retention Plan
#### Dimensionamento della Capacità di Archiviazione e Piano di Retention

#### 4.1 Daily Ingestion Calculation / Calcolo dell'Ingestione Giornaliera
* **Primary Streams (20 Cameras, 24/7 continuous):**
  $$\text{Bitrate Total} = (8 \times 6.0) + (10 \times 4.5) + (2 \times 5.5) = 48.0 + 45.0 + 11.0 = 104.0 \text{ Mbps}$$
* **Data per Second:** $104.0 \text{ Mbps} / 8 = 13.00 \text{ MB/s}$
* **Data per Hour:** $13.00 \text{ MB/s} \times 3600 \text{ s} = 46,800 \text{ MB/h} = 46.80 \text{ GB/h}$
* **Data per Day (24 Hours):** $46.80 \text{ GB/h} \times 24 \text{ h} = 1,123.2 \text{ GB/day} \approx \mathbf{1.123 \text{ TB/day}}$
* **Metadata & AI Vector Index (5%):** $1.123 \times 0.05 = 0.056 \text{ TB/day}$
* **Gross Daily Ingestion ($S_{\text{day}}$):** $\mathbf{1.179 \text{ TB/day}}$

#### 4.2 Multi-Day Retention Requirements / Fabbisogno per Scaglioni di Retention
* **30-Day Mandatory Retention (Industrial / GDPR compliance):**
  $$S_{30} = 30 \times 1.179 \text{ TB} = \mathbf{35.37 \text{ TB}}$$
* **60-Day Extended High-Security Retention:**
  $$S_{60} = 60 \times 1.179 \text{ TB} = \mathbf{70.74 \text{ TB}}$$
* **90-Day Maximum Audit Horizon:**
  $$S_{90} = 90 \times 1.179 \text{ TB} = \mathbf{106.11 \text{ TB}}$$

---

### 5. SAN / Storage Architecture & RAID-6 Reliability Analysis
#### Architettura SAN / Storage e Analisi di Affidabilità RAID-6

#### 5.1 Physical Storage Enclosure: Dell PowerVault ME5012 / Synology RS3621RPxs
* **Form Factor:** 2U Rackmount, 12x 3.5" SAS-3 12Gb/s Drive Bays.
* **Drive Specification:** 12x 16 TB Enterprise SAS 7,200 RPM, 512e/4Kn format, 2.5M hours MTBF.
* **Array Configuration:**
  * **Drive Count:** 12 Disks
  * **Parity Drives:** 2 Disks (RAID-6 dual-parity, allowing survival of 2 concurrent drive failures)
  * **Hot Spare:** 1 Dedicated Global Hot-Spare Disk (auto-rebuild upon physical trip)
  * **Active Data Disks:** $12 - 2 - 1 = \mathbf{9 \text{ Data Disks}}$
* **Gross Raw Usable Capacity:**
  $$\text{Raw Capacity} = 9 \times 16 \text{ TB} = \mathbf{144 \text{ TB}}$$
* **Binary Conversion ($10^{12} \to 2^{40}$) & Filesystem Overhead:**
  $$\text{Effective Usable Storage} = 144 \times 0.9095 \times 0.90 (\text{10% filesystem/snapshot reserve}) = \mathbf{117.8 \text{ TiB usable}}$$

> [!NOTE]
> *EN:* The effective usable volume of **117.8 TiB** guarantees **99.9 days of continuous 24/7 recording** for all 20 cameras, vastly surpassing the 30-day requirement and allowing full operational longevity without disk expansion for over 5 years.
>
> *IT:* Il volume utile effettivo di **117.8 TiB** garantisce ben **99.9 giorni di registrazione continua 24/7** per tutte le 20 telecamere, superando ampiamente il requisito di 30 giorni e offrendo una longevità operativa superiore a 5 anni senza necessità di espansioni disco.

---

### 6. Compute & Hardware AI Acceleration Sizing
#### Dimensionamento Computazionale e Accelerazione AI Hardware

* **VMS & Inference Node:** Dell PowerEdge R750xa Rack Server.
* **CPU:** Dual Intel Xeon Gold 6338 (2x 32 Cores, 64 Threads, 2.0 GHz base, 3.2 GHz Turbo).
* **RAM:** 128 GB DDR4-3200 MHz ECC Registered (4x 32GB RDIMMs, Octa-channel memory).
* **Inference Accelerators:** 1x NVIDIA RTX 6000 Ada Generation (48 GB GDDR6 with ECC, 18,176 CUDA cores, 568 Tensor cores, 91.1 TFLOPS FP32) or 2x NVIDIA L4 (24 GB each).
* **AI Workload Distribution:**
  * 8x 4K Streams: Edge inference on camera (Axis ARTPEC-8 Deep Learning Processing Unit) executes local object detection (person, vehicle, license plate).
  * VMS Central Node: Ingests bounding box telemetry and executes high-confidence secondary classification, facial re-identification, perimeter tripwire verification, and ANPR optical character recognition (OCR) with TensorRT optimization.
  * Inference Latency: $< 15 \text{ ms}$ per inference frame.
* **OS / VMS Database Storage:** 2x 960 GB NVMe PCIe Gen4 SSD in hardware RAID-1 (Dell PERC H755 Front SAS/NVMe controller) delivering $> 800,000 \text{ random read IOPS}$ for SQL database indexing.
