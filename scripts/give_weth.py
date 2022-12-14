from scripts.helpful_scripts import get_account
from brownie import interface, config, network
from web3 import Web3

def main():
    get_weth()

def get_weth():
    """
    Mints weth

    """

    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.withdraw(Web3.toWei(0.76, "ether"),{"from": account})
    tx.wait(1)
    print("Received 0.1 WETH")