from sqlalchemy.orm import Mapped, mapped_column
from src.db.db import Base
from src.schemas.tasks import Tasks


class Tasks(Base):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> Tasks:
        return Tasks(
            id=self.id,
            name=self.name,
            description=self.description
        )
    