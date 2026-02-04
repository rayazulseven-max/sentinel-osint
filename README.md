# SENTINEL: Autonomous OSINT Intelligence Agent

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Security](https://img.shields.io/badge/Security-Standard-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 📡 Mission Profile
**SENTINEL** is an autonomous intelligence gathering agent designed to automate the **Collection**, **Processing**, and **Analysis** phases of the intelligence cycle.

In high-threat environments, human analysts are overwhelmed by the volume of open-source data (news, social feeds, RSS). SENTINEL acts as a force multiplier, autonomously scraping thousands of data points, filtering for specific threat vectors (e.g., "Cyberattack," "Civil Unrest," "Infrastructure Failure"), and generating executive-level situation reports (SITREPs) in real-time.

**Operational Impact:** Reduces "Time-to-Insight" from hours to seconds, allowing analysts to focus on decision-making rather than data entry.

---

## ⚙️ Core Capabilities

### 1. Autonomous Collection (Scraper Module)
* **Multi-Source Ingestion:** Simultaneously monitors RSS feeds, GDELT data, and targeted web sources.
* **Anti-Detection Logic:** Implements randomized user-agent rotation and rate-limiting to bypass standard WAF (Web Application Firewall) defenses.
* **Low-Bandwidth Mode:** Optimized for deployed environments with degraded network connectivity.

### 2. Intelligent Processing (Analysis Module)
* **Entity Extraction (NER):** Automatically identifies and tags **Locations**, **Organizations**, and **Key Individuals** within raw text.
* **Sentiment & Threat Scoring:** Assigns a quantitative "Risk Score" (0-100) to each incoming report based on keyword density and sentiment analysis.
* **Summarization Engine:** Uses local LLM integration (Llama 3 / Mistral) to synthesize 50+ articles into a single 3-bullet summary.

### 3. Dissemination (Reporting Module)
* **Instant Alerts:** Pushes high-priority alerts to Discord/Slack webhooks or SMS gateways.
* **Daily SITREP:** Compiles a PDF briefing document at 0800 hours daily.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Core Logic** | Python 3.11 | Primary agent orchestration |
| **Data Handling** | Pandas / NumPy | High-speed data filtering and structuring |
| **Scraping** | Requests / BeautifulSoup | Lightweight, headless data collection |
| **AI / LLM** | OpenAI API / Ollama | Narrative generation and summarization |
| **Database** | SQLite / JSON | Local, lightweight storage (No cloud dependency) |

---

## 🚀 Installation & Usage

**Prerequisites**
* Python 3.10+
* API Keys (Optional for LLM features)

```bash
# Clone the repository
git clone [https://github.com/YourUsername/sentinel.git](https://github.com/YourUsername/sentinel.git)

# Navigate to directory
cd sentinel

# Install dependencies
pip install -r requirements.txt

# Run the agent in "Monitor Mode"
python main.py --mode monitor --target "San Antonio"
