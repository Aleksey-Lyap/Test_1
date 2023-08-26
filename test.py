from typing import Optional, Any
from base64 import b64decode
import requests


def get_info_block(number_block: int) -> None:
    url_for_block = f'https://akash-api.w3coins.io/blocks/{number_block}'
    response = requests.get(url_for_block)
    block_info: Optional[dict[str, Any]] = response.json().get('block')
    if not block_info:
        print('No transactions')
        return

    data_block: Optional[dict[str, Any]] = block_info.get('data')
    if not data_block:
        print('No transactions')
        return

    transact_info: list[str] = data_block.get('txs', [])
    for data in transact_info:
        print(b64decode(data))


get_info_block(112)
