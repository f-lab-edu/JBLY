import multiprocessing
import importlib

sub_directory_name = "parsing"

def run_job(module_name, response):
    module_name = sub_directory_name + "." + module_name
    module = importlib.import_module(module_name)
    return module.get_total_products(response)

def crawling_each_site(chunked_urls):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = [pool.apply_async(run_job, args=(module_name, response)) for module_name, responses in
                   chunked_urls.items() for response in responses]
        output = []
        for result in results:
            try:
                output.append(result.get())
            except Exception as e:
                print(f"Error occurred while getting result: {e}")
        pool.close()
        pool.join()
    return output
