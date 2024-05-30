# Local Module imports
from .base import EfecteBaseModel


class EfecteCountry(EfecteBaseModel):

    template_code: str = "country"
    "Static template code value"

    odoo_name: str = None
    "Country Name"

    country_name: str = None
    "Broken Country Name"

    country_code: str = None
    "Country Code"

    country_prefix: str = None
    "Country Prefix"

    odoo_id: int = None
    "Odoo Id"
