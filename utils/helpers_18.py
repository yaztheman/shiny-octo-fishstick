"""Utility functions for shiny-octo-fishstick"""

import datetime
from typing import Optional, List, Dict

def format_date(date: datetime.datetime) -> str:
    """Format date to string.
    
    Args:
        date: Date object to format
        
    Returns:
        Formatted date string
    """
    if not date:
        return ''
    return date.strftime('%Y-%m-%d')

def validate_email(email: str) -> bool:
    """Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email:
        return False
    import re
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(pattern, email))

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result or None if division by zero
    """
    if b == 0:
        return None
    return a / b

def filter_valid_items(items: List[Dict]) -> List[Dict]:
    """Filter out invalid items from list."""
    return [item for item in items if item and isinstance(item, dict)]


"""
Shiny Octo Fishstick - Performance Improvement
Shiny Octo Fishstick
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]


"""
Shiny Octo Fishstick - Performance Improvement
Shiny Octo Fishstick
"""

import logging
from functools import lru_cache

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def cached_computation(value):
    """Cached computation for better performance"""
    logger.debug(f"Computing value: {value}")
    return value ** 2

def batch_process(items, batch_size=100):
    """Process items in batches for better memory usage"""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield process_batch(batch)

def process_batch(batch):
    """Process a single batch"""
    return [item.upper() for item in batch]
