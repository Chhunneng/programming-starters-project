#!/usr/bin/env python3
"""
Simple Service Health Check Script
Author: Simardeep Singh
Description:
    Checks the health of a given HTTP endpoint.
    Exits with code 0 if healthy, 1 if not.
"""

import sys
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_service(url: str, timeout: int = 5) -> bool:
    """Check if the service at `url` is healthy."""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            logging.info(f"✅ Service healthy at {url}")
            return True
        else:
            logging.warning(f"⚠️ Service unhealthy at {url} - Status: {response.status_code}")
            return False
    except requests.RequestException as e:
        logging.error(f"❌ Error reaching {url}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python health_check.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    healthy = check_service(url)

    if healthy:
        print(f"[{datetime.now()}] Service at {url} is UP ✅")
        sys.exit(0)
    else:
        print(f"[{datetime.now()}] Service at {url} is DOWN ❌")
        sys.exit(1)