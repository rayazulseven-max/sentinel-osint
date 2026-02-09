import time
import json
import feedparser  # THE UPGRADE: Real RSS scraping
from datetime import datetime

# CONFIGURATION
# ---------------------------------------------------------
TARGET_KEYWORDS = [
    "civil unrest",
    "power outage",
    "cyberattack",
    "protest",
    "police activity",
    "emergency"
]

LOCATIONS = ["San Antonio", "Austin", "Dallas"]

# ANSI COLORS (Keeping the 'Cool Factor')
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

class SentinelAgent:
    def __init__(self, target_city):
        self.target_city = target_city
        self.intel_ledger = []
        print(f"{GREEN}[SENTINEL]{RESET} Initializing Agent for Target: {CYAN}{self.target_city}{RESET}...")
        time.sleep(1) # Brief pause for effect is fine

    def scrape_sources(self):
        """
        Scrapes REAL Google News RSS feeds for the target city + keywords.
        """
        print(f"{YELLOW}[COLLECT]{RESET} Connecting to Global News Stream...")
        
        real_hits = []
        
        # We construct a search query for Google News RSS
        # Query Format: "San Antonio AND (civil unrest OR power outage...)"
        query_keywords = " OR ".join(TARGET_KEYWORDS)
        encoded_query = f"{self.target_city} {query_keywords}"
        rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"

        print(f"   >>> Querying Endpoint: {rss_url[:60]}...")
        
        # THE REAL PAYLOAD
        feed = feedparser.parse(rss_url)
        
        print(f"   >>> Stream Status: {feed.status if 'status' in feed else 'OK'}")
        print(f"   >>> Entries Found: {len(feed.entries)}")

        for entry in feed.entries:
            # Check if any keyword is actually in the title (Case Insensitive)
            title_clean = entry.title.lower()
            
            for keyword in TARGET_KEYWORDS:
                if keyword.lower() in title_clean:
                    # WE HAVE A MATCH
                    hit_data = {
                        "source": entry.source.title,
                        "title": entry.title,
                        "link": entry.link,
                        "published": entry.published,
                        "matched_keyword": keyword
                    }
                    real_hits.append(hit_data)
                    print(f"   {RED}[MATCH]{RESET} {entry.title[:60]}...")
                    break # Stop checking other keywords for this specific headline

        return real_hits

    def analyze_threat(self, hits):
        """
        Calculates threat level based on REAL volume of news.
        """
        print(f"\n{CYAN}[ANALYZE]{RESET} Processing sentiment and volume...")
        time.sleep(0.5)

        hit_count = len(hits)
        
        # LOGIC: More real news = Higher Threat
        if hit_count == 0:
            threat_level = "LOW / STABLE"
            risk_score = 10
        elif hit_count < 3:
            threat_level = "MODERATE / CHATTER"
            risk_score = 45
        elif hit_count < 10:
            threat_level = "ELEVATED / ACTIVE"
            risk_score = 75
        else:
            threat_level = "CRITICAL / SURGE"
            risk_score = 95

        report = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "location": self.target_city,
            "threat_level": threat_level,
            "risk_score": risk_score,
            "total_hits": hit_count,
            "top_headlines": [h['title'] for h in hits[:3]] # Save top 3 for the report
        }
        return report

    def generate_sitrep(self, report):
        """
        Generates the final output for the analyst.
        """
        print(f"\n{GREEN}[REPORT]{RESET} Generating SITREP...")
        time.sleep(1)

        print("\n" + "="*50)
        print(f" SENTINEL SITREP // {report['timestamp']}")
        print("="*50)
        print(f" LOCATION:    {report['location']}")
        print(f" THREAT LVL:  {report['threat_level']}")
        print(f" RISK SCORE:  {report['risk_score']}/100")
        print(f" INTEL COUNT: {report['total_hits']} verified sources")
        print("-" * 50)
        print(" TOP HEADLINES:")
        if not report['top_headlines']:
            print("  >> No significant activity detected.")
        else:
            for headline in report['top_headlines']:
                print(f"  >> {headline}")
        print("="*50 + "\n")

if __name__ == "__main__":
    # Operational Loop
    # You can change "San Antonio" to any city in LOCATIONS
    agent = SentinelAgent("San Antonio")
    
    # Run Cycle
    detected_hits = agent.scrape_sources()
    intel_report = agent.analyze_threat(detected_hits)
    agent.generate_sitrep(intel_report)
    
    print(f"{GREEN}[SENTINEL]{RESET} Cycle Complete. Standing by.")
