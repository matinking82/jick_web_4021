from pydantic import BaseModel


class statistics(BaseModel):
    total_likes: int | None
    total_follows: int | None
    total_posts: int | None
    total_registers: int | None

    new_follows: int | None
    new_posts: int | None
    new_registers: int | None
