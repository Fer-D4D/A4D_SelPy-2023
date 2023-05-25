from Team.Fer.core.Common_II import TinyCore
from Team.Fer.Sauce.Second_Challenge_Week_05.work_flows import workflow_mapper

utils = TinyCore()
utils.open_xlsx("EZSauceTest.xlsx")

workflow_mapper(utils.get_test_data_from_xlsx())
