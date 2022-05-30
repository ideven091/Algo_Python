import pytest
import eth_tester


@pytest.fixture()
def voting(chain):
    CommercialVotingFactory = chain.provider.get_contract_factory('CommercialVoting')
    deploy_txn_hash = CommercialVotingFactory.constructor([b'Messi', b'Ronaldo']).transact()
    contract_address = chain.wait.for_contract_address(deploy_txn_hash)
    return CommercialVotingFactory(address=contract_address)

def test_initial_state(voting, web3):
    assert voting.functions.manager().call() == web3.eth.coinbase

def test_vote_with_money(voting, chain, web3):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]
    account3 = t.get_accounts()[2]

    set_txn_hash = voting.functions.vote(0).transact({'from': account2,
                                                      'value': web3.toWei('0.05', 'ether')})
    chain.wait.for_receipt(set_txn_hash)

    set_txn_hash = voting.functions.vote(1).transact({'from': account3,
                                                      'value': web3.toWei('0.15', 'ether')})
    chain.wait.for_receipt(set_txn_hash)

    assert web3.eth.getBalance(voting.address) == web3.toWei('0.2', 'ether')

def test_vote_with_not_enough_money(voting, web3):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        voting.functions.vote(0).transact({'from': account2,
                                           'value': web3.toWei('0.005', 'ether')})

def test_manager_account_could_withdraw_money(voting, web3, chain):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    set_txn_hash = voting.functions.vote(0).transact({'from': account2, 'value': web3.toWei('1', 'ether')})
    chain.wait.for_receipt(set_txn_hash)

    initial_balance = web3.eth.getBalance(web3.eth.coinbase)
    set_txn_hash = voting.functions.withdraw_money().transact({'from': web3.eth.coinbase})
    chain.wait.for_receipt(set_txn_hash)
    after_withdraw_balance = web3.eth.getBalance(web3.eth.coinbase)

    assert abs((after_withdraw_balance - initial_balance) - web3.toWei('1', 'ether')) < web3.toWei('10', 'gwei')
