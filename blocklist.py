"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by app and the logout resource so that the tokens can be added to the blocklist when the users log out.
"""

BLOCKLIST = set()