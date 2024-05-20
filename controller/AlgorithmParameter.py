class BSEAlgorithmParameterRequestPython:
    def __init__(
            self, start_time, end_time, seller_range_from,
            seller_range_to, buyer_range_from, buyer_range_to,
            step_mode, order_interval, sellers_spec, buyers_spec,
            trial_id, time_mode):
        self.start_time = start_time
        self.end_time = end_time
        self.seller_range_from = seller_range_from
        self.seller_range_to = seller_range_to
        self.buyer_range_from = buyer_range_from
        self.buyer_range_to = buyer_range_to
        self.step_mode = step_mode
        self.order_interval = order_interval
        self.sellers_spec = sellers_spec
        self.buyers_spec = buyers_spec
        self.trial_id = trial_id
        self.time_mode = time_mode
