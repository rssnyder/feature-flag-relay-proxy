from logging import DEBUG
from time import sleep
from os import getenv

from featureflags.evaluations.auth_target import Target
from featureflags.config import with_events_url
from featureflags.config import with_base_url
from featureflags.client import CfClient
from featureflags.util import log

from fastapi import FastAPI

app = FastAPI()

log.setLevel(DEBUG)

# set up relay proxy
relay_proxy_address = getenv("RELAY_PROXY_ADDRESS", "http://localhost:7000")
log.info(f"connecting to proxy at {relay_proxy_address}")

# env
client = CfClient(
    getenv("FF_SDK_KEY"),
    with_base_url(relay_proxy_address),
    with_events_url(relay_proxy_address),
)

# env dos
if getenv("FF_SDK_KEY_TWO"):
    client_two = CfClient(
        getenv("FF_SDK_KEY_TWO"),
        with_base_url(relay_proxy_address),
        with_events_url(relay_proxy_address),
    )

# target
target = Target(
    identifier="HT_1",
    name="Harness_Target_1",
    attributes={"location": "python w/ fast api"},
)


@app.get("/")
def read_root():
    payload = {
        getenv("FF_IDENTIFIER", "test"): client.bool_variation(
            getenv("FF_IDENTIFIER", "test"), target, False
        )
    }

    if getenv("FF_SDK_KEY_TWO"):
        payload[getenv("FF_IDENTIFIER", "test") + "_TWO"] = client_two.bool_variation(
            getenv("FF_IDENTIFIER", "test"), target, False
        )

    return payload
