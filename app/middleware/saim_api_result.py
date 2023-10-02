from fastapi import HTTPException
from typing import Optional, Any


class SaimApiResponse:
    def create_response(self, success: Optional[bool] = False, data: Optional[Any] = None, message: Optional[str] = None):
        response = {
            "data": data,
            "message": message,
            "success": success,
        }
        return response


saim_api_response = SaimApiResponse()
# raise HTTPException(status_code=404, detail="Recurso não encontrado")
