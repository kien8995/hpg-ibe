class MaerskResponse:
    def __init__(self):
        self.from_departure = ""  # cảng đi
        self.to_destination = ""  # cảng đến
        self.container_iso_code = ""
        self.from_service_mode = ""
        self.to_service_mode = ""
        self.number_of_weeks = 4
        self.date_type = "D"
        self.date = ""
        self.vessel_flag = None
        self.cargo_type = ""
        self.container_type = ""
        self.container_length = 0
        self.brand_code = "maeu"
