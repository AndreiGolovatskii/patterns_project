from libs.player.resource_wallet import ResourceWallet



def test_wallet():
    wallet = ResourceWallet(money=100, oil=100, electricity=100)

    low_price = ResourceWallet(money=10, oil=10, electricity=10)
    high_price = ResourceWallet(money=100, oil=101, electricity=99)    

    assert low_price < high_price
    assert low_price <= wallet
    assert not high_price <= wallet
    assert not high_price < wallet

    assert (wallet - low_price) < wallet
    assert wallet + low_price - low_price == wallet

    assert wallet.money == 100
    wallet -= wallet
    assert wallet == ResourceWallet()
