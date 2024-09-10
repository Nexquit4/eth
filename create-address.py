import time

from web3 import Web3
from eth_account import Account
import random
from mnemonic import Mnemonic

# Включение функций для работы с сид-фразами
Account.enable_unaudited_hdwallet_features()
i = 0

# Список Ethereum RPC эндпоинтов
nodes = [
    'https://rpc.ankr.com/eth',
    'https://ethereum.blockpi.network/v1/rpc/public',
    'https://cloudflare-eth.com',
    'https://eth-mainnet.gateway.pokt.network/v1/5f3453978e354ab992c4da79',
    'https://eth-mainnet.public.blastapi.io',
    'https://1rpc.io/eth',
    'https://api.securerpc.com/v1',
    'https://ethereum.publicnode.com',
    'https://yolo-intensive-paper.discover.quiknode.pro/45cad3065a05ccb632980a7ee67dd4cbb470ffbd',
    'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161',
    'https://eth-mainnet.alchemyapi.io/v2/QKMdAyFAARxN-dEm_USOu8-u0klcBuTO',
    'https://eth.public-rpc.com',
    'https://mainnet-eth.compound.finance',
    'https://eth.llamarpc.com',
    'https://endpoints.omniatech.io/v1/eth/mainnet/public',
    'https://mainnet-eth.compound.finance'
]


def generate_seed_phrase():
    """Генерация сид-фразы и получение приватного ключа и адреса"""
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # Генерация случайной сид-фразы
    acct = Account.from_mnemonic(seed_phrase)
    private_key = acct.key.hex()

    return seed_phrase, private_key, acct.address


def check_balance(node_url, address):
    """Проверка баланса по ноде и адресу"""
    try:
        w3 = Web3(Web3.HTTPProvider(node_url))
        if not w3.isConnected():
            return None  # Возвращаем None, если нода не отвечает

        balance = w3.eth.get_balance(address, 'latest')
        print(f"{balance} ETH | {address}")

        if balance != 0:
            print(f"FOUND balance on {address}")
            return True
    except Exception as e:
        return None
    return False


def check_wallet_balance(seed_phrase):
    """Проверка баланса для всех адресов в кошельке"""
    acct = Account.from_mnemonic(seed_phrase)
    for address in acct.address:
        for node_url in nodes:
            result = check_balance(node_url, address)
            if result is None:
                # Если нода не отвечает, переходим к следующей
                continue
            elif result:
                # Если найден баланс, выводим информацию и выходим
                print(f"Address with balance found! Seed phrase: {seed_phrase}")
                return
        # Если ни одна нода не обнаружила баланс, продолжаем с другим адресом


while True:
    # Генерация сид-фразы и получение адреса
    i = i + 1
    seed_phrase, private_key, address = generate_seed_phrase()

    # Проверка баланса для всех адресов в кошельке
    check_wallet_balance(seed_phrase)

    print(f"{i} {address} | {seed_phrase}")
    time.sleep(3)

#bargain edge fiber guide maximum open artwork episode various game donate crime



