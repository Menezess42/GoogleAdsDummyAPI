import random
from datetime import date
from decimal import Decimal
from pprint import pprint

import pandas as pd
import pytest
from faker import Faker
import faker_commerce
from pydantic import BaseModel

FAKER_SEED = 42

Faker.seed(FAKER_SEED)

class AdsData(BaseModel):
    ad_id: str
    company_name: str
    product_name: str
    tagline: str
    description: str
    price_BR: Decimal
    start_date: date
    end_date: date
    target_audience: str


# You can send seed to chose the location of your fake data
fake_br = Faker("pt_BR")
fake_br.add_provider(faker_commerce.Provider)

# Testing faker for fake ads in pt-BR
def generate_fake_ads(num_ads: int) -> list[AdsData]:
    """
    Generates a list of fake advertising data records.
    """
    targetAudienceChoice = [
        "Tech Enthusiasts",
        "Parents",
        "Fitness Buffs",
        "Gamers",
        "Pet Owners",
    ]

    listOfAdsData: list[AdsData] = []

    for _ in range(num_ads):
        product_name = fake_br.unique.ecommerce_name()
        company_name = fake_br.company()
        tagline = fake_br.bs().capitalize() + "!"
        description = fake_br.text(max_nb_chars=200)
        price = fake_br.pydecimal(
            left_digits=3, right_digits=2, min_value=1.99, max_value=999.99
        )
        start_date = fake_br.date_between(start_date="-1y", end_date="today")
        end_date = fake_br.date_between(start_date=start_date, end_date="+6M")
        ads_id = fake_br.unique.uuid4()
        target_audience = random.choice(targetAudienceChoice)

        adsData = AdsData(
                ad_id=ads_id,
                company_name=company_name,
                product_name=product_name,
                tagline=tagline,
                description=description,
                price_BR=price,
                start_date=start_date,
                end_date=end_date,
                target_audience=target_audience,)

        listOfAdsData.append(adsData)
    return listOfAdsData


def test_faker_seed():
        adsList = generate_fake_ads(1)
        adsList = [ad.model_dump() for ad in adsList]
        assert adsList[0].get('company_name') == 'da Cruz'


