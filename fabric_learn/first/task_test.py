from fabric.api import run, task


def taskA():
    run('ls')


def taskB():
    run('whoami')


# @task(aliases="abc")
# def task_a_b_c():
#     run("ls")

# @task
# def migrate():
#     pass


# @task
# def push():
#     pass


# @task
# def provision():
#     pass


# @task
# def full_deploy():
#     if not provisioned:
#         provision()
#     push()
#     migrate()
