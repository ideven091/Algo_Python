import pytest
import eth_tester


@pytest.fixture()
def voting(chain):
    TokenBasedVotingFactory = chain.provider.get_contract_factory('TokenBasedVoting')
    deploy_txn_hash = TokenBasedVotingFactory.constructor([b'Messi', b'Ronaldo']).transact()
    contract_address = chain.wait.for_contract_address(deploy_txn_hash)
    return TokenBasedVotingFactory(address=contract_address)

def assign_tokens(voting, chain, web3):
    t = eth_tester.EthereumTester()
    accounts = t.get_accounts()

    for i in range(1, 9):
        set_txn_hash = voting.functions.assign_token(accounts[i]).transact({'from': web3.eth.coinbase})
        chain.wait.for_receipt(set_txn_hash)

def test_assign_token(voting, chain):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    assert not voting.functions.token(account2).call()

    set_txn_hash = voting.functions.assign_token(account2).transact({})
    chain.wait.for_receipt(set_txn_hash)

    assert voting.functions.token(account2).call()

def test_cannot_vote_without_token(voting, chain, web3):
    t = eth_tester.EthereumTester()
    account10 = t.get_accounts()[9]

    assign_tokens(voting, chain, web3)

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        voting.functions.vote(0).transact({'from': account10})

def test_can_vote_with_token(voting, chain, web3):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    assign_tokens(voting, chain, web3)

    assert voting.functions.proposals__vote_count(0).call() == 0

    set_txn_hash = voting.functions.vote(0).transact({'from': account2})
    chain.wait.for_receipt(set_txn_hash)

    assert voting.functions.proposals__vote_count(0).call() == 1
