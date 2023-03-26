import multiprocessing
import importlib

sub_directory_name = "urlCollection"

def run_job(module_name):
    module_name = sub_directory_name + "." + module_name
    module = importlib.import_module(module_name)
    return module.gatherUrls()

def run():
    module_names = ['moreCherryUrlsCollector', 'porternaUrlsCollector', 'theVerlinUrlsCollector']

    # Create a multiprocessing pool with a maximum of 3 workers
    with multiprocessing.Pool(3) as pool:
        # Map the run_job function to each module name in parallel
        results = [pool.apply_async(run_job, args=(module_name,)) for module_name in module_names]
        output = []
        for result in results:
            try:
                output.append(result.get())
            except Exception as e:
                print(f"Error occurred while getting result: {e}")

    return output # return [defaultdict<list>{ shop_name : [each site total url]}]