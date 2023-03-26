import multiprocessing
import importlib

sub_directory_name = "urlCollection"

def run_job(module_name):
    module_name = sub_directory_name + "." + module_name
    module = importlib.import_module(module_name)
    return module.gatherUrls()

'''
apply_async() 메소드의 반환값으로 AsyncResult 객체를 반환하며,
이 객체의 get() 메소드를 호출하면 해당 프로세스가 완료될 때까지 대기하게 됩니다.
'''
def run():
    module_names = ['moreCherryUrlsCollector', 'porternaUrlsCollector', 'theVerlinUrlsCollector']

    with multiprocessing.Pool(3) as pool:
        results = [pool.apply_async(run_job, args=(module_name,)) for module_name in module_names]
        output = []
        for result in results:
            try:
                output.append(result.get())
            except Exception as e:
                print(f"Error occurred while getting result: {e}")

    return output # return [defaultdict<list>{ shop_name : [each site total url]}]