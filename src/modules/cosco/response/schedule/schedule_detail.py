"""
    ScheduleDetail response model
"""
from typing import Any


class ScheduleDetail:
    """
        ScheduleDetail model class
    """
    def __init__(self):
        self.pod = ""
        self.rev_facility_code = ""
        self.available = ""
        self.dir = ""
        self.pol = ""
        self.ata = ""
        self.atd = ""
        self.cargo_nature = ""
        self.eta = ""
        self.etd = ""
        self.ext_voyage = ""
        self.pol_facility_code = ""
        self.vessel = ""
        self.row_num = 0
        self.vgm_cutoff_dt = ""
        self.vessel_code = ""
        self.id = ""
        self.cut_off = ""
        self.pod_facility_code = ""
        self.leg_sequence = 0
        self.transit_time = ""
        self.pod_port_code = ""
        self.voyage = ""
        self.inbound_haulage = ""
        self.si_cutoff = ""
        self.r24_cutoff = ""
        self.service = ""
        self.deli_facility_code = ""
        self.pol_port_code = ""
        self.new_ext_voyage = ""
        self.de_list2 = []
        self.de_list1 = []
        self.outbound_haulage = ""

    @staticmethod
    def of(data: Any) -> 'ScheduleDetail':
        """mapping data to ScheduleDetail

        Args:
            data (Any): data object

        Returns:
            ScheduleDetail: mapping result
        """
        schedule_detail = ScheduleDetail()
        schedule_detail.pod = data.pod
        schedule_detail.rev_facility_code = data.revFacilityCode
        schedule_detail.available = data.available
        schedule_detail.dir = data.dir
        schedule_detail.pol = data.pol
        schedule_detail.ata = data.ata
        schedule_detail.atd = data.atd
        schedule_detail.cargo_nature = data.cargoNature
        schedule_detail.eta = data.eta
        schedule_detail.etd = data.etd
        schedule_detail.ext_voyage = data.extVoyage
        schedule_detail.pol_facility_code = data.polFacilityCode
        schedule_detail.vessel = data.vessel
        schedule_detail.row_num = data.rowNum
        schedule_detail.vgm_cutoff_dt = data.vgmCutoffDt
        schedule_detail.vessel_code = data.vesselCode
        schedule_detail.id = data.id
        schedule_detail.cut_off = data.cutOff
        schedule_detail.pod_facility_code = data.podFacilityCode
        schedule_detail.leg_sequence = data.legSequence
        schedule_detail.transit_time = data.transitTime
        schedule_detail.pod_port_code = data.podPortCode
        schedule_detail.voyage = data.voyage
        schedule_detail.inbound_haulage = data.inboundHaulage
        schedule_detail.si_cutoff = data.siCutoff
        schedule_detail.r24_cutoff = data.r24Cutoff
        schedule_detail.service = data.service
        schedule_detail.deli_facility_code = data.deliFacilityCode
        schedule_detail.pol_port_code = data.polPortCode
        schedule_detail.new_ext_voyage = data.newExtVoyage
        schedule_detail.de_list2 = data.deList2
        schedule_detail.de_list1 = data.deList1
        schedule_detail.outbound_haulage = data.outboundHaulage

        return schedule_detail
