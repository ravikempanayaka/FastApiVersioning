from enum import Enum

from fastapi import APIRouter, Header

from client import create_version_item

version = 'v'


class VersionNumber(str, Enum):
    _1_0 = "1"
    _2_0 = "2"
    _3_0 = "3"


class BaseDetailView:
    @property
    def router(self):
        api_router = APIRouter(prefix=f'/{version}')

        @api_router.get('{accept_version}/get/{uid}')
        def get_detail_api(uid: str, accept_version: VersionNumber = Header(VersionNumber._1_0)):
            class_name = 'views.ClientBaseDetailView'
            items = create_version_item(accept_version.value, class_name)
            return items.get_detail_api(uid)

        return api_router


routers = [
    BaseDetailView
]


def get_routers():
    return routers
