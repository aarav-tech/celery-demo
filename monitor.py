from celery import Celery

def my_monitor(app):
    state = app.events.State()

    def announce_failed_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print(f'TASK FAILED: {task.name}[{task.uuid}]')

    def announce_succeeded_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print(f'TASK SUCCEEDED: {task.name}[{task.uuid}]')

    def worker_online_handler(event):
        state.event(event)
        print("New worker gets online")
        print(event['hostname'], event['timestamp'], event['freq'], event['sw_ver'])

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-failed': announce_failed_tasks,
                'task-succeeded': announce_succeeded_tasks,
                'worker-online': worker_online_handler,
                '*': state.event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    app = Celery('celery_demo')
    my_monitor(app)