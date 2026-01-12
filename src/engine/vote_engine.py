from typing import TypeVar, Generic, Dict, Hashable

VoterT = TypeVar("VoterT", bound=Hashable)
CandidateT = TypeVar("CandidateT", bound=Hashable)


class VoteBallot(Generic[VoterT, CandidateT]):
    def __init__(self, author: VoterT, target: CandidateT) -> None:
        self._author = author
        self._target = target

    @property
    def author(self) -> VoterT:
        return self._author

    @property
    def target(self) -> CandidateT:
        return self._target


class VoteEngine(Generic[VoterT, CandidateT]):
    def __init__(self) -> None:
        self._vote_direction: Dict[VoterT, CandidateT] = {}

    def get_voted_from(self, author: VoterT) -> CandidateT:
        return self._vote_direction[author]

    def vote(self, ballot: VoteBallot[VoterT, CandidateT]) -> None:
        self._vote_direction[ballot.author] = ballot.target

    def get_winner(self) -> CandidateT:
        count: Dict[CandidateT, int] = {}

        for target in self._vote_direction.values():
            count[target] = count.get(target, 0) + 1

        return max(count.keys(), key= lambda x: count[x])

    def clear(self) -> None:
        self._vote_direction.clear()
