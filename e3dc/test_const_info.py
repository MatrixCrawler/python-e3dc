from e3dc.const import Const


class TestConstInfo(object):
    def test_time_info_string(self):
        assert Const.Info.TIME == 'INFO_REQ_UTC_TIME'
