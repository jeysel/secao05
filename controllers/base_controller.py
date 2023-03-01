from typing import Optional, List
from fastapi.requests import Request
from sqlalchemy.future import select
from core.database import get_session

class BaseController:
    def __init__(self, request: Request, model: object) -> None:
        self.request: Request = request
        self.model: object = model

    # Retorna todos os registros do model
    async def get_all_crud(self) -> Optional[List[object]]:
       async with get_session() as session:
            query = select(self.model)
            result = await session.execute(query)

            return  result.scalars().all()

    # Retorna o objeto especificado pelo id_obj ou None
    async def get_one_crud(self, id_obj: int) -> Optional[object]:
        async with get_session() as session:
            obj: self.model = await session.get(self.model, id_obj)

            return obj

    async def post_crud(self) -> None:
        raise NotImplementedError("Voce deve implementar este método.")

    async def put_crud(self, obj: object) -> None:
        raise NotImplementedError("Você deve implementar este método")

    async def del_crud(self, id_obj: int) -> None:
        async with get_session() as session:
            obj: self.model = await  session.get(sel.model, id_obj)

            if obj:
                await session.delete(obj)
                await session.commit()