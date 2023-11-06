# Local Module imports
from .base import EfecteBaseModel


class EfecteCountry(EfecteBaseModel):

    template_code: str = "country"
    "Static template code value"

    country_name: str = None
    "Country Name"

    country_code: str = None
    "Country Code"
