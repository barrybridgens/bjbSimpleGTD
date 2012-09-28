#

from bjbSimpleGTD import simpleGTD

gtd = simpleGTD.simpleGTD()

gtd.add_task('test 1')
gtd.add_task('test 2')
gtd.add_task('test 3')
gtd.add_task('test another one')

gtd.add_context('context 1')
gtd.add_context('context 2')
gtd.add_context('context 3')
gtd.add_context('context another one with a long name')

gtd.dump_tasks()
gtd.dump_contexts()
