def priority_scheduler(jobs):
    heap = []
    order = 0

    for job, priority in jobs:
        heap.insert((-priority, order, job))
        order += 1

    release_order = []

    while heap.size() > 0:
        priority, order, job = heap.extract()
        release_order.append(job)

    print("Release Order:", release_order)


jobs = [
    ("Job A", 2),
    ("Job B", 5),
    ("Job C", 1),
    ("Job D", 4)
]

priority_scheduler(jobs)
