from module_17.app.backend.db import Base, engine
from module_17.app.models.user import User
from module_17.app.models.task import Task


Base.metadata.create_all(engine)
