from fastapi import HTTPException
from typing import Optional, Any


class SaimApiResponse:
    async def create_response(self, success: Optional[bool] = False, data: Optional[Any] = None, message: Optional[str] = None):
        response = {
            "data": data,
            "message": message,
            "success": success,
        }
        return response
    
    # async def create_error_response(self, message: str):
    #     return await self.create_response(success=False, message=message)

saim_api_response = SaimApiResponse()
# raise HTTPException(status_code=404, detail="Recurso não encontrado")
