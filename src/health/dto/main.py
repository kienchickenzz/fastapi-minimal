from src.base.dto.main import PaginatedRequestBase, PaginatedResponseBase

class HealthCheckRequest(PaginatedRequestBase):
    pass

class HealthCheckDto(PaginatedResponseBase):
    id: int
    created_at: str
    updated_at: str
