# For admin panel customization
JAZZMIN_SETTINGS = {
    "site_logo": "user/images/favicon.png",
    "login_logo": "user/images/logo.png",
    "site_icon": "user/images/favicon.png",
    "custom_css": "user/css/admin.css",
    "copyright": "Trello",
    "search_model": ["user.UserAccount"],
    "topmenu_links": [
        {"name": "Home",  "url": "/"},
    ],
    "related_modal_active": True,
    "show_ui_builder": True,
    "order_with_respect_to": [
        "user", "user.UserAccount",
        "login_history",
    ],

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ['authtoken', 'auth'],

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Trello",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Trello",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Trello",
}
