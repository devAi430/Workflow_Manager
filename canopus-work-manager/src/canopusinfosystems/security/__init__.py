"""
Canopus Infosystems security module.

This module provides security-related functionality for Canopus Infosystems, including:
- Fingerprinting for component identity and tracking
- Security configuration for controlling access and permissions
- Future: authentication, scoping, and delegation mechanisms
"""

from canopusinfosystems.security.fingerprint import Fingerprint
from canopusinfosystems.security.security_config import SecurityConfig

__all__ = ["Fingerprint", "SecurityConfig"]
