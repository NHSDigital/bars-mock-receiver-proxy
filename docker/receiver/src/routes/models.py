from pydantic import BaseModel
from typing import List


class Profile(BaseModel):
    profile: List[str]


class ServiceRequestBody(BaseModel):
    resourceType: str
    meta: Profile


class AppointmentBody(BaseModel):
    resourceType: str
    meta: Profile


class Organisation(BaseModel):
    meta: Profile


class NhsdToken(BaseModel):
    subject: str
    organisation: Organisation
