struct Proposal:
    name: bytes32
    vote_count: int128

proposals: public(map(int128, Proposal))

voters_voted: public(map(address, int128))

manager: public(address)

@public
def __init__(_proposalNames: bytes32[2]):
    for i in range(2):
        self.proposals[i] = Proposal({
            name: _proposalNames[i],
            vote_count: 0
        })
    self.manager = msg.sender

@public
@payable
def vote(proposal: int128):
    assert msg.value >= as_wei_value(0.01, "ether")
    assert self.voters_voted[msg.sender] == 0
    assert proposal < 2 and proposal >= 0

    self.voters_voted[msg.sender] = 1
    self.proposals[proposal].vote_count += 1

@private
@constant
def winning_proposal() -> int128:
    winning_vote_count: int128 = 0
    winning_proposal: int128 = 0
    for i in range(2):
        if self.proposals[i].vote_count > winning_vote_count:
            winning_vote_count = self.proposals[i].vote_count
            winning_proposal = i
    return winning_proposal

@public
@constant
def winner_name() -> bytes32:
    return self.proposals[self.winning_proposal()].name

@public
def withdraw_money():
    assert msg.sender == self.manager

    send(self.manager, self.balance)
