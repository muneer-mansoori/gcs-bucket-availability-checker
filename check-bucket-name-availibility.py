#!/usr/bin/env python3
"""
Google Cloud Storage Bucket Name Availability Checker

This script checks whether Google Cloud Storage bucket names are available
for creation. It's useful for developers who need to verify bucket name
availability before attempting to create new buckets.

Author: Your Name
License: MIT
Version: 1.0.0

Requirements:
    - google-cloud-storage
    - Valid Google Cloud credentials (via gcloud auth or service account)

Usage:
    python check-bucket-name-availability.py

Example:
    bucket_list = ["my-unique-bucket-name", "another-bucket-name"]
    check_bucket_availability(bucket_list)
"""

import sys
import os
import logging
from contextlib import redirect_stderr
from typing import List
from google.cloud import storage
from google.api_core.exceptions import NotFound, Forbidden, GoogleAPIError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def check_bucket_availability(bucket_names: List[str], client: storage.Client = None) -> None:
    """
    Check the availability of Google Cloud Storage bucket names.
    
    Args:
        bucket_names (List[str]): List of bucket names to check
        client (storage.Client, optional): Pre-initialized GCS client. 
                                         If None, a new client will be created.
    
    Returns:
        None: Results are printed to stdout
    
    Raises:
        Exception: If there's an issue initializing the GCS client
    """
    if client is None:
        try:
            client = storage.Client()
            logger.info("Initialized Google Cloud Storage client")
        except Exception as e:
            logger.error(f"Failed to initialize GCS client: {e}")
            raise

    logger.info(f"Checking availability for {len(bucket_names)} bucket names")
    
    for bucket_name in bucket_names:
        with open(os.devnull, 'w') as devnull, redirect_stderr(devnull):
            try:
                client.get_bucket(bucket_name)
                print(f'"{bucket_name}" = not available')
                logger.debug(f"Bucket {bucket_name} exists")
            except NotFound:
                print(f'"{bucket_name}" = available')
                logger.debug(f"Bucket {bucket_name} is available")
            except Forbidden:
                print(f'"{bucket_name}" = not available')
                logger.warning(f"Permission denied for bucket {bucket_name}")
            except GoogleAPIError as e:
                print(f'"{bucket_name}" = not available')
                logger.error(f"API error checking bucket {bucket_name}: {e}")
            except Exception as e:
                print(f'"{bucket_name}" = check failed (not available)')
                logger.error(f"Unexpected error checking bucket {bucket_name}: {e}")


def main():
    """
    Main function to demonstrate bucket name availability checking.
    """
    # Example bucket names - replace with your own
    bucket_list = [
        "example-bucket-1",
        "example-bucket-2", 
        "example-bucket-3",
        "my-unique-project-bucket-2024",
        "test-bucket-availability-check"
        # Add more bucket names as needed
    ]
    
    print("Google Cloud Storage Bucket Name Availability Checker")
    print("=" * 55)
    print(f"Checking {len(bucket_list)} bucket names...\n")
    
    try:
        check_bucket_availability(bucket_list)
    except Exception as e:
        logger.error(f"Failed to check bucket availability: {e}")
        sys.exit(1)
    
    print("\nCheck completed!")


if __name__ == "__main__":
    main()
