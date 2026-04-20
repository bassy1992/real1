#!/usr/bin/env python3
"""
Generate a secure Django SECRET_KEY
Run this and copy the output to your Railway environment variables
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    print("Generated SECRET_KEY:")
    print(get_random_secret_key())
