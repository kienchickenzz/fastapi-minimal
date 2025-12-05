from src.health.database.repository.health_check.main import HealthCheckRepository

class HealthCheckService:
    def __init__(self, health_check_repository: HealthCheckRepository):
        self.health_check_repository = health_check_repository

    async def check_db_health(self) -> None:
        await self.health_check_repository.create({})

    async def get_health_checks(self, target_page: int, page_size: int):
        skip = (target_page - 1) * page_size
        return await self.health_check_repository.get_multiple(
            limit=page_size,
            skip=skip,
        )
