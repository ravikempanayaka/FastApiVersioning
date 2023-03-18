from fastapi import APIRouter

version = 'V'


class ClientBaseDetailView:

    def get_detail_api(self, uid: str):
        return f"this v1 is current {version + uid}"
