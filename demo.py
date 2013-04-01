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


if gtd.task_exists('test 1'):
	task_1 = gtd.get_task_uuid('test 1')
	if gtd.context_exists('context 1'):
		context_1 = gtd.get_context_uuid('context 1')
		gtd.task_by_uuid(task_1).add_context(context_1)

gtd.dump_tasks()
gtd.dump_contexts()
