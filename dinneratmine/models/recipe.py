from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base
from heliumwebapp.data.DbContext import engine

Base = declarative_base()


class Magnet(Base):
    __tablename__ = "CooldownApp_CLMCLoad"

    id = Column(Integer, primary_key=True)
    magnet_type = Column(String) #[MagnetType]
    cryostat_number = Column(Integer) #[CryoNo]
    bay_number = Column(String) #[Bay]
    warm_weight = Column(Float) #[WarmWeight]
    rs_magnet = Column(Boolean, default=False) #[RSMagnet]
    n2_fill = Column(Boolean, default=False) #[N2Fill]
    datetime_load = Column(DateTime) #[DateTimeLoad]
    datetime_unload = Column(DateTime) #[DateTimeUnload]
    mac_address = Column(String) #[MAC]
    clmc = Column(Boolean, default=None) #[CLMC]
    load_user = Column(String) #[LoadUser]
    unload_user = Column(String) #[UnoadUser]
    
    
Base.metadata.create_all(engine)