# generated by datamodel-codegen:
#   filename:  nullable.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field


class Cursors(BaseModel):
    prev: Optional[str] = Field(...)
    next: str = 'last'
    index: float


class TopLevel(BaseModel):
    cursors: Cursors


class Info(BaseModel):
    name: str


class User(BaseModel):
    info: Info


class Api(BaseModel):
    apiKey: str = Field(None, description='To be used as a dataset parameter value')
    apiVersionNumber: str = Field(
        None, description='To be used as a version parameter value'
    )
    apiUrl: Optional[AnyUrl] = Field(
        None, description="The URL describing the dataset's fields"
    )
    apiDocumentationUrl: Optional[AnyUrl] = Field(
        None, description='A URL to the API console for each API'
    )


class Apis(BaseModel):
    __root__: Optional[List[Api]] = Field(...)


class EmailItem(BaseModel):
    author: str
    address: str = Field(..., description='email address')
    description: str = 'empty'


class Email(BaseModel):
    __root__: List[EmailItem]


class Id(BaseModel):
    __root__: int