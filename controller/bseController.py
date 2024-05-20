import traceback

from controller.AlgorithmParameter import BSEAlgorithmParameterRequestPython
from BSE import market_session
import random


def convert_java_to_python(java_obj):
    start_time = java_obj.getStartTime()
    end_time = java_obj.getEndTime()
    seller_range_from = java_obj.getSellerRangeFrom()
    seller_range_to = java_obj.getSellerRangeTo()
    buyer_range_from = java_obj.getBuyerRangeFrom()
    buyer_range_to = java_obj.getBuyerRangeTo()
    step_mode = java_obj.getStepMode()
    order_interval = java_obj.getOrderInterval()
    sellers_spec = list(dict(java_obj.getSellersSpec()).items())  # Converting Java map to Python dictionary
    buyers_spec = list(dict(java_obj.getBuyersSpec()).items())
    trial_id = java_obj.getTrialId()
    time_mode = java_obj.getTimeMode()

    return BSEAlgorithmParameterRequestPython(
        start_time, end_time, seller_range_from, seller_range_to,
        buyer_range_from, buyer_range_to, step_mode, order_interval,
        sellers_spec, buyers_spec, trial_id, time_mode
    )


class AlgorithmParameterTransfer(object):

    def __str__(self):
        return f"AlgorithmParameterTransfer from Python side"

    def toString(self):
        return self.__str__()

    # tested
    def helloBSE(self):
        print("BSE hello!")

    # TODO not test
    def transferAlgorithmParameter(self, java_obj):
        print("proxy function {transferAlgorithmParameter} is being called")
        parameters = convert_java_to_python(java_obj)
        try:
            self.runBSE(parameters)
            print("Received request with trial ID:", parameters.trial_id)
        except Exception as e:
            print("Exception caught", str(e))
            traceback.print_exc()
            return "Failure"
        return "Success"

    # def runBSE(self, parameters: BSEAlgorithmParameterRequestPython):
    #     seller_range = (parameters.seller_range_from, parameters.seller_range_to)
    #     buyer_range = (parameters.buyer_range_from, parameters.buyer_range_to)
    #     supply_schedule = [{'from': parameters.start_time, 'to': parameters.end_time,
    #                         'ranges': [seller_range], 'stepmode': parameters.step_mode}]
    #     demand_schedule = [{'from': parameters.start_time, 'to': parameters.end_time,
    #                         'ranges': [buyer_range], 'stepmode': parameters.step_mode}]
    #     order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
    #                    'interval': parameters.order_interval, 'timemode': parameters.end_time}
    #     seller_spec = parameters.sellers_spec
    #     buyer_spec = parameters.buyers_spec
    #     traders_spec = {'sellers': seller_spec, 'buyers': buyer_spec}
    #     verbose = False
    #     dump_flags = {'dump_blotters': False, 'dump_lobs': False, 'dump_strats': False,
    #                   'dump_avgbals': True, 'dump_tape': False}
    #     # dump_all = True
    #     random.seed(100)
    #     market_session(parameters.trial_id, parameters.start_time, parameters.end_time,
    #                    traders_spec, order_sched, dump_flags, verbose)
    def runBSE(self, parameters: BSEAlgorithmParameterRequestPython):
        start_time = parameters.start_time
        end_time = parameters.end_time
        seller_range = (parameters.seller_range_from, parameters.seller_range_to)
        buyer_range = (parameters.buyer_range_from, parameters.buyer_range_to)
        supply_schedule = [{'from': start_time, 'to': end_time,
                            'ranges': [seller_range], 'stepmode': parameters.step_mode}]
        demand_schedule = [{'from': start_time, 'to': end_time,
                            'ranges': [buyer_range], 'stepmode': parameters.step_mode}]
        order_interval = parameters.order_interval
        order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
                       'interval': order_interval, 'timemode': parameters.time_mode}
        sellers_spec = parameters.sellers_spec
        buyers_spec = parameters.buyers_spec
        traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec}
        verbose = False
        trial_id = parameters.trial_id
        dump_flags = {'dump_blotters': False, 'dump_lobs': False, 'dump_strats': False,
                      'dump_avgbals': True, 'dump_tape': False}
        random.seed(100)
        market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)

    class Java:
        implements = ["com.yupi.springbootinit.model.py4jInterface"]


# Make sure that the python code is started first.
# Then execute: java -cp py4j.jar py4j.examples.SingleThreadClientApplication
from py4j.java_gateway import JavaGateway, CallbackServerParameters

simple_hello = AlgorithmParameterTransfer()
gateway = JavaGateway(
    callback_server_parameters=CallbackServerParameters(),
    python_server_entry_point=simple_hello)
print("Starting bse...")
gateway.start_callback_server()
