# Recipe-Blog


###########################################################################################################
Some Basic Security Principles to follow

Keep Debug = False in Production
Limit Allowed hosted to our Server IP, localhost, and hostnames
Keep Secret key strong and safe
All ways use HTTPS  in Production
Keep a check on user uploads if being managed by multiple users
Keep your database secure and don’t use SQLite in Production
Try to use Security and content headers in production, a few headers are given below add these in Settings.py

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True


###########################################################################################################

