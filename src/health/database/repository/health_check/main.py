from src.health.database.model.health_check.main import HealthCheck
from src.health.database.repository.base.main import BaseRepository


class HealthCheckRepository(BaseRepository[HealthCheck]):
    
    def __init__(self, engine):
        super().__init__(engine, HealthCheck)
