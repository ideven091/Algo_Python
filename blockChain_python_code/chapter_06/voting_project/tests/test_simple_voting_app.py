import pytest
import eth_tester


@pytest.fixture()
def voting(chain):
    SimpleVotingFactory = chain.provider.get_contract_factory('SimpleVoting')
    deploy_txn_hash = SimpleVotingFactory.constructor([b'Messi', b'Ronaldo']).transact()
    contract_address = chain.wait.for_contract_address(deploy_txn_hash)
    return SimpleVotingFactory(address=contract_address)

def test_initial_state(voting):
    assert voting.functions.proposals_count().call() == 2

    messi = voting.functions.proposals__name(0).call()
    assert len(messi) == 32
    assert messi[:5] == b'Messi'
    assert voting.functions.proposals__name(1).call()[:7] == b'Ronaldo'
    assert voting.functions.proposals__vote_count(0).call() == 0
    assert voting.functions.proposals__vote_count(1).call() == 0

def test_vote(voting, chain):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    assert voting.functions.proposals__vote_count(0).call() == 0

    set_txn_hash = voting.functions.vote(0).transact({'from': account2})
    chain.wait.for_receipt(set_txn_hash)

    assert voting.functions.proposals__vote_count(0).call() == 1

def test_fail_duplicate_vote(voting, chain):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]

    set_txn_hash = voting.functions.vote(0).transact({'from': account2})
    chain.wait.for_receipt(set_txn_hash)

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        voting.functions.vote(1).transact({'from': account2})

    with pytest.raises(eth_tester.exceptions.TransactionFailed):
        voting.functions.vote(0).transact({'from': account2})

def test_winning_proposal(voting, chain):
    t = eth_tester.EthereumTester()
    account2 = t.get_accounts()[1]
    account3 = t.get_accounts()[2]
    account4 = t.get_accounts()[3]

    set_txn_hash = voting.functions.vote(0).transact({'from': account2})
    chain.wait.for_receipt(set_txn_hash)

    set_txn_hash = voting.functions.vote(0).transact({'from': account3})
    chain.wait.for_receipt(set_txn_hash)

    set_txn_hash = voting.functions.vote(1).transact({'from': account4})
    chain.wait.for_receipt(set_txn_hash)

    assert voting.functions.proposals__vote_count(0).call() == 2
    assert voting.functions.proposals__vote_count(1).call() == 1
    assert voting.functions.winner_name().call()[:5] == b'Messi'
