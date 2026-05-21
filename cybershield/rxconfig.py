import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin


config = rx.Config(

    app_name="frontend",

    app_module_import="frontend",

    frontend_port=3000,

    backend_port=8000,

    disable_plugins=[SitemapPlugin],
)