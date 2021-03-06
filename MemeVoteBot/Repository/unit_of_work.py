from config import DbConfig
from MemeVoteBot.Repository.VoteRepository.vote_repository import VoteRepository
from MemeVoteBot.Repository.VoteRepository.i_vote_repository import IVoteRepository
from MemeVoteBot.Repository.database import Database
from MemeVoteBot.Repository.i_repository import IRepository
from MemeVoteBot.Repository.i_unit_of_work import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self,
                 database_uri=DbConfig.SQLALCHEMY_DATABASE_URI,
                 vote_repository: IRepository = None):
        self.database = Database(database_uri)
        self.session = self.database.session()
        # repositories
        self.vote_repository = vote_repository
        if not self.vote_repository:
            self.vote_repository = VoteRepository(self.session)

    def get_vote_repository(self) -> IVoteRepository:
        return self.vote_repository

    def set_vote_repository(self, repository: IRepository) -> None:
        self.vote_repository = repository

    def complete(self) -> None:
        self.session.commit()
