# M3U8 Proxy on Hugging Face Spaces

This proxy injects headers into `.m3u8` and segment requests to bypass 403 Forbidden errors (e.g., for TiviMate).

Usage:
- `/stream.m3u8` proxies the master playlist
- `/segment?url=<encoded_url>` proxies video segments
