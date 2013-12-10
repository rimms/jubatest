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

###
### ZooKeeper Configuration
###
env.zookeeper('127.0.0.1', 2181)

###
### Miscellaneous Node Configuration
###
env.workdir('/tmp')
env.cluster_prefix('sample')

###
### Test Parameters
###
basedir = '/home/kenichi/Development'
env.param('JUBATUS_TUTORIAL_DIR', basedir + '/jubatus-tutorial-python')
env.param('JUBATUS_BENCH_CLASSIFIER', basedir + '/jubatus-benchmark/jubatus-bench-classifier')
env.param('JUBATUS_BENCH_CLASSIFIER_DATASET', basedir + '/jubatus-benchmark/url_svmlight/Day0.svm')
