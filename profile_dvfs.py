import os
import subprocess
import lamp_dvfs


##

cpu_freq_list = [200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000,1300000,1400000]
gpu_freq_list = [600000000,543000000,480000000,420000000,350000000,266000000,177000000]
mem_freq_list = [165000000,206000000,275000000,413000000,543000000,633000000,728000000,825000000]

# gpu driven governor setting
gpu_cluster = {
    600000000: {'cpu':1400000 , 'mem':825000000},
    543000000: {'cpu':1200000 , 'mem':728000000},
    480000000: {'cpu':1000000 , 'mem':633000000},
    420000000: {'cpu':800000 , 'mem':543000000},
    350000000: {'cpu':600000 , 'mem':413000000},
    266000000: {'cpu':400000 , 'mem':275000000},
    177000000: {'cpu':200000 , 'mem':165000000}
 }

# memory driven governor setting
mem_cluster = {
    165000000: {'gpu':177000000, 'cpu':200000},
    206000000: {'gpu':177000000, 'cpu':400000},
    275000000: {'gpu':266000000, 'cpu':600000},
    413000000: {'gpu':350000000, 'cpu':800000},
    543000000: {'gpu':420000000, 'cpu':1000000},
    633000000: {'gpu':480000000, 'cpu':1100000},
    728000000: {'gpu':543000000, 'cpu':1200000},
    825000000: {'gpu':600000000, 'cpu':1400000}
}
# cpu driven governor setting
cpu_cluster = {
    200000: {'gpu':177000000, 'mem':165000000},
    300000: {'gpu':177000000, 'mem':165000000},
    400000: {'gpu':177000000, 'mem':165000000},
    500000: {'gpu':266000000, 'mem':275000000},
    600000: {'gpu':266000000, 'mem':275000000},
    700000: {'gpu':350000000, 'mem':413000000},
    800000: {'gpu':350000000, 'mem':413000000},
    900000: {'gpu':420000000, 'mem':543000000},
    1000000: {'gpu':420000000, 'mem':543000000},
    1100000: {'gpu':480000000, 'mem':633000000},
    1200000: {'gpu':480000000, 'mem':633000000},
    1300000: {'gpu':600000000, 'mem':825000000},
    1400000: {'gpu':600000000, 'mem':825000000}
}

cpu_nu05_cluster0 = {
    200000: {'gpu':600000000, 'mem':543000000},
    300000: {'gpu':350000000, 'mem':633000000},
    400000: {'gpu':177000000, 'mem':825000000},
    500000: {'gpu':350000000, 'mem':543000000},
    600000: {'gpu':543000000, 'mem':543000000},
    700000: {'gpu':350000000, 'mem':633000000},
    800000: {'gpu':350000000, 'mem':543000000},
    900000: {'gpu':177000000, 'mem':543000000},
    1000000: {'gpu':420000000, 'mem':275000000},
    1100000: {'gpu':480000000, 'mem':275000000},
    1200000: {'gpu':480000000, 'mem':206000000},
    1300000: {'gpu':350000000, 'mem':206000000},
    1400000: {'gpu':177000000, 'mem':165000000}
}

mem_cluster0 = {
    165000000: {'gpu':177000000, 'cpu':1400000},
    206000000: {'gpu':480000000, 'cpu':1200000},
    275000000: {'gpu':420000000, 'cpu':1000000},
    413000000: {'gpu':177000000, 'cpu':900000},
    543000000: {'gpu':543000000, 'cpu':700000},
    633000000: {'gpu':350000000, 'cpu':600000},
    728000000: {'gpu':350000000, 'cpu':500000},
    825000000: {'gpu':177000000, 'cpu':400000}
}


cpu_nu05_cluster1 = {
    200000: {'gpu':480000000, 'mem':543000000},
    300000: {'gpu':480000000, 'mem':633000000},
    400000: {'gpu':177000000, 'mem':825000000},
    500000: {'gpu':350000000, 'mem':543000000},
    600000: {'gpu':350000000, 'mem':543000000},
    700000: {'gpu':350000000, 'mem':633000000},
    800000: {'gpu':350000000, 'mem':543000000},
    900000: {'gpu':177000000, 'mem':633000000},
    1000000: {'gpu':420000000, 'mem':728000000},
    1100000: {'gpu':350000000, 'mem':633000000},
    1200000: {'gpu':350000000, 'mem':825000000},
    1300000: {'gpu':350000000, 'mem':728000000},
    1400000: {'gpu':177000000, 'mem':633000000}
}

'''
Run more clustetring to find the optimal power performance
'''



power_policy = lamp_dvfs.OSLScheduler()
## CPU driven governor
power_policy.set_cluster(cpu_nu05_cluster1)
## Memory driven governor
# power_policy.set_cluster(mem_cluster0)
# GPU driven governor
# power_policy.set_cluster(gpu_cluster)
## run
power_policy.run()
 