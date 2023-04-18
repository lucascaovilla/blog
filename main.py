l = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x**2, l)))


def runb_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()