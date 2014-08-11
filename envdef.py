# ----------------------------- #
#  Test Environment Definition  #
# ----------------------------- #

###
### Jubatus Configuration
###
env.prefix('/opt/jubatus')
#env.prefix('/tmp/jubatus')
#env.variable('LD_LIBRARY_PATH', '/tmp/jubatus/lib:/opt/jubatus/lib')

###
### Test Node Configuration
###
env.node('127.0.0.1', range(19199,19299))
#env.node('127.0.0.1', 19199)

###
### ZooKeeper Configuration
###
env.zookeeper('127.0.0.1', 2181)

###
### Miscellaneous Node Configuration
###
env.workdir('/tmp')
env.cluster_prefix('sample')
#env.remote_process_timeout(300)

###
### Test Parameters
###
env.include('envdef_local.py')
