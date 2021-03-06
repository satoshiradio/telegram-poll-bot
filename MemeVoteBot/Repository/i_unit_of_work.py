from abc import ABC, abstractmethod

from MemeVoteBot.Repository.VoteRepository.i_vote_repository import IVoteRepository
from MemeVoteBot.Repository.i_repository import IRepository


class IUnitOfWork(ABC):
    @abstractmethod
    def get_vote_repository(self) -> IVoteRepository:
        raise NotImplementedError

    @abstractmethod
    def set_vote_repository(self, repository: IRepository):
        raise NotImplementedError

    @abstractmethod
    def complete(self) -> int:
        raise NotImplementedError
