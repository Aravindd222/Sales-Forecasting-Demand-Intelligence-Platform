from pydantic import BaseModel

class SalesInput(BaseModel):
    Store: int
    Dept: int
    IsHoliday: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    Size: int
    Year: int
    Month: int
    Week: int
    Quarter: int
    Lag_1: float
    Lag_4: float
    Rolling_Mean_4: float
    Rolling_STD_4: float