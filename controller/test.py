from BSE import market_session
import random

start_time = 0
end_time = 60 * 10

seller_range = (80, 310)
buyer_range = (250, 490)

supply_schedule = [{'from': start_time, 'to': end_time,
                    'ranges': [seller_range], 'stepmode': 'fixed'}]
demand_schedule = [{'from': start_time, 'to': end_time,
                    'ranges': [buyer_range], 'stepmode': 'fixed'}]

# Smith used periodic updating -- at the start of each "day" all traders are issued with fresh assignments.
# Let's do that once every 30 seconds
order_interval = 30
order_sched = {'sup': supply_schedule, 'dem': demand_schedule,
               'interval': order_interval, 'timemode': 'periodic'}

# time mode : periodic, drip-fixed, drip-jitter, drip-poisson
# periodic: periodic replenishment of orders, once every 30 seconds.


sellers_spec = [('ZIC', 10), ('SHVR', 10), ('ZIP', 10)]
buyers_spec = sellers_spec
traders_spec = {'sellers': sellers_spec, 'buyers': buyers_spec}

verbose = False

trial_id = 'test'
dump_flags = {'dump_blotters': True, 'dump_lobs': True, 'dump_strats': True,
              'dump_avgbals': True, 'dump_tape': True}

random.seed(100)

market_session(trial_id, start_time, end_time, traders_spec, order_sched, dump_flags, verbose)
